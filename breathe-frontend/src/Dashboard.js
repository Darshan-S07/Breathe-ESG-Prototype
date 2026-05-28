import axios from "axios";

function Dashboard({ records, refreshRecords }) {

  const approveRecord = async (id) => {

    try {

      await axios.patch(
        `http://127.0.0.1:8000/api/approve/${id}/`,
        {
          status: "APPROVED"
        }
      );

      refreshRecords();

    } catch (error) {

      console.error(error);

      alert("Approval failed");
    }
  };

  return (
    <div>
      <h2>Normalized Records</h2>

      <table border="1" cellPadding="10">

        <thead>
          <tr>
            <th>ID</th>
            <th>Type</th>
            <th>Quantity</th>
            <th>Unit</th>
            <th>Emissions</th>
            <th>Status</th>
            <th>⚠️</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>

          {records.map((record) => (

            <tr key={record.id}>

              <td>{record.id}</td>

              <td>{record.activity_type}</td>

              <td>{record.normalized_quantity}</td>

              <td>{record.normalized_unit}</td>

              <td>{record.emissions_value}</td>

              <td>{record.status}</td>

              <td>
                {record.suspicious_flag ? "⚠️" : ""}
              </td>

              <td>

                {record.status !== "APPROVED" && (

                  <button
                    onClick={() => approveRecord(record.id)}
                  >
                    Approve
                  </button>

                )}

              </td>

            </tr>

          ))}

        </tbody>

      </table>
    </div>
  );
}

export default Dashboard;