# Import the required libraries for AWS service interaction and JSON processing.
import boto3
import json

bedrock = boto3.client("bedrock-runtime")

# Set up the prompt and temperature.
prompt = "Write a short poem about a curious cat"  # Use this example, or create one of your own!
temperature = 0.9  # TODO: when you run the code, try adjusting the temperature value between 0.0 and 1.0 to experiment with randomness.
request = {
    "messages": [{"role": "user", "content": [{"text": prompt}]}],
    "inferenceConfig": {"temperature": temperature},
}
response = bedrock.invoke_model(
    modelId="amazon.nova-lite-v1:0", body=json.dumps(request)
)

response_body = json.loads(response["body"].read())

print(response_body["output"]["message"]["content"][0]["text"])
