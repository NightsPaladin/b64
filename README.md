# b64 - Command-line Base64 Encoder/Decoder

- Produces HTTP Basic Auth compatible Base64 strings

Basic usage
------------------------------

Encoding a string:

$ ./b64.py -e | --encode "\<string-to-encode\>"

$ echo "string-to-encode" | ./b64 -e | --encode


Decoding a string:

$ ./b64.py -d | --decode "\<string-to-decode\>"

$ echo "string-to-decode" | ./b64 -d | --decode