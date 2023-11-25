import { BasicButtonProps } from "../Types/Buttons";
import { customTheme } from "../Themes/themeController";
export default function PrimaryButton({ text, onClick }: BasicButtonProps) {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        backgroundColor: customTheme.app.button.type_1.background_color,
        color: customTheme.app.button.type_1.text_color,
        height: 50,
        borderRadius: 10,
        width: 100,
        cursor: "pointer",
      }}
      onClick={onClick}
    >
      <p>{text}</p>
    </div>
  );
}
