
# app.py

import websaw
from websaw import DefaultContext
import jwt
from jwt.algorithms import RSAAlgorithm
import requests

class MyApp(websaw.Application):
    pass

app = MyApp(__name__)

@app.route('GET', '/')
def verify_token(ctx: DefaultContext):
    # Get the Authorization header
    auth_header = ctx.request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return ctx.response.json({'error': 'Authorization header missing or invalid'}, status=401)

    # Extract the token
    token = auth_header.split(' ')[1]

    # Try verifying with public key from file
    try:
        with open('public_key.pem', 'r') as f:
            public_key = f.read()
        payload = jwt.decode(token, public_key, algorithms=['RS256'])
        return ctx.response.json({'message': 'Token is valid', 'payload': payload})
    except Exception as e:
        # Verification with public key failed, try JWKS URL
        try:
            jwks_url = 'https://example.com/.well-known/jwks.json'  # Replace with your JWKS URL
            jwks_response = requests.get(jwks_url)
            jwks_response.raise_for_status()
            jwks = jwks_response.json()
            unverified_header = jwt.get_unverified_header(token)
            kid = unverified_header['kid']
            public_keys = {
                jwk['kid']: RSAAlgorithm.from_jwk(jwk)
                for jwk in jwks['keys']
            }
            key = public_keys.get(kid)
            if key is None:
                return ctx.response.json({'error': 'Public key not found in JWKS'}, status=401)
            payload = jwt.decode(token, key=key, algorithms=['RS256'])
            return ctx.response.json({'message': 'Token is valid', 'payload': payload})
        except Exception as e:
            return ctx.response.json({'error': 'Token verification failed', 'details': str(e)}, status=401)

