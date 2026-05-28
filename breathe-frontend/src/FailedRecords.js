function FailedRecords({ failedRecords }) {

  return (

    <div style={{ marginTop: "30px" }}>

      <h2>Failed Records</h2>

      <table border="1" cellPadding="10">

        <thead>
          <tr>
            <th>ID</th>
            <th>Error</th>
            <th>Payload</th>
          </tr>
        </thead>

        <tbody>

          {failedRecords.map((record) => (

            <tr key={record.id}>

              <td>{record.id}</td>

              <td>{record.error_message}</td>

              <td>
                {JSON.stringify(record.raw_payload)}
              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default FailedRecords;