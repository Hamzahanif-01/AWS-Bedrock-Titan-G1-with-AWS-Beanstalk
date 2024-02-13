from flask import Flask, render_template, request, redirect, url_for, flash
import boto3
import json

application = Flask(__name__)

def invoke_titan_image(prompt):
    try:
        bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")
        request_data = {
            "taskType": "TEXT_IMAGE",
            "textToImageParams": {"text": prompt},
            "imageGenerationConfig": {
                "numberOfImages": 1,
                "quality": "standard",
                "cfgScale": 8.0,
                "height": 512,
                "width": 512,
                "seed": 0,
            },
        }
        response = bedrock.invoke_model(modelId="amazon.titan-image-generator-v1", body=json.dumps(request_data))
        response_body = json.loads(response["body"])
        base64_image_data = response_body["images"][0]
        return base64_image_data
    except Exception as e:
        print("Error invoking Titan image generator:", e)
        return None

@application.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt_data = request.form["prompt"]
        image_bytes = invoke_titan_image(prompt_data)
        if image_bytes:
            return render_template("index.html", image_data=image_bytes)
        else:
            flash("Failed to generate image from prompt. Please try again.", "error")
            return redirect(url_for("index"))
    return render_template("index.html")

if __name__ == "__main__":
    application.run(debug=True)
