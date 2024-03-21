<script>
	import welcome_fallback from '$lib/images/svelte-welcome.png';
	import bannerLight from '$lib/images/AmigosHubLight.png';
</script>

<svelte:head>
	<title>Homepage</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<h1>
		<span class="welcome">
			<picture>
				<source srcset={bannerLight} type="image/png" />
				<img src={welcome_fallback} alt="Welcome" />
			</picture>
		</span>

		<strong class="orange">Добро пожаловать!</strong>
	</h1>

	<h2>
		May the <strong>Gamble</strong> be with you!
	</h2>


	<p>Приветствуем на форуме!

		Добро пожаловать в наше сообщество! Здесь вы найдете множество интересных обсуждений, полезную информацию и возможность обмена опытом.
		
		Участвуйте активно, задавайте вопросы, делитесь своими знаниями и идеями. Наша цель - создать дружественное и поддерживающее сообщество для обмена полезной информацией.
		
		Благодарим вас за участие и желаем приятного времяпровождения на нашем форуме! <a>Войдите</a> или <sa>зарегистрируйтесь</sa>, чтобы начать общение.
		
		</p>

		<table>
			<tr>
			  <th>Название</th>
			  <th>Описание</th>
			  <th>Доска</th>
			</tr>
			<tr>
			  <td>Аноним</td>
			  <td>Анонимная доска ( регистрация не требуется )</td>
			  <td><a href="/anon/">/anon/</a></td>
			</tr>
			<tr>
			  <td>Политика</td>
			  <td>Francisco Chang</td>
			  <td><a href="/p/">/p/</a></td>
			</tr>
			<tr>
			  <td>Техника и IT</td>
			  <td>Roland Mendel</td>
			  <td><a href="/it/">/it/</a></td>
			</tr>
			<tr>
			  <td>Игры</td>
			  <td>Helen Bennett</td>
			  <td><a href="/gm/">/gm/</a></td>
			</tr>
		  </table>
</section>

<style>

	.orange{
		color: #ff6600;
	}
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
	table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
  margin-top: 10em;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
