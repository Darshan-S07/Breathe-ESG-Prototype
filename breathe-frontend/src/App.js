import { useEffect, useState } from "react";
import axios from "axios";

import Upload from "./Upload";
import Dashboard from "./Dashboard";
import FailedRecords from "./FailedRecords";

function App() {

  const [records, setRecords] = useState([]);

  const [failedRecords, setFailedRecords] = useState([]);

  const fetchRecords = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/api/records/"
      );

      setRecords(response.data);

    } catch (error) {

      console.error(error);
    }
  };

  const fetchFailedRecords = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/api/failed-records/"
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