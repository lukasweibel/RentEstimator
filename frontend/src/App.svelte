<script>
  import Header from "./components/Header.svelte";

  let area = "";
  let rooms = "";
  let zip = "";
  let predictedValue = "";

  async function handleSubmit(event) {
    event.preventDefault();

    const url = "/predict";

    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          area,
          rooms,
          zip,
        }),
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }

      const result = await response.json();
      predictedValue = Math.round(result); // Assuming 'result' can be directly rounded
      console.log("Prediction Result:", predictedValue);
      // Process your result here
    } catch (error) {
      console.error("Error submitting form:", error);
    }
  }
</script>

<main>
  <Header></Header>
  <form on:submit|preventDefault={handleSubmit}>
    <input type="number" step="any" bind:value={area} placeholder="Area" />
    <input type="number" step="any" bind:value={rooms} placeholder="Rooms" />
    <input type="text" bind:value={zip} placeholder="ZIP Code" />
    <button type="submit">Submit</button>
  </form>
  <p>{predictedValue}</p>
</main>

<style>
  main {
    text-align: center;
    padding: 2em;
    max-width: 320px;
    margin: 30px auto;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
  }

  form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  input,
  button {
    width: calc(100% - 20px); /* Adjust width to fit inside the form padding */
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box; /* Includes padding and border in the element's total width and height */
  }

  input:focus,
  button:focus {
    border-color: #007bff;
    outline: none; /* Removes the default outline and replaces it with a border color change */
  }

  button {
    background-color: #007bff;
    color: #ffffff;
    font-size: 16px;
    font-weight: bold;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  button:hover {
    background-color: #0056b3;
  }

  p {
    color: #28a745; /* Green color for success messages */
    margin-top: 20px;
  }

  @media (min-width: 640px) {
    main {
      max-width: 400px;
    }
  }

  @media (min-width: 1024px) {
    /* Adjusted for laptop screens */
    main {
      max-width: 600px; /* Wider form on larger screens */
      padding: 3em; /* More padding for better aesthetics */
      margin: 50px auto; /* Increased vertical margin */
    }
  }
</style>
