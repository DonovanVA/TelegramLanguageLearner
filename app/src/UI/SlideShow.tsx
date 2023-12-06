import React, { useReducer } from "react";
import { TranslationData } from "../Types/translation_data";
import ArrowBackIosNewIcon from "@mui/icons-material/ArrowBackIosNew";
import ArrowForwardIosIcon from "@mui/icons-material/ArrowForwardIos";
import VolumeUpIcon from "@mui/icons-material/VolumeUp";
import { customTheme } from "../Themes/themeController";
import { postPronunciation } from "../APIs/sendTranslated";
interface State {
  currentIndex: number;
}

type Action = { type: "NEXT" } | { type: "PREV" };
export default function SlideShow({
  translatedDataRows,
}: {
  translatedDataRows: TranslationData[];
}) {
  const initialState = {
    currentIndex: 0,
  };

  const reducer = (state: State, action: Action) => {
    switch (action.type) {
      case "NEXT":
        return {
          ...state,
          currentIndex:
            state.currentIndex === translatedDataRows.length - 1
              ? 0
              : state.currentIndex + 1,
        };
      case "PREV":
        return {
          ...state,
          currentIndex:
            state.currentIndex === 0
              ? translatedDataRows.length - 1
              : state.currentIndex - 1,
        };
      default:
        return state;
    }
  };

  const [state, dispatch] = useReducer(reducer, initialState);

  const { currentIndex } = state;
  const currentData = translatedDataRows[currentIndex];

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "row",
        height: 200,
        width: 600,
        justifyContent: "space-between",
        alignItems: "center",
        padding: 10,
      }}
    >
      <div
        style={{ cursor: "pointer" }}
        onClick={() => dispatch({ type: "PREV" })}
      >
        <ArrowBackIosNewIcon />
      </div>

      <div
        style={{
          display: "flex",
          flexDirection: "row",
        }}
      >
        {/* Render the content of the current index */}
        <div
          style={{
            display: "flex",
            flexDirection: "row",
            justifyContent: "space-between",
            width: "100%",
            gap: 20,
          }}
        >
          <div
            style={{
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
            }}
          >
            <h2>Number</h2>
            <h3>#{state.currentIndex + 1}</h3>
          </div>

          <div
            style={{
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
            }}
          >
            <h2>Word</h2>
            <h3>{currentData?.word}</h3>
          </div>
          <div
            style={{
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
            }}
          >
            <h2 style={{ color: customTheme.app.text.secondary }}>
              Translated
            </h2>
            <h3 style={{ color: customTheme.app.text.secondary }}>
              {currentData?.translation}
            </h3>
          </div>
          <div
            style={{
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
            }}
          >
            <h2 style={{ color: customTheme.app.text.secondary }}>
              Pronunciation
            </h2>
            <h3 style={{ color: customTheme.app.text.secondary }}>
              {currentData?.pronunciation}
            </h3>
          </div>
        </div>
        {/* Replace 'someField' with the field name you want to display */}
        {currentData?.translation && currentData?.language_code && (
          <div
            style={{ cursor: "pointer", marginTop:24, marginLeft: 20 }}
            onClick={() =>
              postPronunciation(
                currentData.translation,
                currentData.language_code
              )
            }
          >
            <VolumeUpIcon />
          </div>
        )}
      </div>

      <div
        style={{ cursor: "pointer" }}
        onClick={() => dispatch({ type: "NEXT" })}
      >
        <ArrowForwardIosIcon />
      </div>
    </div>
  );
}
