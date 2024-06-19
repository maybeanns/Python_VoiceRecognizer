# Python_VoiceRecognizer

## How it looks like:
![voice recognizer](https://github.com/maybeanns/Python_VoiceRecognizer/assets/140887479/dd70b50e-4847-4618-a663-20d008aef4cd)
## How it works:

### Requirements
- Python 3.6 or higher
- `speech_recognition` library
- `pyttsx3` library
- Internet connection for the Google Web Speech API
  
1. **Initialization**:
   - The script initializes a recognizer instance from the `speech_recognition` library.
   - The script enters an infinite loop to continuously listen for microphone input.

2. **Listening**:
   - Within each loop iteration, the microphone is activated and the ambient noise level is adjusted to improve recognition accuracy.
   - The script listens for spoken input and captures it as audio.

3. **Recognition**:
   - The captured audio is sent to the Google Web Speech API to be converted into text.
   - The recognized text is converted to lowercase and printed.

4. **Error Handling**:
   - If the speech is unintelligible, an `UnknownValueError` is caught, and the script continues to the next iteration.
   - If there is an issue with the API request, a `RequestError` is caught, and the script breaks out of the loop.

✌️ Peace!
