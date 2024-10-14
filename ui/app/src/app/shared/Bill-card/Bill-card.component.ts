import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Bill-card.component.html',
  styleUrls: ['./Bill-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Bill-card]': 'true'
  }
})

export class BillCardComponent {


}