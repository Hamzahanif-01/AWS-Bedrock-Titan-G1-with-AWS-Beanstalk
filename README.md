# Setting up Flask app for AWS Beanstalk for envoking AWS Titan G1 Model API


Your website's foundation lies in your Flask Python application. Ensure your main application file (Application.py) contains the necessary SDK code to utilize Bedrock services APIs seamlessly.

    
The Bedrock API implementation and the rest of the code for the application can be found here
A thing extra that you need to do is create a .ebextensionsfolder ( mostly hidden ) and within that folder have a file named EB_extensions.config which should direct your Beanstalk engine to your application's main file. The content of the file should be like

    option_settings:
        aws:elasticbeanstalk:container:python:
            WSGIPath: application:application
    
Now, there are multiple ways to upload your code onto the Elastic Beanstalk (EB) platform. 
You can either use an **Archive.zip** file 
Upload files to an **S3 bucket** and provide the location to the EB platform. 
Grant a **URL** with the relevant files

> IMPORTANT: Ensure only project files are compressed! NOT the entire
> project, it's a common mistake that is made and is hard to debug with
> your Beanstalk platform as it will not be able to locate the main file
> for your application
> 3. Utilizing AWS Bedrock Titan for Image Generation

AWS Bedrock offers a robust suite of tools for various AI and machine learning tasks. To use image generation services via Bedrock Titan, navigate to the Bedrock console and request access to the desired model by navigation to model access. Be mindful of the region's availability, as it impacts the model's accessibility. Once granted access ( usually takes around an hour or two ), integrate the services into your application 
For this project, we will choose the **AWS Titan Image Generation Model**
We will use this API in our Flask Application - API structure is provided for each foundational model on AWS Bedrock.

    { 	 "modelId": "amazon.titan-image-generator-v1", 	 "contentType": "application/json",  "accept": "application/json",  "body": "{\"textToImageParams\":{\"text\":\"this is where you place your input text\"},\"taskType\":\"TEXT_IMAGE\",\"imageGenerationConfig\":{\"cfgScale\":8,\"seed\":0,\"quality\":\"standard\",\"width\":1024,\"height\":1024,\"numberOfImages\":3}}" 
    }
