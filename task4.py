# Import the required libraries for AWS service interaction and JSON processing.
import boto3
import json

# Connect to Amazon Bedrock.
bedrock = boto3.client("bedrock-runtime")

# Define a list of pet dictionaries.
pets = [
    {"name": "Buddy", "type": "dog", "age": 3, "description": ""},
    {"name": "Mittens", "type": "cat", "age": 5, "description": ""},
    {"name": "Lucky", "type": "dog", "age": 6, "description": ""},
]
# Process each pet.
for pet in pets:

    # Set temperature based on pet type.
    if pet["type"] == "cat":
        temperature = 0.9
    else:
        temperature = 0.3

    # Create the prompt.
    prompt = f"Write an engaging adoption description for a {pet['age']}-year-old {pet['type']} named {pet['name']}."

    # Create the request.
    request = {
        "messages": [{"role": "user", "content": [{"text": prompt}]}],
        "inferenceConfig": {"temperature": temperature, "topP": 0.9},
    }

    # Send the request.
    response = bedrock.invoke_model(
        modelId="amazon.nova-lite-v1:0", body=json.dumps(request)
    )

    # Process the response.
    response_body = json.loads(response["body"].read())
    pet["description"] = response_body["output"]["message"]["content"][0]["text"]

# Display the results.
print("\nGenerated Pet Descriptions\n")

for pet in pets:
    print(f"Name: {pet['name']}")
    print(f"Type: {pet['type']}")
    print(f"Age: {pet['age']}")
    print("Description:")
    print(pet["description"])
    print("-" * 50)
