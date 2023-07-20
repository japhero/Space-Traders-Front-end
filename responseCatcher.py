def responseCatcher(code):
    """
    raises the correct error based on the error code given.

    Args:
        code int: An error code usually returned by the request when a request is made.
    """

    codes = \
        {
            4000: 'cooldownConflictError',
            4001: 'waypointNoAccessError',
            4100: 'tokenEmptyError',
            4101: 'tokenMissingSubjectError',
            4102: 'tokenInvalidSubjectError',
            4103: 'missingTokenRequestError',
            4104: 'invalidTokenRequestError',
            4105: 'invalidTokenSubjectError',
            4106: 'accountNotExistsError',
            4107: 'agentNotExistsError',
            4108: 'accountHasNoAgentError',
            4109: 'registerAgentExistsError',
            4200: 'navigateInTransitError',
            4201: 'navigateInvalidDestinationError',
            4202: 'navigateOutsideSystemError',
            4203: 'navigateInsufficientFuelError',
            4204: 'navigateSameDestinationError',
            4205: 'shipExtractInvalidWaypointError',
            4206: 'shipExtractPermissionError',
            4207: 'shipJumpNoSystemError',
            4208: 'shipJumpSameSystemError',
            4210: 'shipJumpMissingModuleError',
            4211: 'shipJumpNoValidWaypointError',
            4212: 'shipJumpMissingAntimatterError',
            4214: 'shipInTransitError',
            4215: 'shipMissingSensorArraysError',
            4216: 'purchaseShipCreditsError',
            4217: 'shipCargoExceedsLimitError',
            4218: 'shipCargoMissingError',
            4219: 'shipCargoUnitCountError',
            4220: 'shipSurveyVerificationError',
            4221: 'shipSurveyExpirationError',
            4222: 'shipSurveyWaypointTypeError',
            4223: 'shipSurveyOrbitError',
            4224: 'shipSurveyExhaustedError',
            4225: 'shipRefuelDockedError',
            4226: 'shipRefuelInvalidWaypointError',
            4227: 'shipMissingMountsError',
            4228: 'shipCargoFullError',
            4229: 'shipJumpFromGateToGateError',
            4230: 'waypointChartedError',
            4231: 'shipTransferShipNotFound',
            4232: 'shipTransferAgentConflict',
            4233: 'shipTransferSameShipConflict',
            4234: 'shipTransferLocationConflict',
            4235: 'warpInsideSystemError',
            4236: 'shipNotInOrbitError',
            4237: 'shipInvalidRefineryGoodError',
            4238: 'shipInvalidRefineryTypeError',
            4239: 'shipMissingRefineryError',
            4240: 'shipMissingSurveyorError',
            4500: 'acceptContractNotAuthorizedError',
            4501: 'acceptContractConflictError',
            4502: 'fulfillContractDeliveryError',
            4503: 'contractDeadlineError',
            4504: 'contractFulfilledError',
            4505: 'contractNotAcceptedError',
            4506: 'contractNotAuthorizedError',
            4508: 'shipDeliverTermsError',
            4509: 'shipDeliverFulfilledError',
            4510: 'shipDeliverInvalidLocationError',
            4600: 'marketTradeInsufficientCreditsError',
            4601: 'marketTradeNoPurchaseError',
            4602: 'marketTradeNotSoldError',
            4603: 'marketNotFoundError',
            4604: 'marketTradeUnitLimitError'
        }
    if code in codes:
        raise Exception(codes[code])
    else:
        raise Exception("code not Real")
