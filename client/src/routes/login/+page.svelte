<!-- <script>
    let username = '';
    let password = '';
    let accessToken = '';
  
    async function login() {
      const response = await fetch('http://37.26.14.48:8000/auth/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });
  
      if (response.ok) {
        const data = await response.json();
        accessToken = data.access_token;
        alert('Login successful');
      } else {
        alert('Login failed');
      }
    }
  </script>
  
  <div>
    <form on:submit|preventDefault={login}>
      <h2>Login</h2>
      <input type="text" placeholder="Username" bind:value={username} />
      <input type="password" placeholder="Password" bind:value={password} />
      <button type="submit">Login</button>
    </form>
  </div>
  
  {#if accessToken}
  <p>Logged in with token: {accessToken}</p>
  {/if} -->


  <!-- Login.svelte -->
<script lang="js">
    import { onMount } from 'svelte';

    let username = '';
    let password = '';
    let errorMessage = '';
  
    async function login() {
      try {
        const response = await fetch('http://localhost:8000/token', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
          body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`,
        });
  
        const data = await response.json();
  
        if (!response.ok) {
          throw new Error(data.detail || 'Failed to login');
        }
  
        localStorage.setItem('token', data.access_token);
        // Перенаправить пользователя куда-либо после успешного входа, если требуется
        // navigate('/home'); // Пример использования svelte-routing для перенаправления
  
        console.log('Login successful:', data);
      } catch (error) {
        errorMessage = "errormsg!!";
      }
    }
  
    // Пример автоматического перенаправления, если пользователь уже вошел
    onMount(() => {
      const token = localStorage.getItem('token');
      if (token) {
        // navigate('/home'); // Или ваша логика проверки токена
      }
    });
  </script>
  
  <style>
    .error {
      color: red;
    }
  </style>
  
  <form on:submit|preventDefault={login}>
    <div>
      <label for="username">Username:</label>
      <input id="username" type="text" bind:value={username} required>
    </div>
    <div>
      <label for="password">Password:</label>
      <input id="password" type="password" bind:value={password} required>
    </div>
    {#if errorMessage}
      <p class="error">{errorMessage}</p>
    {/if}
    <button type="submit">Login</button>
  </form>