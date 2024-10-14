import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Chef-card.component.html',
  styleUrls: ['./Chef-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Chef-card]': 'true'
  }
})

export class ChefCardComponent {


}