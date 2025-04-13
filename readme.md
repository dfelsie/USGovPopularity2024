Based on work by Lakshya Jain, I wrote some code based on data from wikipedia and MorningConsult to calculate the approvals of governors compared to polling data and their parties' margin of victory in the 2024 presidential election.
Here are the results:

# Governors Compared to Their Party's Electoral Margin

| State          | Governor               | Party      | Approval Rating | Party Margin | vs Expected | Number of Polls |
| -------------- | ---------------------- | ---------- | --------------- | ------------ | ----------- | --------------- |
| Vermont        | Phil Scott             | Republican | 62.5%           | -33.3%       | +65.1%      | 4               |
| Kentucky       | Andy Beshear           | Democratic | 52.3%           | -30.5%       | +54.2%      | 2               |
| New Hampshire  | Chris Sununu           | Republican | 59.2%           | -2.7%        | +29.2%      | 11              |
| Delaware       | John Carney            | Democratic | 68.0%           | +14.7%       | +28.3%      | 1\*             |
| Pennsylvania   | Josh Shapiro           | Democratic | 52.2%           | -1.7%        | +27.6%      | 8               |
| Kansas         | Laura Kelly            | Democratic | 39.2%           | -16.1%       | +25.7%      | 1\*             |
| Georgia        | Brian Kemp             | Republican | 60.1%           | +2.4%        | +22.5%      | 2               |
| Virginia       | Glenn Youngkin         | Republican | 52.9%           | -5.8%        | +21.4%      | 13              |
| Nevada         | Joe Lombardo           | Republican | 47.9%           | +3.1%        | +18.6%      | 3               |
| North Carolina | Roy Cooper             | Democratic | 48.1%           | -3.2%        | +14.8%      | 15              |
| Michigan       | Gretchen Whitmer       | Democratic | 52.0%           | -1.4%        | +14.5%      | 9               |
| Connecticut    | Ned Lamont             | Democratic | 60.0%           | +14.5%       | +12.5%      | 1\*             |
| Utah           | Spencer Cox            | Republican | 62.0%           | +21.6%       | +11.7%      | 3               |
| Wisconsin      | Tony Evers             | Democratic | 50.7%           | -0.9%        | +10.7%      | 4               |
| Maine          | Janet Mills            | Democratic | 54.7%           | +6.9%        | +9.4%       | 6               |
| Arizona        | Katie Hobbs            | Democratic | 42.4%           | -0.5%        | +6.7%       | 3               |
| Massachusetts  | Maura Healey           | Democratic | 56.3%           | +25.2%       | +4.8%       | 3               |
| New Jersey     | Phil Murphy            | Democratic | 48.5%           | +5.9%        | +3.9%       | 8               |
| Maryland       | Wes Moore              | Democratic | 56.1%           | +28.5%       | +1.8%       | 3               |
| Colorado       | Jared Polis            | Democratic | 45.2%           | +11.3%       | +1.2%       | 2               |
| South Carolina | Henry McMaster         | Republican | 49.6%           | +17.9%       | -1.6%       | 5               |
| New Mexico     | Michelle Lujan Grisham | Democratic | 47.0%           | +6.0%        | -2.0%       | 1\*             |
| Florida        | Ron DeSantis           | Republican | 53.5%           | +13.1%       | -2.7%       | 4               |
| New York       | Kathy Hochul           | Democratic | 49.0%           | +12.6%       | -5.9%       | 10              |
| Ohio           | Mike DeWine            | Republican | 37.7%           | +11.2%       | -6.3%       | 2               |
| Indiana        | Eric Holcomb           | Republican | 37.0%           | +19.0%       | -7.0%       | 1\*             |
| Illinois       | J.B. Pritzker          | Democratic | 44.3%           | +10.9%       | -7.6%       | 2               |
| Montana        | Greg Gianforte         | Republican | 36.7%           | +19.9%       | -9.4%       | 1\*             |
| Texas          | Greg Abbott            | Republican | 46.8%           | +13.7%       | -9.7%       | 9               |
| California     | Gavin Newsom           | Democratic | 50.5%           | +20.1%       | -11.4%      | 11              |
| North Dakota   | Doug Burgum            | Republican | 49.6%           | +35.4%       | -12.1%      | 2               |
| Iowa           | Kim Reynolds           | Republican | 43.7%           | +13.2%       | -12.5%      | 4               |
| Missouri       | Mike Parson            | Republican | 44.5%           | +18.4%       | -12.9%      | 2               |
| Tennessee      | Bill Lee               | Republican | 46.9%           | +29.7%       | -15.5%      | 4               |
| Louisiana      | John Bel Edwards       | Republican | 44.3%           | +22.0%       | -17.7%      | 3               |
| West Virginia  | Jim Justice            | Republican | 51.1%           | +41.9%       | -18.8%      | 2               |
| Nebraska       | Jim Pillen             | Republican | 25.6%           | +19.5%       | -20.3%      | 1\*             |
| Arkansas       | Sarah Huckabee Sanders | Republican | 44.2%           | +30.6%       | -21.3%      | 2               |
| South Dakota   | Kristi Noem            | Republican | 43.2%           | +29.2%       | -22.5%      | 1\*             |
| Mississippi    | Tate Reeves            | Republican | 45.7%           | +24.9%       | -25.2%      | 3               |
| Wyoming        | Mark Gordon            | Republican | 34.8%           | +45.8%       | -27.3%      | 1\*             |
| Oklahoma       | Kevin Stitt            | Republican | 41.5%           | +34.3%       | -29.2%      | 2               |
| Idaho          | Brad Little            | Republican | 28.1%           | +36.5%       | -37.1%      | 1\*             |


A few notes:

A few govs had no polls from morningconsult at all, so they have been excluded: that's why the table doesn't have 50 rows.
Some of these governors have very few associated polls, so take their numbers with a grain of salt. Sorry Brad Little: you're (probably) not really this unpopular.
Governors are pretty popular! I think this methodology has some value, but it probably overstates the how skilled some governors are, if they're in states that voted one way for president, but the opposite for governor. This is how Scott and Beshear can have such incredible margins.
