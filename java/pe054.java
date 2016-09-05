// run with: java pe054 < ../pe054.txt

import java.util.Arrays;
import java.util.Scanner;

public class pe054 {
	public static boolean player1Wins(Hand p1, Hand p2){
		if ((p1.score).compareTo(p2.score) > 0) {
			return true;
		} else if ((p1.score).compareTo(p2.score) < 0) {
			return false;
		} else {
			//System.out.println("d");
			Card p1c = p1.hand[4], p2c = p2.hand[4];
			int i = 4, j = 4;
			while (p1c.compareTo(p2c) == 0) {
				//System.out.println("hey");
				while ((p1.hand[i]).compareTo(p1c) == 0) {
					i--;
				}
				p1c = p1.hand[i];
				while ((p2.hand[j]).compareTo(p2c) == 0) {
					j--;
				}
				p2c = p2.hand[j];
			}
			//System.out.println("Draw! Player 1: " + p1c.number + " Player 2: " + p2c.number);
			return p1c.compareTo(p2c) > 0;
		}
	}
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int count = 0;
		while (s.hasNextLine()) {
			String temp = s.nextLine();
			String[] temp2 = temp.split("\\s");
			Hand player1 = new Hand(Arrays.copyOfRange(temp2, 0, 5));
			Hand player2 = new Hand(Arrays.copyOfRange(temp2, 5, 10));
			boolean c = player1Wins(player1, player2);
			//System.out.printf("Player 1: %s\nPlayer 2: %s\nPlayer 1 score: %s\nPlayer 2 score: %s\nPlayer 1 wins: %s\n\n", 
					//player1, player2, player1.score, player2.score, c);
			count += c ? 1 : 0;
		}
		System.out.println(count);
	}
}

public class Hand {
	public Card[] hand = new Card[5];
	public Score score;
	
	public Hand(String[] hand) {
		for (int i = 0; i < 5; i++) {
			this.hand[i] = new Card(hand[i]);
		}
		Arrays.sort(this.hand);
		// run functions in order
		if (royalFlush(this)) return;
		if (straightFlush(this)) return;
		if (fourOfAKind(this)) return;
		if (fullHouse(this)) return;
		if (flush(this)) return;
		if (straight(this)) return;
		if (threeOfAKind(this)) return;
		if (twoPairs(this)) return;
		if (onePair(this)) return;
		if (highCard(this)) return;
		
	}
	@Override
	public String toString() {
		String result = "";
		for (int i = 0; i < 5; i++) {
			result += this.hand[i].number + "" + this.hand[i].suit + " ";
		}
		return result;
	}
	////////////////////////////////////////
	private static boolean royalFlush(Hand cards) {
		int n = 10;
		char s = cards.hand[0].suit;
		for (Card c : cards.hand) {
			if (c.number != n || c.suit != s) {
				return false;
			}
			n++;
		}
		cards.score = new Score(10, 14);
		return true;
	}
	private static boolean straightFlush(Hand cards) {
		int n = cards.hand[0].number;
		char s = cards.hand[0].suit;
		for (Card c : cards.hand) {
			if (c.number != n || c.suit != s) {
				return false;
			}
			n++;
		}
		cards.score = new Score(9, n-1);
		return true;
	}
	private static boolean fourOfAKind(Hand cards) {
		int n = cards.hand[0].number;
		int i = 0;
		int distinct = 1;
		for (Card c : cards.hand) {
			if (c.number != n) {
				if (i != 1 || i != 4) { // change must occur between either 0 and 1 or 3 and 4
					return false;
				}
				n = c.number;
				distinct++;
			}
			if (distinct > 2) {
				return false;
			}
			i++;
		}
		cards.score = new Score(8, cards.hand[2].number);
		return true;
	}
	private static boolean fullHouse(Hand cards) {
		int n = cards.hand[0].number;
		int distinct = 1;
		for (Card c : cards.hand) {
			if (c.number != n) {
				n = c.number;
				distinct++;
			}
			if (distinct > 2) {
				return false;
			}
		}
		cards.score = new Score(7, cards.hand[2].number);
		return true;
	}
	private static boolean flush(Hand cards) {
		char s = cards.hand[0].suit;
		for (Card c : cards.hand) {
			if (c.suit != s) {
				return false;
			}
		}
		cards.score = new Score(6, cards.hand[4].number);
		return true;
	}
	private static boolean straight(Hand cards) {
		int n = cards.hand[0].number;
		for (Card c : cards.hand) {
			if (c.number != n) {
				return false;
			}
			n++;
		}
		cards.score = new Score(5, cards.hand[4].number);
		return true;
	}
	private static boolean threeOfAKind(Hand cards) {
		for (int i = 2; i < 5; i++) {
			if (cards.hand[i].number == cards.hand[i-1].number && cards.hand[i-1].number == cards.hand[i-2].number) {
				cards.score = new Score(4, cards.hand[i].number);
				return true;
			}
		}
		return false;
	}
	private static boolean twoPairs(Hand cards) {
		int pairs = 0;
		int a = 0;
		for (int i = 1; i < 5; i++) {
			if (cards.hand[i].number == cards.hand[i-1].number) {
				pairs++;
				a = cards.hand[i].number > a ? cards.hand[i].number : a;
				if (pairs == 2) {
					cards.score = new Score(3, a);
					return true;
				}
			}
		}
		return false;
	}
	private static boolean onePair(Hand cards) {
		for (int i = 1; i < 5; i++) {
			if (cards.hand[i].number == cards.hand[i-1].number) {
				cards.score = new Score(2, cards.hand[i].number);
				return true;
			}
		}
		return false;
	}
	private static boolean highCard(Hand cards) {
		cards.score = new Score(1, cards.hand[4].number);
		return true;
	}
}


// defines a lexicographically compared tuple for score keeping
public class Score implements Comparable<Score> {
	private int handRank, highestCard;
	public Score(int handRank, int highestCard) {
		this.handRank = handRank;
		this.highestCard = highestCard;
	}
	@Override
	public int compareTo(Score secondHand) {
		return this.handRank == secondHand.handRank ? 
				this.highestCard - secondHand.highestCard 
				: 
				this.handRank - secondHand.handRank;
	}
	@Override
	public String toString() {
		return "hand rank: " + handRank + "\thighest card: " + highestCard;
	}
}

//defines a lexicographically compared tuple
public class Card implements Comparable<Card> {
	public int number;
	public char suit;
	public Card(String card) {
		this.number = extractNumber(card.charAt(0));
		this.suit = card.charAt(1);
	}
	public static int extractNumber(char num) {
		if (num <= '9') {
			return num - (int) '0';
		} else if (num == 'T') {
			return 10;
		} else if (num == 'J') {
			return 11;
		} else if (num == 'Q') {
			return 12;
		} else if (num == 'K') {
			return 13;
		} else {
			return 14; // (num == 'A')
		}
	}
	@Override
	public int compareTo(Card card) {
		return this.number - card.number;
	}
}