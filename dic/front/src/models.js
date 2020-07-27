export class Candidate {
    constructor(word, candidate, translate) {
        this.word = word;
        this.candidate = candidate;
        this.translate = translate;
    }
}

export class Result {
    constructor(result, translate, attr, additional) {
        this.result = result;
        this.translate = translate;
        this.attr = attr;
        this.additional = additional;
    }
}