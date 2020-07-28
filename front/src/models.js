export class Candidate {
    constructor(word, candidate, translate) {
        this.word = word;
        this.candidate = candidate;
        this.translate = translate;
    }
}

export class Result {
    constructor(result, translate, word, additional) {
        this.result = result;
        this.translate = translate;
        this.word = word;
        this.additional = additional;
    }
}