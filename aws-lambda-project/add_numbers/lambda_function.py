exports.handler = async (event) => {
    // Extract numbers from the event body
    const { num1, num2 } = event;
    
    // Validate inputs
    if (typeof num1 !== 'number' || typeof num2 !== 'number') {
        return {
            statusCode: 400,
            body: JSON.stringify({ message: "Invalid input. Please provide two numbers." }),
        };
    }
    
    // Perform the addition
    const result = num1 + num2;

    return {
        statusCode: 200,
        body: JSON.stringify({ result }),
    };
};
