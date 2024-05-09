// This sample uses Atlassian Forge
// https://developer.atlassian.com/platform/forge/
import api, { route } from "@forge/api";

const response = await api.asUser().requestJira(route`/rest/api/3/issue/{issueIdOrKey}`, {
  headers: {
    'Accept': 'application/json'
  }
});

console.log(`Response: ${response.status} ${response.statusText}`);
console.log(await response.json());