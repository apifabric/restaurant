import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './RestaurantTable-card.component.html',
  styleUrls: ['./RestaurantTable-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.RestaurantTable-card]': 'true'
  }
})

export class RestaurantTableCardComponent {


}