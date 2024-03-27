<script>
  import { onMount } from "svelte";

  let area = "";
  let rooms = "";
  let zip = "";
  let predictedValue = "";

  async function handleSubmit(event) {
    // Prevent the browser from submitting the form traditionally
    event.preventDefault();

    // The URL to your Flask endpoint
    //const url = "http://127.0.0.1:5000/predict";
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
      predictedValue = result;
      console.log("Prediction Result:", result);
      // Process your result here
    } catch (error) {
      console.error("Error submitting form:", error);
    }
  }
</script>

<main>
  <h1>RentEstimator 3</h1>
  <form on:submit|preventDefault={handleSubmit}>
    <input type="number" bind:value={area} placeholder="Area" />
    <input type="number" bind:value={rooms} placeholder="Rooms" />
    <input type="text" bind:value={zip} placeholder="ZIP Code" />
    <button type="submit">Submit</button>
  </form>
  <p>{predictedValue}</p>
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  input,
  button {
    margin: 0.5em 0; /* Spacing between inputs and button */
    padding: 0.5em;
  }

  input {
    width: 90%; /* Make input fields wider */
  }

  button {
    cursor: pointer;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
