Title: Cheaper Micropayments with FPS
Date: 2008-08-24 15:24
Author: James
Tags: AWS
Slug: cheaper-micropayments-with-fps

Earlier this month, Amazon [changed the pricing structure][] for
micropayment (aggregate) transactions performed with the Flexible
Payments Service (FPS). FPS no longer charges a per-transaction fee for
payments made from a prepaid or postpaid instrument. Fees are only
changed when money is transferred into an instrument: to fund a prepaid
instrument, or to settle a postpaid instrument.

The new fee structure makes the FPS micropayment instruments much more
attractive. Using the prepaid and postpaid instruments, you can
aggregate many small payments into a few large transactions to minimise
the cost of transaction fees over these payments. Previously, Amazon
took a cut of each individual payment as well as imposing transaction
fees to fund and settle the instruments, but that extra fee burden has
been removed.

  [changed the pricing structure]: http://developer.amazonwebservices.com/connect/thread.jspa?threadID=23558
