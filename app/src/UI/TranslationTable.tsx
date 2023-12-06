import { DataGrid, GridColDef, GridValueGetterParams } from "@mui/x-data-grid";
import { TranslationData } from "../Types/translation_data";
import { postPronunciation } from "../APIs/sendTranslated";
import VolumeUpIcon from "@mui/icons-material/VolumeUp";
export default function TranslationTable({
  translatedDataRows,
}: {
  translatedDataRows: TranslationData[];
}) {
  const columns: GridColDef[] = [
    {
      field: "word",
      headerName: "Word",
      width: 90,
      align: "center",
      headerAlign: "center",
    },
    {
      field: "count",
      headerName: "Count",
      type: "number",
      width: 130,
      align: "center",
      headerAlign: "center",
    },
    {
      field: "pronunciation",
      headerName: "Pronunciation",
      width: 130,
      align: "center",
      headerAlign: "center",
    },
    {
      field: "translation",
      headerName: "Translation",
      width: 130,
      align: "center",
      headerAlign: "center",
    },
    {
      field: "language",
      headerName: "Language",
      width: 130,
      align: "center",
      headerAlign: "center",
    },
    {
      field: "sound",
      headerName: "Sound",
      width: 130,
      align: "center",
      headerAlign: "center",
      renderCell: (params) => {
        const { translation, language_code } = params.row;
        return (
          <div
            style={{ cursor: "pointer" }}
            onClick={() =>
              translatedDataRows &&
              postPronunciation(translation, language_code)
            }
          >
            <VolumeUpIcon />
          </div>
        );
      },
    },
  ];

  return (
    <div
      style={{
        height: 600,
      }}
    >
      <DataGrid
        rows={translatedDataRows}
        columns={columns}
        initialState={{
          pagination: {
            paginationModel: { page: 0, pageSize: 10 },
          },
        }}
        getRowId={(row: TranslationData) => row.word}
        pageSizeOptions={[5, 10]}
      />
    </div>
  );
}
