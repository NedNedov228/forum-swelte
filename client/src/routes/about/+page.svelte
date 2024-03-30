<script>
	
</script>

<svelte:head>
	<title>About</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	

	<h1>О нас</h1>
	
	<p>
		Наш форум - это онлайн-сообщество, где люди со всего мира собираются для обмена идеями, знаниями и опытом. Мы создали это место для всех, кто ищет вдохновение, информацию или просто хочет общаться с единомышленниками. На нашем форуме вы найдете разнообразные темы для обсуждения, дружелюбную атмосферу и возможность расширить свой круг общения. Присоединяйтесь к нашему сообществу и станьте частью нашего вдохновляющего и интерактивного онлайн-мира!
	</p>
</section>

<style>
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
</style>
