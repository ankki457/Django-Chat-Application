const AWS = require('aws-sdk');

// Initialize S3
const s3 = new AWS.S3();

exports.handler = async (event) => {
    try {
        const bucketName = 'my-document-storage'; // Replace with your bucket name
        const { fileName, fileContent } = event;

        // Validate inputs
        if (!fileName || !fileContent) {
            return {
                statusCode: 400,
                body: JSON.stringify({ message: "Invalid input. Please provide fileName and fileContent." }),
            };
        }

        // Convert the file content (Base64) to a Buffer
        const buffer = Buffer.from(fileContent, 'base64');

        // Define the upload parameters
        const params = {
            Bucket: bucketName,
            Key: fileName,
            Body: buffer,
            ContentType: 'application/pdf', // Set based on file type
        };

        // Upload to S3
        await s3.upload(params).promise();

        return {
            statusCode: 200,
            body: JSON.stringify({ message: "File uploaded successfully!" }),
        };
    } catch (error) {
        console.error(error);
        return {
            statusCode: 500,
            body: JSON.stringify({ message: "Failed to upload the file.", error: error.message }),
        };
    }
};
