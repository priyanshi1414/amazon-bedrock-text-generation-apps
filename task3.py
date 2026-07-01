# Import the required libraries for AWS service interaction and JSON processing.
import boto3
import json

# Connect to Amazon Bedrock.
bedrock = boto3.client("bedrock-runtime")
pet_type = input("Enter your pet type (dog/cat): ")
ingredients = input("Enter your ingredients separated by commas: ")
allergies = input("Enter any allergies separated by commas (press Enter if none): ")
prompt = f" Create a safe treat recipe for a {pet_type} using these ingredients: {ingredients}."

if allergies.strip():
    prompt += f" Avoid these allergies: {allergies}."

max_tokens = 512
temperature = 0.7
request = {
    "messages": [{"role": "user", "content": [{"text": prompt}]}],
    "inferenceConfig": {
        "temperature": temperature,
        "topP": 0.9,
    },
}
response = bedrock.invoke_model(
    modelId="amazon.nova-lite-v1:0", body=json.dumps(request)
)
response_body = json.loads(response["body"].read())

print(
    f"\nRecipe generated with {max_tokens} max tokens and a temperature of {temperature}.\n"
)

if response_body["output"]["message"]["content"][0]["text"].startswith(
    " - The generated text has been blocked"
):
    print(
        "I apologize, but I cannot provide specific pet food recipes. For your pet's safety, please consult with a veterinarian."
    )
else:
    print(response_body["output"]["message"]["content"][0]["text"])
