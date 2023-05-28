/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { MessageType } from './MessageType';

export type Message = {
    content: string;
    type: MessageType;
    timestamp: string;
    conversationContext?: string;
};
