import { useState } from "react";
import axios from "axios";

function Upload({ refreshRecords }) {
  API="https://breathe-esg-prototype-8t0u.onrender.com"
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
        `${API}/api/upload/`,
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