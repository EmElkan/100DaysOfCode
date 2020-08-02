import { Component } from '@angular/core';
import posthog from 'posthog-js';
posthog.init("F0fspJp-zJgXilTSooRJQK0Y--xFrAZdUp6Wnk5Gz64", {api_host: "http://127.0.0.1:8000"});

@Component({
  selector: 'ngx-components',
  template: `
    <router-outlet></router-outlet>
  `,
})
export class ExtraComponentsComponent {
}
