<script>
    let username = '';
    let password = '';
    let email = '';

    async function register() {
        const response = await fetch('http://37.26.14.48:8000/auth/reg/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password, email }),
        });

        if (!response.ok) {
            const message = `An error has occured: ${response.status}`;
            throw new Error(message);
        }

        const result = await response.json();
        console.log(result);
        alert(`User ${result.username} registered successfully!`);
    }
</script>

<form on:submit|preventDefault={register}>
    <input type="text" bind:value={username} placeholder="Username">
    <input type="password" bind:value={password} placeholder="Password">
    <input type="email" bind:value={email} placeholder="Email (optional)">
    <button type="submit">Register</button>
</form>

<style>
    form {
        display: flex;
        flex-direction: column;
        width: 200px;
    }
    input, button {
        margin-bottom: 1rem;
    }
</style>