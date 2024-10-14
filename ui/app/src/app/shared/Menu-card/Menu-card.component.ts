import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Menu-card.component.html',
  styleUrls: ['./Menu-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Menu-card]': 'true'
  }
})

export class MenuCardComponent {


}