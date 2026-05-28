import { useEffect, useState } from "react";
import axios from "axios";

import Upload from "./Upload";
import Dashboard from "./Dashboard";
import FailedRecords from "./FailedRecords";

function App() {
  API="https://breathe-esg-prototype-8t0u.onrender.com"
  const [records, setRecords] = useState([]);

  const [failedRecords, setFailedRecords] = useState([]);

  const fetchRecords = async () => {

    try {

      const response = await axios.get(
        `${API}/api/records/`
      );

      setRecords(response.data);

    } catch (error) {

      console.error(error);
    }
  };

  const fetchFailedRecords = async () => {

    try {

      const response = await axios.get(
        `${API}/api/failed-records/`
      );

      setFailedRecords(response.data);

    } catch (error) {

      console.error(error);
    }
  };

  const refreshAll = () => {

    fetchRecords();
    fetchFailedRecords();
  };

  useEffect(() => {

  refreshAll();

// eslint-disable-next-line react-hooks/exhaustive-deps
}, []);

  return (

    <div style={{ padding: "20px" }}>

      <h1>Breathe ESG Prototype</h1>

      <Upload refreshRecords={refreshAll} />

      <Dashboard
        records={records}
        refreshRecords={refreshAll}
      />

      <FailedRecords
        failedRecords={failedRecords}
      />

    </div>
  );
}

export default App;