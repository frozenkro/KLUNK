/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { Message } from './Message';

export type Interaction = {
    proompt: Message;
    response?: Message;
    conversationContext?: string;
};
