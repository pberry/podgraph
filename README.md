# podgraph
Wherein we map the connections between podcasts.

## The Idea
You listen to podcasts. Podcasts have hosts and guests. Both hosts and guests appear on other podcasts you may not know about. Wouldn't it be great to a) visualize a graph of podcasts starting with one you know and love and b) be able to find other podcasts based on the connections of hosts and guests?

## Implementation Challenges

### Data
Data for this is currently unstructured, in that it only exists in episode descriptions or titles, if at all. There is no _current_ standard for including this information in a structured manner ([FOAF](http://www.foaf-project.org/) or maybe a [JSON Feed extension](https://jsonfeed.org/version/1#extensions) in the future?), so even if podcast producers wanted to incude this data, they couldn't.

Collecting the data today is completely manual. Automating this would be preferable, as would finding a way to incorporate the data into a standard format that would be widely used. Relay.fm has this data for their own shows, for example [Serenity Caldwell appearances](https://www.relay.fm/people/serenitycaldwell), but this doesn't include off-network appearances.

* Networks
	* [5by5](http://5by5.tv/)
	* [Panoply](http://panoply.fm/) 
	* [The Incomparable](https://www.theincomparable.com/) (show _and_ network)
	* [Relay.fm](https://www.relay.fm/)
* Podcasts
	* [The Talk Show](https://daringfireball.net/thetalkshow/) (one host)
	* [Unattended Consequences](https://unattendedconsequences.simplecast.fm/) (two hosts)
	* 
* Host(s)
	* [John Gruber](https://twitter.com/gruber) (hosts one show)
	* [Jason Snell](https://twitter.com/jsnell) (hosts many shows, guests on others)
* Guest(s)
	* [MG Siegler](https://twitter.com/mgsiegler)
	* [Serenity Caldwell](http://manyhats.tumblr.com/about)

## Visualization
If one had a graph data set of the connections between podcasts, hosts, and guests you could create a visual representation of the podcast ecosystem.

## Recommendations
Ideally one would be able to start at a podcast or person, either as a host or guest, and then find other podcasts they would be interested in based on the connections of the people. For instance, say you like [Unattended Consequences](https://unattendedconsequences.simplecast.fm/) which is hosted by [Max Tempkin](https://twitter.com/MaxTemkin) and [Patrick Rothfuss](http://www.patrickrothfuss.com/). They don't have a lot of guests, but they do show up on other podcasts as guests. There are all kinds of reasons that you may not know about those connections and this system would allow you to discover these other shows.
