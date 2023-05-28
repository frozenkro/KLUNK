/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Interaction } from '../models/Interaction';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class ChatService {

    /**
     * Proompt
     * @param requestBody 
     * @returns any Successful Response
     * @throws ApiError
     */
    public static proomptChatPost(
requestBody: Interaction,
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/chat/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
