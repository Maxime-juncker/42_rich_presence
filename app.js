import fetch from 'node-fetch';

const url = "https://api.wit.ai/message?v=20140826&q=";

const UID = "u-s4t2ud-7281dedadbd2dbca3c6332461f9bf60084b5bae10e88a1a17d16093cf23abb5f"
const SECRET = "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" 

// curl -X POST --data "grant_type=client_credentials&client_id=MY_AWESOME_UID&client_secret=MY_AWESOME_SECRET" https://api.intra.42.fr/oauth/token

var response = await fetch('https://api.intra.42.fr/oauth/token', {
	method: 'POST',
	headers: {
		'Content-Type': 'application/x-www-form-urlencoded',
	},
	body: new URLSearchParams({
		grant_type: 'client_credentials',
		client_id: UID,
		client_secret: SECRET,
	}),
});

var data = await response.json();
console.log(data);


const code = data["access_token"]
console.log(code);

response = await fetch('https://api.intra.42.fr/v2/users?&filter[login]=mjuncker', {
	method: 'GET',
	headers: {
		'Authorization': 'Bearer ' + code,
	},
});


data = await response.json();
console.log(data);



import RPC from 'discord-rpc';

const clientId = '1383806236763623496';

RPC.register(clientId);

const rpc = new RPC.Client({ transport: 'ipc' });

rpc.on('ready', () => {
  rpc.setActivity({
    details: 'test detail',
    state: 'test',
    startTimestamp: new Date(),
    largeImageKey: 'your_large_image_key', // must match uploaded asset name
    largeImageText: 'app',
    // smallImageKey: 'your_small_image_key', // optional
    // smallImageText: 'Small icon text',
    // buttons: [
    //   { label: 'My Website', url: 'https://example.com' },
    //   { label: 'GitHub', url: 'https://github.com/yourname' }
    // ]
  });

  console.log('Rich Presence set!');
});

rpc.login({ clientId }).catch(console.error);
