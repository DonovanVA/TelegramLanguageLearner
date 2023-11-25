import axios from "axios";
import { RawTranslationData } from "../Types/translation_data";

const BASE_URL = process.env.REACT_APP_BASE_URL;

export async function getSendTranslated() {
  try {
    const endpoint = "send_translated";
    const url = BASE_URL + endpoint;
    console.log(url);
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
