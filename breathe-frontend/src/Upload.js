import { useState } from "react";
import axios from "axios";

function Upload({ refreshRecords }) {

  const [file, setFile] = useState(null);

  const handleUpload = async () => {

    if (!file) {
      alert("Select a file");
      return;
    }

    const formData = new FormData();

    formData.append("file", file);
    formData.append("source_type", "SAP");
    formData.append("organization_id", 1);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/api/upload/",
        formData
      );

      alert(
        `Uploaded ${response.data.records_created} records`
      );

      refreshRecords();

    } catch (error) {

      console.error(error);

      alert("Upload failed");
    }
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <h2>Upload ESG Data</h2>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={handleUpload}>
        Upload
      </button>
    </div>
  );
}

export default Upload;