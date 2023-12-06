import axios from "axios";
import { RawTranslationData } from "../Types/translation_data";

const BASE_URL = process.env.REACT_APP_BASE_URL;

export async function getSendTranslated() {
  try {
    const endpoint = "send_translated";
    const url = BASE_URL + endpoint;
    const instance = axios.create({ baseURL: BASE_URL });
    const response = await instance.get("/send_translated");
    // Extract data from the response
    const data: RawTranslationData = response.data;
    return data;
  } catch (error) {
    console.error(error);
    // Handle errors here or rethrow to propagate the error
    throw error;
  }
}

export async function postPronunciation(
  translatedText: string,
  outLang: string
) {
  try {
    const endpoint = "pronunciation";
    const url = BASE_URL + endpoint;

    // Create a FormData object to send POST data
    const formData = new FormData();
    formData.append("translated_text", translatedText);
    formData.append("out_lang", outLang);

    // Send a POST request to the server
    const response = await axios.post(url, formData, {
      responseType: "blob", // Set response type to handle audio file
    });

    // Handle the audio file in the response
    const audioBlob = response.data;
    const audioUrl = URL.createObjectURL(audioBlob);

    // Play the audio or perform further actions
    const audio = new Audio(audioUrl);
    audio.play();

    return audioUrl; // Return the URL if needed
  } catch (error) {
    console.error(error);
    throw error;
  }
}
