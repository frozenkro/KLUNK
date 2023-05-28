import App from './App.svelte';
import { OpenAPI } from './BUNK/core/OpenAPI';

OpenAPI.BASE = 'http://localhost:8000';

const app = new App({
	target: document.body
});

export default app;