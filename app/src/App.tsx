import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { customTheme } from "./Themes/themeController";
import { useEffect, useState } from "react";
import { getSendTranslated } from "./APIs/sendTranslated";
import { RawTranslationData, TranslationData } from "./Types/translation_data";
import TranslationTable from "./UI/TranslationTable";
import BasicButton from "./UI/PrimaryButton";
import PrimaryButton from "./UI/PrimaryButton";
import SecondaryButton from "./UI/SecondaryButton";
import SlideShow from "./UI/SlideShow";
function App() {
  const [translatedDataRows, setTranslatedDataRows] = useState<
    TranslationData[]
  >([]);
  const [tableMode, setTableMode] = useState<boolean>(false);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const data: RawTranslationData = await getSendTranslated();
        // Handle data here
        setTranslatedDataRows(data.data);
      } catch (error) {
        console.error(error);
        // Handle errors here
      }
    };

    fetchData();

    return () => {
      // Cleanup code if needed
    };
  }, []);

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        gap: 10,
        backgroundColor: customTheme.app.background_color,
        height: "100vh",
      }}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          backgroundColor: customTheme.app.widget.background_color,
          justifyContent: "space-evenly",
          alignItems: "center",
          padding: 20,
          borderRadius: 20,
          margin: 0,
          width: 600,
          height: 100,
        }}
      >
        <PrimaryButton text={"Table mode"} onClick={() => setTableMode(true)} />
        <SecondaryButton
          text={"Slide mode"}
          onClick={() => setTableMode(false)}
        />
      </div>
      <div
        style={{
          backgroundColor: customTheme.app.widget.background_color,
          borderRadius: 0,
          margin: 0,
        }}
      >
        {tableMode ? (
          <TranslationTable translatedDataRows={translatedDataRows} />
        ) : (
          <SlideShow translatedDataRows={translatedDataRows}></SlideShow>
        )}
      </div>
    </div>
  );
}

export default App;
