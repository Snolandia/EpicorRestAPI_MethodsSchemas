import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CashReceiptAdjustmentSvc
# Description: Cash Receipt Adjustment BO
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CashReceiptAdjustments(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CashReceiptAdjustments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashReceiptAdjustments
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CashReceiptAdjustments",headers=creds) as resp:
           return await resp.json()

async def post_CashReceiptAdjustments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashReceiptAdjustments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CashReceiptAdjustments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CashReceiptAdjustments_Company_GroupID_HeadNum(Company, GroupID, HeadNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashReceiptAdjustment item
   Description: Calls GetByID to retrieve the CashReceiptAdjustment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashReceiptAdjustment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CashReceiptAdjustments(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CashReceiptAdjustments_Company_GroupID_HeadNum(Company, GroupID, HeadNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CashReceiptAdjustment for the service
   Description: Calls UpdateExt to update CashReceiptAdjustment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashReceiptAdjustment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CashReceiptAdjustments(" + Company + "," + GroupID + "," + HeadNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CashReceiptAdjustments_Company_GroupID_HeadNum(Company, GroupID, HeadNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CashReceiptAdjustment item
   Description: Call UpdateExt to delete CashReceiptAdjustment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashReceiptAdjustment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CashReceiptAdjustments(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CashReceiptAdjustments_Company_GroupID_HeadNum_CashDtls(Company, GroupID, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CashDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CashReceiptAdjustments(" + Company + "," + GroupID + "," + HeadNum + ")/CashDtls",headers=creds) as resp:
           return await resp.json()

async def get_CashReceiptAdjustments_Company_GroupID_HeadNum_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company, GroupID, HeadNum, InvoiceNum, InvoiceRef, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashDtl item
   Description: Calls GetByID to retrieve the CashDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CashReceiptAdjustments(" + Company + "," + GroupID + "," + HeadNum + ")/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")",headers=creds) as resp:
           return await resp.json()

async def get_CashDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CashDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CashDtls",headers=creds) as resp:
           return await resp.json()

async def post_CashDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CashDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company, GroupID, HeadNum, InvoiceNum, InvoiceRef, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashDtl item
   Description: Calls GetByID to retrieve the CashDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company, GroupID, HeadNum, InvoiceNum, InvoiceRef, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CashDtl for the service
   Description: Calls UpdateExt to update CashDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CashDtls_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company, GroupID, HeadNum, InvoiceNum, InvoiceRef, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CashDtl item
   Description: Call UpdateExt to delete CashDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CashDtls(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")",headers=creds) as resp:
           return await resp.json()

async def get_CDTaxDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CDTaxDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CDTaxDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CDTaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CDTaxDtls",headers=creds) as resp:
           return await resp.json()

async def post_CDTaxDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CDTaxDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CDTaxDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CDTaxDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CDTaxDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CDTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company, SourceModule, HeadNum, APTranNo, InvoiceNum, InvoiceRef, BankAcctID, TranNum, Voided, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CDTaxDtl item
   Description: Calls GetByID to retrieve the CDTaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CDTaxDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CDTaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CDTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CDTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company, SourceModule, HeadNum, APTranNo, InvoiceNum, InvoiceRef, BankAcctID, TranNum, Voided, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CDTaxDtl for the service
   Description: Calls UpdateExt to update CDTaxDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CDTaxDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CDTaxDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CDTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CDTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company, SourceModule, HeadNum, APTranNo, InvoiceNum, InvoiceRef, BankAcctID, TranNum, Voided, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CDTaxDtl item
   Description: Call UpdateExt to delete CDTaxDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CDTaxDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/CDTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/LegalNumGenOpts",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCashHead, whereClauseCashDtl, whereClauseCDTaxDtl, whereClauseLegalNumGenOpts, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCashHead=" + whereClauseCashHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCashDtl=" + whereClauseCashDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCDTaxDtl=" + whereClauseCDTaxDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, headNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "groupID=" + groupID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "headNum=" + headNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AdjustCashReceipt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AdjustCashReceipt
   Description: Adjust Cash Receipt
   OperationID: AdjustCashReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AdjustCashReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AdjustCashReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CashRecGetInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CashRecGetInvoices
   Description: This procedure returns both open and invoices to adjust within Cash Receipt Adjustment Entry
   OperationID: CashRecGetInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CashRecGetInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CashRecGetInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPendingToPostAdjustments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPendingToPostAdjustments
   Description: Return ListMessage of Cash Receipt Adjustments pending to post and Invoice Unposted Balance
   OperationID: GetPendingToPostAdjustments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPendingToPostAdjustments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPendingToPostAdjustments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreAdjustCashReceipt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreAdjustCashReceipt
   Description: Check if Prompting for LegalNumbers
   OperationID: PreAdjustCashReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreAdjustCashReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreAdjustCashReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAdjustmentCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAdjustmentCustID
   OperationID: ChangeAdjustmentCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAdjustmentCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAdjustmentCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTranDocTypeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTranDocTypeID
   Description: Sets default values when the TranDocTypeID changes
   OperationID: OnChangeTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalcInvBal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalcInvBal
   Description: Calculate Invoice Balance.
   OperationID: CalcInvBal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcInvBal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcInvBal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalcDiscount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalcDiscount
   Description: Public Method - calculate Discount.
   OperationID: CalcDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalcAllocAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalcAllocAmount
   Description: Calculate AllocAmount.
   OperationID: CalcAllocAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcAllocAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcAllocAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AutoSelectItem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoSelectItem
   Description: Auto Select Invoices.
   OperationID: AutoSelectItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoSelectItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoSelectItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectInvoiceAlloc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectInvoiceAlloc
   Description: Select Invoices to Allocate.
   OperationID: SelectInvoiceAlloc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectInvoiceAlloc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectInvoiceAlloc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalcSelectedInvcTotal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalcSelectedInvcTotal
   Description: Calculate Unapplied Amount.
   OperationID: CalcSelectedInvcTotal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcSelectedInvcTotal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcSelectedInvcTotal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetDisplayBalance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetDisplayBalance
   Description: Calculate total values: calcTotalDN, calcTotalDNbase.
   OperationID: SetDisplayBalance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetDisplayBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetDisplayBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ForceTakeDiscount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ForceTakeDiscount
   Description: ForceTakeDiscount - actions on Force Discount clicked.
   OperationID: ForceTakeDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ForceTakeDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ForceTakeDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingAllocAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingAllocAmount
   Description: Actions on AllocAmount ColumnChanging.
   OperationID: OnChangingAllocAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAllocAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAllocAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingCashApplied(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingCashApplied
   Description: Actions on CashApplied ColumnChanging.
   OperationID: OnChangingCashApplied
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingCashApplied_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingCashApplied_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingDiscount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingDiscount
   Description: Actions on Discount ColumnChanging.
   OperationID: OnChangingDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingInvcSelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingInvcSelected
   Description: Actions on InvcSelected ColumnChanging.
   OperationID: OnChangingInvcSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingInvcSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingInvcSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedInvcSelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedInvcSelected
   Description: Actions on InvcSelected ColumnChanged.
   OperationID: OnChangedInvcSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedInvcSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedInvcSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedAllocAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedAllocAmount
   Description: Actions on AllocAmount ColumnChanged.
   OperationID: OnChangedAllocAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedAllocAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedAllocAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedCashApplied(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedCashApplied
   Description: Actions on CashApplied ColumnChanged.
   OperationID: OnChangedCashApplied
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedCashApplied_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedCashApplied_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedDiscount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedDiscount
   Description: Actions on CashApplied ColumnChanged.
   OperationID: OnChangedDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildCustAddress(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildCustAddress
   OperationID: BuildCustAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildCustAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildCustAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCDTaxDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCDTaxDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCDTaxDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCDTaxDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCDTaxDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashReceiptAdjustmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CDTaxDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CDTaxDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Erp_Tablesets_CDTaxDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this tax detail.  This is assigned by the system.
Values can be; AR, AP.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.APTranNo:int = obj["APTranNo"]
      """  Integer assigned by the system copied from APTran.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice. Manually entered if the currency is the base currency.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. Manually entered if the currency is the base currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency. Manually entered.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Reverse Charge.  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution Date  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Tax Rate Date  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.Rpt1DefTaxableAmt:int = obj["Rpt1DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxableAmt:int = obj["Rpt2DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxableAmt:int = obj["Rpt3DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.DefTaxAmt:int = obj["DefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.DocDefTaxAmt:int = obj["DocDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.Rpt1DefTaxAmt:int = obj["Rpt1DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxAmt:int = obj["Rpt2DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxAmt:int = obj["Rpt3DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Relates record to a BankAcct.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID of the Transaction.  """  
      self.DedTaxAmt:int = obj["DedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.DocDedTaxAmt:int = obj["DocDedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.Rpt1DedTaxAmt:int = obj["Rpt1DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DedTaxAmt:int = obj["Rpt2DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DedTaxAmt:int = obj["Rpt3DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.FixedAmount:int = obj["FixedAmount"]
      """  Fixed Tax Amount  """  
      self.DocFixedAmount:int = obj["DocFixedAmount"]
      """  Document Fixed Tax Amount  """  
      self.Rpt1FixedAmount:int = obj["Rpt1FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2FixedAmount:int = obj["Rpt2FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3FixedAmount:int = obj["Rpt3FixedAmount"]
      """  Reporting currency value of this field  """  
      self.DiscTaxAdj:int = obj["DiscTaxAdj"]
      """  Discount Tax Adjustment  """  
      self.DocDiscTaxAdj:int = obj["DocDiscTaxAdj"]
      """  Discount Tax Adjustment in foreign currency.  """  
      self.Rpt1DiscTaxAdj:int = obj["Rpt1DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxAdj:int = obj["Rpt2DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxAdj:int = obj["Rpt3DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.DiscTaxableAdj:int = obj["DiscTaxableAdj"]
      """  Discount Taxable Adjustment  """  
      self.DocDiscTaxableAdj:int = obj["DocDiscTaxableAdj"]
      """  Discount Taxable Adjustment in foreign currency.  """  
      self.Rpt1DiscTaxableAdj:int = obj["Rpt1DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxableAdj:int = obj["Rpt2DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxableAdj:int = obj["Rpt3DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates if transaction was voided.  The rest of the unique key will contain the original transaction values (like APTran)  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DiscTaxAdjVar:int = obj["DiscTaxAdjVar"]
      """  Discount Tax Adjustment Variance  """  
      self.DocDiscTaxAdjVar:int = obj["DocDiscTaxAdjVar"]
      """  Discount Tax Adjustment Variance  """  
      self.Rpt1DiscTaxAdjVar:int = obj["Rpt1DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxAdjVar:int = obj["Rpt2DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxAdjVar:int = obj["Rpt3DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGOrigTaxableAmt:int = obj["AGOrigTaxableAmt"]
      """  AGOrigTaxableAmt  """  
      self.GainLoss:int = obj["GainLoss"]
      """  GainLoss  """  
      self.DocGainLoss:int = obj["DocGainLoss"]
      """  DocGainLoss  """  
      self.Rpt1GainLoss:int = obj["Rpt1GainLoss"]
      """  Rpt1GainLoss  """  
      self.Rpt2GainLoss:int = obj["Rpt2GainLoss"]
      """  Rpt2GainLoss  """  
      self.Rpt3GainLoss:int = obj["Rpt3GainLoss"]
      """  Rpt3GainLoss  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  APInvoiceNum  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.GroupID:str = obj["GroupID"]
      """  Group ID - used to link to Cash Head  """  
      self.CTDescription:str = obj["CTDescription"]
      self.DisableManual:bool = obj["DisableManual"]
      """  Flag to indicate if Manual checkbox should be Read Only  """  
      self.EnableTax:bool = obj["EnableTax"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "Group" to which is transaction is assigned. This is not user maintainable. It is duplicated from the corresponding CashHead record.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The foreign key that relates this detail record to a CashHead record. Duplicated from CashHead.HeadNum when record is created. Not applicable to user interface.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.TranType:str = obj["TranType"]
      """   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction cannot be maintained; it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted to the General Ledger Module.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date. Duplicated from the CashBatc.TranDate. Not user maintainable. This is refreshed as part of the post process.  """  
      self.CheckRef:str = obj["CheckRef"]
      """   The customer's Check number of the receipt transaction. Duplicated from CashHead.CheckRef. This is a mandatory field used only for Cash Receipt type of translations.  Primarily used as a reference. The only validation is that it can't be blank.
This is used when TranType = PrePay, MisPay or PayInv.  """  
      self.TranAmt:int = obj["TranAmt"]
      """   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.
For records based in Debit Note applied  it carries a negative sign.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction, it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  """  
      self.Discount:int = obj["Discount"]
      """   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  """  
      self.Comment:str = obj["Comment"]
      """  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adjust".  """  
      self.Reference:str = obj["Reference"]
      """  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this CashDtl, only differs from cashead when the invoice is locked.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.DebitNote:bool = obj["DebitNote"]
      """  The internally set flag to indicate if this detail line of the Cash payment is Debit Note type.  """  
      self.DNComments:str = obj["DNComments"]
      """  Debit Note Detail Comments.  """  
      self.DNAmount:int = obj["DNAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DocDnAmount:int = obj["DocDnAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DNCustNbr:str = obj["DNCustNbr"]
      """  The Debit Note Number assigned by the customer.  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding difference arises when invoice in one currency are settled in another currency  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1DnAmount:int = obj["Rpt1DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2DnAmount:int = obj["Rpt2DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3DnAmount:int = obj["Rpt3DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.TaxReceiptDate:str = obj["TaxReceiptDate"]
      """  Tax Receipt Date (Thailand Localization)  """  
      self.TaxReceiptNo:str = obj["TaxReceiptNo"]
      """  Tax Receipt No. (Thailand Localization)  """  
      self.WHTCertificateDate:str = obj["WHTCertificateDate"]
      """  Withholding Tax Certificate Date  (Thailand Localization)  """  
      self.WHTCertificateNo:str = obj["WHTCertificateNo"]
      """  Withholding Tax Certificate No. (Thailand Localization)  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  Invoice Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Invoice Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.TaxRemarks:str = obj["TaxRemarks"]
      """  Tax Remarks  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.SEPADDMsgID:str = obj["SEPADDMsgID"]
      """  SEPADDMsgID  """  
      self.SEPADDPmtID:str = obj["SEPADDPmtID"]
      """  SEPADDPmtID  """  
      self.PmtDueDate:str = obj["PmtDueDate"]
      """  PmtDueDate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.MXPaymentNum:int = obj["MXPaymentNum"]
      """  MX Payment Number for AR Invoice  """  
      self.WriteOffHeadNumRef:int = obj["WriteOffHeadNumRef"]
      """  Reference to HeadNum of main CashHead record.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  EpicorFSA  """  
      self.TaxableAdjustment:bool = obj["TaxableAdjustment"]
      """  Taxable Adjustment  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BaseAdjAmt:int = obj["BaseAdjAmt"]
      """  Adjustment amount in Base Currency  """  
      self.BaseCurrDesc:str = obj["BaseCurrDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.BillConNum:int = obj["BillConNum"]
      """  The Billing Contact Number.  Obtained from InvcHead.BillConNum.  """  
      self.CopyRate:bool = obj["CopyRate"]
      """  If this flag is true the AR Invoice exchange rates is used when the Adjustment is applied and no currency Gain/Loss is calculated  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Indicates if invoice related to  this detail line is Correction invoice with negatice balance  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyDescription:str = obj["CurrencyDescription"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol  """  
      self.DebitNotesApplied:str = obj["DebitNotesApplied"]
      """  This field displays all Debit Note customer defined numbers applied.  """  
      self.DispDocSelfAssessAmt:int = obj["DispDocSelfAssessAmt"]
      self.DispDocWithholdAmt:int = obj["DispDocWithholdAmt"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display gl account  """  
      self.DispSelfAssessAmt:int = obj["DispSelfAssessAmt"]
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DispWithholdAmt:int = obj["DispWithholdAmt"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Doc Invoice Amount  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Doc Invoice Balance  """  
      self.DocNetCash:int = obj["DocNetCash"]
      self.DocNewBalance:int = obj["DocNewBalance"]
      """  Doc New Invoice Balance  """  
      self.DocWriteOffAmount:int = obj["DocWriteOffAmount"]
      """  Write Off Amount  """  
      self.DsblCopyRate:bool = obj["DsblCopyRate"]
      """  If this flag is true then CopyRate checkbox is Read Only  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Legal Number Field  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Legal Number Field  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  """  
      self.GainLossAmt:int = obj["GainLossAmt"]
      self.GLRefCodeDesc:str = obj["GLRefCodeDesc"]
      """  G/L Reference Code Description  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Legal Number Field  """  
      self.InvDiscountDate:str = obj["InvDiscountDate"]
      self.InvDueDate:str = obj["InvDueDate"]
      self.InvExchRate:int = obj["InvExchRate"]
      """  Invoice Exchange Rate  """  
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      self.InvLockRate:bool = obj["InvLockRate"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Invoice Amount  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoice Balance  """  
      self.InvTermsCode:str = obj["InvTermsCode"]
      self.InvXRateLabel:str = obj["InvXRateLabel"]
      self.IsCreditPayment:bool = obj["IsCreditPayment"]
      """  This flag is used to differentiate between a normal Invoice Credit Memo and a Credit Payment.  """  
      self.IsDiscountforCreditM:bool = obj["IsDiscountforCreditM"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      self.NetCash:int = obj["NetCash"]
      self.NewBalance:int = obj["NewBalance"]
      """  New Invoice Balance  """  
      self.OldGainLoss:int = obj["OldGainLoss"]
      self.OrderNum:int = obj["OrderNum"]
      """  The related order number (InvcHead.OrderNum)  """  
      self.PNRef:str = obj["PNRef"]
      """  Processing company's Reference ID, unique to each transaction  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions  """  
      self.RecalcTranAmt:bool = obj["RecalcTranAmt"]
      """  Whether to recalculate the CashDtl.TranAmt and all related columns prior to saving.  """  
      self.RedStornoOpt:str = obj["RedStornoOpt"]
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.RemoveForAdjustment:bool = obj["RemoveForAdjustment"]
      """  This will indicate the information on this CashDtl record will not be included in the Cash Receipt Adjustment.  """  
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt1GainLossAmt:int = obj["Rpt1GainLossAmt"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt1NetCash:int = obj["Rpt1NetCash"]
      self.Rpt1NewBalance:int = obj["Rpt1NewBalance"]
      self.Rpt1OldGainLoss:int = obj["Rpt1OldGainLoss"]
      self.Rpt1WriteOffAmount:int = obj["Rpt1WriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt1WriteOffGainLossAmt:int = obj["Rpt1WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt2GainLossAmt:int = obj["Rpt2GainLossAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt2NetCash:int = obj["Rpt2NetCash"]
      self.Rpt2NewBalance:int = obj["Rpt2NewBalance"]
      self.Rpt2OldGainLoss:int = obj["Rpt2OldGainLoss"]
      self.Rpt2WriteOffAmount:int = obj["Rpt2WriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt2WriteOffGainLossAmt:int = obj["Rpt2WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt3GainLossAmt:int = obj["Rpt3GainLossAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.Rpt3NetCash:int = obj["Rpt3NetCash"]
      self.Rpt3NewBalance:int = obj["Rpt3NewBalance"]
      self.Rpt3OldGainLoss:int = obj["Rpt3OldGainLoss"]
      self.Rpt3WriteOffAmount:int = obj["Rpt3WriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt3WriteOffGainLossAmt:int = obj["Rpt3WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  CustID associated with CashDtl.SoldToCustNum  """  
      self.SoldToCustNum:int = obj["SoldToCustNum"]
      """  Populated from InvcHead.SoldToCustNum.  """  
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  CustName associated with CashDtl.SoldToCustNum  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  Legal Number Field  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Description of the Tran Type  """  
      self.Type:str = obj["Type"]
      """  This field shows if this CashDtl line is 'Debit Note' type , created as a result of Debit Note(s) applied.  """  
      self.WriteOff:bool = obj["WriteOff"]
      """  Write Off  """  
      self.WriteOffAccount:str = obj["WriteOffAccount"]
      """  Write Off Account  """  
      self.WriteOffAccountDesc:str = obj["WriteOffAccountDesc"]
      """  Write Off Account Description  """  
      self.WriteOffAmount:int = obj["WriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffGainLossAmt:int = obj["WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.XRateLabel:str = obj["XRateLabel"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Legal Number Field  """  
      self.OldWriteOffAmount:int = obj["OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffAccountDisp:str = obj["WriteOffAccountDisp"]
      self.TaxableWriteOff:bool = obj["TaxableWriteOff"]
      self.TotalGainLossAmt:int = obj["TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.OldWriteOffGainLossAmt:int = obj["OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt1OldWriteOffGainLossAmt:int = obj["Rpt1OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt2OldWriteOffGainLossAmt:int = obj["Rpt2OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt3OldWriteOffGainLossAmt:int = obj["Rpt3OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt1TotalGainLossAmt:int = obj["Rpt1TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.Rpt2TotalGainLossAmt:int = obj["Rpt2TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.Rpt3TotalGainLossAmt:int = obj["Rpt3TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.DocOldWriteOffAmount:int = obj["DocOldWriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt1OldWriteOffAmount:int = obj["Rpt1OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt2OldWriteOffAmount:int = obj["Rpt2OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt3OldWriteOffAmount:int = obj["Rpt3OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffComment:str = obj["WriteOffComment"]
      """  Allows uset to enter comment for Write Off.  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.ReferenceTranDate:str = obj["ReferenceTranDate"]
      self.ReferenceTranNum:int = obj["ReferenceTranNum"]
      self.ReferenceTranTime:int = obj["ReferenceTranTime"]
      self.EnableManualWHTax:bool = obj["EnableManualWHTax"]
      """  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  """  
      self.WHTaxManualChange:bool = obj["WHTaxManualChange"]
      """  Indicates if the withholding amount tax was manually modified.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.InvoiceNumInvoiceType:str = obj["InvoiceNumInvoiceType"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Displays the ID of the group the transaction is assigned to.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Displays the receipt header number used for internal reference.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.TranType:str = obj["TranType"]
      """  Displays the transaction type.  """  
      self.CheckRef:str = obj["CheckRef"]
      """  Displays the number of the check.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Displays the transaction amount.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Displays the transaction amount in customer currency.  """  
      self.CustID:str = obj["CustID"]
      """  Displays the customer ID.  """  
      self.TranDate:str = obj["TranDate"]
      """  Displays the date of the transaction.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  """  
      self.UnAppliedAmt:int = obj["UnAppliedAmt"]
      """  Displays the unapplied amount.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Displays the unapplied amount in base currency.  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Displays the amount applied to invoices.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Displays the amount in document currency applied to invoices.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Displays the fiscal year that the check is posted to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Displays the fiscal period that the check is posted to.  """  
      self.Reference:str = obj["Reference"]
      """  Displays any reference.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted.  """  
      self.CreditMemoNum:int = obj["CreditMemoNum"]
      """  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Displays the customer currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Displays the exchange rate that is used for this check.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Displays the tax amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Displays the legal number of the check.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.CardType:str = obj["CardType"]
      """  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  """  
      self.ExpirationMonth:int = obj["ExpirationMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpirationYear:int = obj["ExpirationYear"]
      """  The expiration year of the credit card.  """  
      self.CardID:str = obj["CardID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Stores the encrypted credit card number  """  
      self.CCAmount:int = obj["CCAmount"]
      """  Credit Transaction Amount, makes up part of CCTotal  """  
      self.CCFreight:int = obj["CCFreight"]
      """  Credit Card transaction freight amount, part of CCTotal  """  
      self.CCTax:int = obj["CCTax"]
      """  Credit Card Transaction Tax amount, part of CCTotal  """  
      self.CCTotal:int = obj["CCTotal"]
      """  Total amount being sent to the credit card processor  """  
      self.CCDocAmount:int = obj["CCDocAmount"]
      """  See CCAmount  """  
      self.CCDocFreight:int = obj["CCDocFreight"]
      """  See CCFreight  """  
      self.CCDocTax:int = obj["CCDocTax"]
      """  See CCTax  """  
      self.CCDocTotal:int = obj["CCDocTotal"]
      """  See CCTotal  """  
      self.CCStreetAddr:str = obj["CCStreetAddr"]
      """  Address used during AVS validation for credit transactions  """  
      self.CCZip:str = obj["CCZip"]
      """  Zip used during AVS validation in credit transactions  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnAppliedAmt:int = obj["Rpt1UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnAppliedAmt:int = obj["Rpt2UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnAppliedAmt:int = obj["Rpt3UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.DocDepApplied:int = obj["DocDepApplied"]
      """  Amount of deposit applied  """  
      self.Rpt1CCAmount:int = obj["Rpt1CCAmount"]
      """  See CCAmount  """  
      self.Rpt2CCAmount:int = obj["Rpt2CCAmount"]
      """  See CCAmount  """  
      self.Rpt3CCAmount:int = obj["Rpt3CCAmount"]
      """  See CCAmount  """  
      self.Rpt1CCFreight:int = obj["Rpt1CCFreight"]
      """  See CCFreight  """  
      self.Rpt2CCFreight:int = obj["Rpt2CCFreight"]
      """  See CCFreight  """  
      self.Rpt3CCFreight:int = obj["Rpt3CCFreight"]
      """  See CCFreight  """  
      self.Rpt1CCTax:int = obj["Rpt1CCTax"]
      """  See CCTax  """  
      self.Rpt2CCTax:int = obj["Rpt2CCTax"]
      """  See CCTax  """  
      self.Rpt3CCTax:int = obj["Rpt3CCTax"]
      """  See CCTax  """  
      self.Rpt1CCTotal:int = obj["Rpt1CCTotal"]
      """  See CCTotal  """  
      self.Rpt2CCTotal:int = obj["Rpt2CCTotal"]
      """  See CCTotal  """  
      self.Rpt3CCTotal:int = obj["Rpt3CCTotal"]
      """  See CCTotal  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.ReceiptCurrencyCode:str = obj["ReceiptCurrencyCode"]
      """  The unique code of Receipt Currency.  """  
      self.ReceiptAmt:int = obj["ReceiptAmt"]
      """  Amount of Receipt in Receipt Currency.  """  
      self.BankRcptExchangeRate:int = obj["BankRcptExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  """  
      self.SettlementExchangeRate:int = obj["SettlementExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  """  
      self.CMCurrencyCode:str = obj["CMCurrencyCode"]
      """  The unique Currency code for Credit Memo.  """  
      self.CMAmount:int = obj["CMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.ReverseRef:int = obj["ReverseRef"]
      """  Reference to cash receipt which had been reversed.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Date when cash receipt had been reversed  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.TaxWhld:int = obj["TaxWhld"]
      """  Withhold Tax  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Dsicount Date  """  
      self.TaxWhldCalc:int = obj["TaxWhldCalc"]
      """  Calculate Withhold Tax  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Addition to Contract  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.UnallocatedAmt:int = obj["UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  """  
      self.DocUnallocatedAmt:int = obj["DocUnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  """  
      self.Rpt1UnallocatedAmt:int = obj["Rpt1UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  """  
      self.Rpt2UnallocatedAmt:int = obj["Rpt2UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  """  
      self.Rpt3UnallocatedAmt:int = obj["Rpt3UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  """  
      self.ApplyHeadNum:int = obj["ApplyHeadNum"]
      """  Number of the unallocated deposit payment to be apply.  """  
      self.AllocatedAmt:int = obj["AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Base currency.  """  
      self.DocAllocatedAmt:int = obj["DocAllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Document currency.  """  
      self.Rpt1AllocatedAmt:int = obj["Rpt1AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  """  
      self.Rpt2AllocatedAmt:int = obj["Rpt2AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  """  
      self.Rpt3AllocatedAmt:int = obj["Rpt3AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  """  
      self.Comment:str = obj["Comment"]
      """  Comments related to the cash receipt.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment Method Unique Identifier  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.BankTranID:str = obj["BankTranID"]
      """  ID Given by the Bank assigned during matching  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.TaxRemarks:str = obj["TaxRemarks"]
      """  Tax Remarks  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.BankTransDate:str = obj["BankTransDate"]
      """  Bank Transaction Date  """  
      self.Payee:str = obj["Payee"]
      """  Payee  """  
      self.AccountNumber:str = obj["AccountNumber"]
      """  AccountNumber  """  
      self.OtherDetails:str = obj["OtherDetails"]
      """  OtherDetails  """  
      self.MandateReference:str = obj["MandateReference"]
      """  MandateReference  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SEPADDExportDate:str = obj["SEPADDExportDate"]
      """  SEPADDExportDate  """  
      self.BOEInvoiceNum:int = obj["BOEInvoiceNum"]
      """  BOE Invoice Number  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.OwnReference:str = obj["OwnReference"]
      """  OwnReference  """  
      self.DocumentType:str = obj["DocumentType"]
      """  DocumentType  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.BankRcptExchangeRate10D:int = obj["BankRcptExchangeRate10D"]
      """  BankRcptExchangeRate10D  """  
      self.SettlementExchangeRate10D:int = obj["SettlementExchangeRate10D"]
      """  SettlementExchangeRate10D  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.PayMethodReference:str = obj["PayMethodReference"]
      """  PayMethodReference  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MX Receipt’s Fiscal Folio (UUID)  """  
      self.AllowUpdSettlementCurr:bool = obj["AllowUpdSettlementCurr"]
      """  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.AVSAddr:str = obj["AVSAddr"]
      """  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.AVSZip:str = obj["AVSZip"]
      """  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.BankAcctDesc:str = obj["BankAcctDesc"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Currency Value  """  
      self.BankBaseXRateLabel:str = obj["BankBaseXRateLabel"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      """  Bank Currency Symbol  """  
      self.BankExchangeRate:int = obj["BankExchangeRate"]
      self.BankRcptXRateLabel:str = obj["BankRcptXRateLabel"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      """  Bill To Name  """  
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  """  
      self.CardStore:str = obj["CardStore"]
      """  Stored Credit Card Number  """  
      self.CardTypeDescription:str = obj["CardTypeDescription"]
      """  The credit card description. For example, American Express, Visa, Master Card, Discover, etc.  """  
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      """  Description  """  
      self.CCAllowSales:bool = obj["CCAllowSales"]
      """  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  """  
      self.CCApprovalNum:str = obj["CCApprovalNum"]
      self.CCCSCID:str = obj["CCCSCID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  """  
      self.CCEnableAddress:bool = obj["CCEnableAddress"]
      """  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  """  
      self.CCEnableCSC:bool = obj["CCEnableCSC"]
      """  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  """  
      self.CCResponse:str = obj["CCResponse"]
      """  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  """  
      self.CCTranID:str = obj["CCTranID"]
      """  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  """  
      self.CCTranType:str = obj["CCTranType"]
      """  Credit Card Transaction Type  """  
      self.CMCurrencyCodeCurrDesc:str = obj["CMCurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CMCurrencyCodeCurrencyID:str = obj["CMCurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CMCurrencyCodeCurrName:str = obj["CMCurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CMCurrencyCodeCurrSymbol:str = obj["CMCurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CMCurrencyCodeDocumentDesc:str = obj["CMCurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CSCResult:str = obj["CSCResult"]
      """  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustFullAddr:str = obj["CustFullAddr"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustomerName:str = obj["CustomerName"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.DocumentNum:int = obj["DocumentNum"]
      """  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  """  
      self.DspCMAmount:int = obj["DspCMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.DspDocTranAmt:int = obj["DspDocTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user enters this amount and then it is used as a limit/control when applying it to the invoices.  """  
      self.DspSalesOrderValue:int = obj["DspSalesOrderValue"]
      self.DspTranAmt:int = obj["DspTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  """  
      self.EnableTransactionDate:bool = obj["EnableTransactionDate"]
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  """  
      self.InvcLegalNumber:str = obj["InvcLegalNumber"]
      """  The InvcHead legal number  """  
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      """  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumberDsp:str = obj["LegalNumberDsp"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockRate:bool = obj["LockRate"]
      """  Copied from OrderHed.LockRate  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.PaymentMethod:str = obj["PaymentMethod"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      """  Description  """  
      self.RcptCurrencyCodeCurrDesc:str = obj["RcptCurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.RcptCurrencyCodeCurrencyID:str = obj["RcptCurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.RcptCurrencyCodeCurrName:str = obj["RcptCurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.RcptCurrencyCodeCurrSymbol:str = obj["RcptCurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.RcptCurrencyCodeDocumentDesc:str = obj["RcptCurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.ReferencePNRef:str = obj["ReferencePNRef"]
      """  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  """  
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SalesOrderValue:int = obj["SalesOrderValue"]
      self.SettlementXRateLabel:str = obj["SettlementXRateLabel"]
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  """  
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      """  Sum of all rounding differences of the payments for one Cash Receipt and one Check  """  
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Description of TranType  """  
      self.UnappliedAmountApplied:bool = obj["UnappliedAmountApplied"]
      """  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  """  
      self.XRateLabel:str = obj["XRateLabel"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Displays the ID of the group the transaction is assigned to.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Displays the receipt header number used for internal reference.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.TranType:str = obj["TranType"]
      """  Displays the transaction type.  """  
      self.CheckRef:str = obj["CheckRef"]
      """  Displays the number of the check.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Displays the transaction amount.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Displays the transaction amount in customer currency.  """  
      self.CustID:str = obj["CustID"]
      """  Displays the customer ID.  """  
      self.TranDate:str = obj["TranDate"]
      """  Displays the date of the transaction.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  """  
      self.UnAppliedAmt:int = obj["UnAppliedAmt"]
      """  Displays the unapplied amount.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Displays the unapplied amount in base currency.  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Displays the amount applied to invoices.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Displays the amount in document currency applied to invoices.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Displays the fiscal year that the check is posted to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Displays the fiscal period that the check is posted to.  """  
      self.Reference:str = obj["Reference"]
      """  Displays any reference.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted.  """  
      self.CreditMemoNum:int = obj["CreditMemoNum"]
      """  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Displays the customer currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Displays the exchange rate that is used for this check.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Displays the tax amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Displays the legal number of the check.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.CardType:str = obj["CardType"]
      """  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  """  
      self.ExpirationMonth:int = obj["ExpirationMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpirationYear:int = obj["ExpirationYear"]
      """  The expiration year of the credit card.  """  
      self.CardID:str = obj["CardID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Stores the encrypted credit card number  """  
      self.CCAmount:int = obj["CCAmount"]
      """  Credit Transaction Amount, makes up part of CCTotal  """  
      self.CCFreight:int = obj["CCFreight"]
      """  Credit Card transaction freight amount, part of CCTotal  """  
      self.CCTax:int = obj["CCTax"]
      """  Credit Card Transaction Tax amount, part of CCTotal  """  
      self.CCTotal:int = obj["CCTotal"]
      """  Total amount being sent to the credit card processor  """  
      self.CCDocAmount:int = obj["CCDocAmount"]
      """  See CCAmount  """  
      self.CCDocFreight:int = obj["CCDocFreight"]
      """  See CCFreight  """  
      self.CCDocTax:int = obj["CCDocTax"]
      """  See CCTax  """  
      self.CCDocTotal:int = obj["CCDocTotal"]
      """  See CCTotal  """  
      self.CCStreetAddr:str = obj["CCStreetAddr"]
      """  Address used during AVS validation for credit transactions  """  
      self.CCZip:str = obj["CCZip"]
      """  Zip used during AVS validation in credit transactions  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnAppliedAmt:int = obj["Rpt1UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnAppliedAmt:int = obj["Rpt2UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnAppliedAmt:int = obj["Rpt3UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.DocDepApplied:int = obj["DocDepApplied"]
      """  Amount of deposit applied  """  
      self.Rpt1CCAmount:int = obj["Rpt1CCAmount"]
      """  See CCAmount  """  
      self.Rpt2CCAmount:int = obj["Rpt2CCAmount"]
      """  See CCAmount  """  
      self.Rpt3CCAmount:int = obj["Rpt3CCAmount"]
      """  See CCAmount  """  
      self.Rpt1CCFreight:int = obj["Rpt1CCFreight"]
      """  See CCFreight  """  
      self.Rpt2CCFreight:int = obj["Rpt2CCFreight"]
      """  See CCFreight  """  
      self.Rpt3CCFreight:int = obj["Rpt3CCFreight"]
      """  See CCFreight  """  
      self.Rpt1CCTax:int = obj["Rpt1CCTax"]
      """  See CCTax  """  
      self.Rpt2CCTax:int = obj["Rpt2CCTax"]
      """  See CCTax  """  
      self.Rpt3CCTax:int = obj["Rpt3CCTax"]
      """  See CCTax  """  
      self.Rpt1CCTotal:int = obj["Rpt1CCTotal"]
      """  See CCTotal  """  
      self.Rpt2CCTotal:int = obj["Rpt2CCTotal"]
      """  See CCTotal  """  
      self.Rpt3CCTotal:int = obj["Rpt3CCTotal"]
      """  See CCTotal  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.ReceiptCurrencyCode:str = obj["ReceiptCurrencyCode"]
      """  The unique code of Receipt Currency.  """  
      self.ReceiptAmt:int = obj["ReceiptAmt"]
      """  Amount of Receipt in Receipt Currency.  """  
      self.BankRcptExchangeRate:int = obj["BankRcptExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  """  
      self.SettlementExchangeRate:int = obj["SettlementExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  """  
      self.CMCurrencyCode:str = obj["CMCurrencyCode"]
      """  The unique Currency code for Credit Memo.  """  
      self.CMAmount:int = obj["CMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.ReverseRef:int = obj["ReverseRef"]
      """  Reference to cash receipt which had been reversed.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Date when cash receipt had been reversed  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.TaxWhld:int = obj["TaxWhld"]
      """  Withhold Tax  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Dsicount Date  """  
      self.TaxWhldCalc:int = obj["TaxWhldCalc"]
      """  Calculate Withhold Tax  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Addition to Contract  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.UnallocatedAmt:int = obj["UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  """  
      self.DocUnallocatedAmt:int = obj["DocUnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  """  
      self.Rpt1UnallocatedAmt:int = obj["Rpt1UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  """  
      self.Rpt2UnallocatedAmt:int = obj["Rpt2UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  """  
      self.Rpt3UnallocatedAmt:int = obj["Rpt3UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  """  
      self.ApplyHeadNum:int = obj["ApplyHeadNum"]
      """  Number of the unallocated deposit payment to be apply.  """  
      self.AllocatedAmt:int = obj["AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Base currency.  """  
      self.DocAllocatedAmt:int = obj["DocAllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Document currency.  """  
      self.Rpt1AllocatedAmt:int = obj["Rpt1AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  """  
      self.Rpt2AllocatedAmt:int = obj["Rpt2AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  """  
      self.Rpt3AllocatedAmt:int = obj["Rpt3AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  """  
      self.Comment:str = obj["Comment"]
      """  Comments related to the cash receipt.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment Method Unique Identifier  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.BankTranID:str = obj["BankTranID"]
      """  ID Given by the Bank assigned during matching  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.TaxRemarks:str = obj["TaxRemarks"]
      """  Tax Remarks  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.BankTransDate:str = obj["BankTransDate"]
      """  Bank Transaction Date  """  
      self.Payee:str = obj["Payee"]
      """  Payee  """  
      self.AccountNumber:str = obj["AccountNumber"]
      """  AccountNumber  """  
      self.OtherDetails:str = obj["OtherDetails"]
      """  OtherDetails  """  
      self.MandateReference:str = obj["MandateReference"]
      """  MandateReference  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SEPADDExportDate:str = obj["SEPADDExportDate"]
      """  SEPADDExportDate  """  
      self.BOEInvoiceNum:int = obj["BOEInvoiceNum"]
      """  BOE Invoice Number  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.OwnReference:str = obj["OwnReference"]
      """  OwnReference  """  
      self.DocumentType:str = obj["DocumentType"]
      """  DocumentType  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.BankRcptExchangeRate10D:int = obj["BankRcptExchangeRate10D"]
      """  BankRcptExchangeRate10D  """  
      self.SettlementExchangeRate10D:int = obj["SettlementExchangeRate10D"]
      """  SettlementExchangeRate10D  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.PayMethodReference:str = obj["PayMethodReference"]
      """  PayMethodReference  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.RcptCurAppliedAmt:int = obj["RcptCurAppliedAmt"]
      """  The amount of the cash receipt applied to invoices in receipt currency  """  
      self.RcptCurUnAppliedAmt:int = obj["RcptCurUnAppliedAmt"]
      """  The amount of the cash receipt that is unapplied in receipt currency  """  
      self.MXAccountNumber:str = obj["MXAccountNumber"]
      """  MXAccountNumber  """  
      self.MXPaidAs:str = obj["MXPaidAs"]
      """  MX Method of Payment: single, multiple, etc.  """  
      self.MXPaySupplementFlag:bool = obj["MXPaySupplementFlag"]
      """  If TRUE then MX Electronic Payment XML is required  """  
      self.LockboxID:str = obj["LockboxID"]
      """  LockboxID  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MX Receipt’s Fiscal Folio (UUID)  """  
      self.MXOriginalCheckRef:str = obj["MXOriginalCheckRef"]
      """  MX UUID of the original Receipt being corrected  """  
      self.MXConfirmationCode:str = obj["MXConfirmationCode"]
      """  MX Confirmation Code for special Cash Receipts  """  
      self.MXBankID:str = obj["MXBankID"]
      """  MX Customer’s Bank ID  """  
      self.ReversedReason:str = obj["ReversedReason"]
      """  Text entered by the user to indicate the reason Cash receipt was Reversed.  """  
      self.CCCity:str = obj["CCCity"]
      """  Credit Card Holder City.  """  
      self.CCState:str = obj["CCState"]
      """  Credit Card Holder State.  """  
      self.ccToken:str = obj["ccToken"]
      """  ccToken  """  
      self.DepositBalance:int = obj["DepositBalance"]
      """  DepositBalance  """  
      self.DocDepositBalance:int = obj["DocDepositBalance"]
      """  DocDepositBalance  """  
      self.Rpt1DepositBalance:int = obj["Rpt1DepositBalance"]
      """  Rpt1DepositBalance  """  
      self.Rpt2DepositBalance:int = obj["Rpt2DepositBalance"]
      """  Rpt2DepositBalance  """  
      self.Rpt3DepositBalance:int = obj["Rpt3DepositBalance"]
      """  Rpt3DepositBalance  """  
      self.Adjustment:bool = obj["Adjustment"]
      """  Indicates this record is an adjustment CashHead.  """  
      self.AdjustmentRef:int = obj["AdjustmentRef"]
      """  Reference to cash receipt which had been adjusted.  """  
      self.AdjustmentReason:str = obj["AdjustmentReason"]
      """  The reason for the adjustment entered by the user  """  
      self.WriteOffAmount:int = obj["WriteOffAmount"]
      """  Total Check Write Off Amount  """  
      self.DocWriteOffAmount:int = obj["DocWriteOffAmount"]
      """  DocWriteOffAmount  """  
      self.Rpt1WriteOffAmount:int = obj["Rpt1WriteOffAmount"]
      """  Rpt1WriteOffAmount  """  
      self.Rpt2WriteOffAmount:int = obj["Rpt2WriteOffAmount"]
      """  Rpt2WriteOffAmount  """  
      self.Rpt3WriteOffAmount:int = obj["Rpt3WriteOffAmount"]
      """  Rpt3WriteOffAmount  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  Mexico Certified Timestamp  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  Mexico SAT Seal  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  Mexico Digital Seal  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  Mexico SAT Certificate Serial Number  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  Mexico Original String Timbre Fiscal Digital  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  Mexico Certificate  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  Mexico Certificate Serial Number  """  
      self.SourceGroupID:str = obj["SourceGroupID"]
      """  SourceGroupID  """  
      self.SourceHeadNum:int = obj["SourceHeadNum"]
      """  SourceHeadNum  """  
      self.SEC:str = obj["SEC"]
      """  Standard Entry Class Code  """  
      self.ACHTranCode:int = obj["ACHTranCode"]
      """  ACH Transaction Code  """  
      self.CustomerBankID:str = obj["CustomerBankID"]
      """  ID of the Customer's bank.  """  
      self.CustomerBankAcctNumber:str = obj["CustomerBankAcctNumber"]
      """  The Bank account number for the Customer.  """  
      self.CustomerBankSwiftNum:str = obj["CustomerBankSwiftNum"]
      """  CustomerBankSwiftNum  """  
      self.CustomerBankIBANCode:str = obj["CustomerBankIBANCode"]
      """  The Bank account IBAN Code  """  
      self.CustomerBankNameOnAccount:str = obj["CustomerBankNameOnAccount"]
      """  Name on the Bank Account.  """  
      self.CustomerBankAddress1:str = obj["CustomerBankAddress1"]
      """  First address line of customer bank.  """  
      self.CustomerBankAddress2:str = obj["CustomerBankAddress2"]
      """  Second address line of customer bank.  """  
      self.CustomerBankAddress3:str = obj["CustomerBankAddress3"]
      """  Third address line of customer bank.  """  
      self.CustomerBankCity:str = obj["CustomerBankCity"]
      """  Bank City  """  
      self.CustomerBankState:str = obj["CustomerBankState"]
      """  Bank State/Prov  """  
      self.CustomerBankPostalCode:str = obj["CustomerBankPostalCode"]
      """  Postal Code or zip code  """  
      self.CustomerBankCountryNum:int = obj["CustomerBankCountryNum"]
      """  Bank account Country Number.  """  
      self.ARRemittanceSlipPrinted:bool = obj["ARRemittanceSlipPrinted"]
      """  ARRemittanceSlipPrinted  """  
      self.CustomerBankName:str = obj["CustomerBankName"]
      """  Customer Bank Name  """  
      self.MXPostedTimeStamp:str = obj["MXPostedTimeStamp"]
      """  MXPostedTimeStamp  """  
      self.MXSerie:str = obj["MXSerie"]
      """  MXSerie  """  
      self.MXFolio:str = obj["MXFolio"]
      """  MXFolio  """  
      self.MXEPaymentType:str = obj["MXEPaymentType"]
      """  MXEPaymentType  """  
      self.MXEPaymentCertificateNumber:str = obj["MXEPaymentCertificateNumber"]
      """  MXEPaymentCertificateNumber  """  
      self.MXEPaymentOriginalString:str = obj["MXEPaymentOriginalString"]
      """  MXEPaymentOriginalString  """  
      self.MXEPaymentDigitalSeal:str = obj["MXEPaymentDigitalSeal"]
      """  MXEPaymentDigitalSeal  """  
      self.Source:str = obj["Source"]
      """  Source  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  GL Description for the Reverse process  """  
      self.CMDescription:str = obj["CMDescription"]
      """  GL Description for AR - Apply Credit Memo  """  
      self.BankReceiptAmt:int = obj["BankReceiptAmt"]
      """  Receipt Amount in Bank Currency  """  
      self.MXCancelReasonCode:str = obj["MXCancelReasonCode"]
      """  MXCancelReasonCode  """  
      self.MXSubstHeadNum:int = obj["MXSubstHeadNum"]
      """  MXSubstHeadNum  """  
      self.MXCancellationMode:str = obj["MXCancellationMode"]
      """  MXCancellationMode  """  
      self.ELIEInvException:str = obj["ELIEInvException"]
      """  E-invoice error description.  """  
      self.ELIEInvID:str = obj["ELIEInvID"]
      """  EInvoice ID  """  
      self.ELIEInvoice:bool = obj["ELIEInvoice"]
      """  E-invoice  """  
      self.ELIEInvServiceProviderStatus:int = obj["ELIEInvServiceProviderStatus"]
      """  E-invoice Service Provider Status  """  
      self.ELIEInvStatus:int = obj["ELIEInvStatus"]
      """  E-invoice Status  """  
      self.ELIEInvUpdatedBy:str = obj["ELIEInvUpdatedBy"]
      """  User Id of the person generated E-invoice.  """  
      self.ELIEInvUpdatedOn:str = obj["ELIEInvUpdatedOn"]
      """  E-invoice Updated On  """  
      self.AdjustmentCustName:str = obj["AdjustmentCustName"]
      """  Adjustment Customer Name  """  
      self.AdjustmentCustNum:int = obj["AdjustmentCustNum"]
      """  Customer to which the new invoices will be applied.  """  
      self.AdjustmentDate:str = obj["AdjustmentDate"]
      """  Date the adjustment was made.  """  
      self.AdjustmentDocUnAppliedAmt:int = obj["AdjustmentDocUnAppliedAmt"]
      """  Displays the amount available to apply to the invoices.  """  
      self.AdjustmentOnAccount:bool = obj["AdjustmentOnAccount"]
      """  On Account  """  
      self.AdjustmentTranDocTypeID:str = obj["AdjustmentTranDocTypeID"]
      """  Temp TranDocTypeID used when adjusting a Cash Rececipt  """  
      self.AllocDepBal:int = obj["AllocDepBal"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.AllowUpdSettlementCurr:bool = obj["AllowUpdSettlementCurr"]
      """  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  """  
      self.AmtToAlloc:int = obj["AmtToAlloc"]
      """  Amount to Allocate  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.AVSAddr:str = obj["AVSAddr"]
      """  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.AVSZip:str = obj["AVSZip"]
      """  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Currency Value  """  
      self.BankBaseXRateLabel:str = obj["BankBaseXRateLabel"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      """  Bank Currency Symbol  """  
      self.BankExchangeRate:int = obj["BankExchangeRate"]
      self.BankRcptXRateLabel:str = obj["BankRcptXRateLabel"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Base Currency Symbol  """  
      self.BillToName:str = obj["BillToName"]
      """  Bill To Name  """  
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  """  
      self.CardStore:str = obj["CardStore"]
      """  Stored Credit Card Number  """  
      self.CCAllowSales:bool = obj["CCAllowSales"]
      """  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  """  
      self.CCApprovalNum:str = obj["CCApprovalNum"]
      self.CCCSCID:str = obj["CCCSCID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  """  
      self.CCCSCIDToken:str = obj["CCCSCIDToken"]
      """  Tokenized value of CSCID  """  
      self.CCEnableAddress:bool = obj["CCEnableAddress"]
      """  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  """  
      self.CCEnableCSC:bool = obj["CCEnableCSC"]
      """  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  """  
      self.CCIsTraining:bool = obj["CCIsTraining"]
      """   Indicates if the credit card setup will be using a testing Paygate instance for transactions.
Force requests to use Paygate test url: paygate-test1.eaglesoa.com  """  
      self.CCResponse:str = obj["CCResponse"]
      """  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  """  
      self.CCTranID:str = obj["CCTranID"]
      """  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  """  
      self.CCTranType:str = obj["CCTranType"]
      """  Credit Card Transaction Type  """  
      self.CentralCollectionCheck:bool = obj["CentralCollectionCheck"]
      """  Check Box on the UI to filter records by Central Collection flag  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Correction Invoice with negative amount  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      """  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Credit Memo  """  
      self.CREProcessor:bool = obj["CREProcessor"]
      """  CREProcessor is true when Credit Card Configuration is CRE Server.  """  
      self.CSCResult:str = obj["CSCResult"]
      """  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.CurrAmtSelected:int = obj["CurrAmtSelected"]
      """  Current Amount Selected on Invoice Select Tab  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustFullAddr:str = obj["CustFullAddr"]
      """  Displays the address of the customer that paid the receipt.  """  
      self.CustomerName:str = obj["CustomerName"]
      self.DisableFieldsForPCashDoc:bool = obj["DisableFieldsForPCashDoc"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocAllocDepBal:int = obj["DocAllocDepBal"]
      self.DocAmtToAlloc:int = obj["DocAmtToAlloc"]
      """  Doc Amount to Allocate  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  Displays the discount applied to the receipt.  """  
      self.DocReceipt:int = obj["DocReceipt"]
      """  Displays the invoice amount paid by this receipt. The amount includes both discount and payment amounts.  """  
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.DocumentNum:int = obj["DocumentNum"]
      """  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  """  
      self.DocWhldTax:int = obj["DocWhldTax"]
      self.DspBankBatchID:str = obj["DspBankBatchID"]
      self.DspCMAmount:int = obj["DspCMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.DspDocTranAmt:int = obj["DspDocTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  """  
      self.DspSalesOrderValue:int = obj["DspSalesOrderValue"]
      self.DspTranAmt:int = obj["DspTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableGetDefaultAcct:bool = obj["EnableGetDefaultAcct"]
      """  Indicates if the option to get the default account is enable.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableTransactionDate:bool = obj["EnableTransactionDate"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  """  
      self.GLRefCodeDescription:str = obj["GLRefCodeDescription"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.InvcLegalNumber:str = obj["InvcLegalNumber"]
      """  The InvcHead legal number  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumberDsp:str = obj["LegalNumberDsp"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockRate:bool = obj["LockRate"]
      """  Copied from OrderHed.LockRate  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.ManualTaxAdj:bool = obj["ManualTaxAdj"]
      self.MXCancellationID:str = obj["MXCancellationID"]
      """  MXCancellationID  """  
      self.MXCancellationStatus:str = obj["MXCancellationStatus"]
      self.MXECEPXml:str = obj["MXECEPXml"]
      """  MXECEPXml  """  
      self.MXOriginalRefNum:str = obj["MXOriginalRefNum"]
      """  Mexico Calculated field - shows Check Reference number of the original Receipt being corrected  """  
      self.PayGateHostAddress:str = obj["PayGateHostAddress"]
      """  Host Address for the Paygate Hosted Token Service.  """  
      self.PayGateNameSpace:str = obj["PayGateNameSpace"]
      """  NameSpace for the Paygate Hosted Token Service.  """  
      self.PayGatePublicKey:str = obj["PayGatePublicKey"]
      """  Public Key for the Paygate Hosted Token Service EWA component.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  This column is used within cash receipt tracker to show either the receipt date or the source/ original receipt date if the cash receipt has been adjusted.  """  
      self.ReferencePNRef:str = obj["ReferencePNRef"]
      """  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  """  
      self.Rpt1AllocDepBal:int = obj["Rpt1AllocDepBal"]
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt1WhldTax:int = obj["Rpt1WhldTax"]
      self.Rpt2AllocDepBal:int = obj["Rpt2AllocDepBal"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt2WhldTax:int = obj["Rpt2WhldTax"]
      self.Rpt3AllocDepBal:int = obj["Rpt3AllocDepBal"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt3WhldTax:int = obj["Rpt3WhldTax"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SalesOrderValue:int = obj["SalesOrderValue"]
      self.SettlementXRateLabel:str = obj["SettlementXRateLabel"]
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  """  
      self.SystemTranType:str = obj["SystemTranType"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      """  Sum of all rounding differences of the payments for one Cash Receipt and one Check  """  
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Description of TranType  """  
      self.UnappliedAmountApplied:bool = obj["UnappliedAmountApplied"]
      """  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  """  
      self.WhldTax:int = obj["WhldTax"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.AdjustmentCustID:str = obj["AdjustmentCustID"]
      """  Displays the customer ID.  """  
      self.ReferenceTranDate:str = obj["ReferenceTranDate"]
      self.ReferenceTranNum:int = obj["ReferenceTranNum"]
      self.ReferenceTranTime:int = obj["ReferenceTranTime"]
      self.CustFullAddrFormatted:str = obj["CustFullAddrFormatted"]
      """  Displays the address of the customer that paid the receipt with newline delimiter.  """  
      self.EnableManualWHTax:bool = obj["EnableManualWHTax"]
      """  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  """  
      self.WHTaxManualChange:bool = obj["WHTaxManualChange"]
      """  Indicates if the withholding tax was manually modified.  """  
      self.TranTypeDescCaption:str = obj["TranTypeDescCaption"]
      """  Payment type description, displayed in the Details page header.  """  
      self.AdjustmentCustAddress:str = obj["AdjustmentCustAddress"]
      self.MXSubstGroupId:str = obj["MXSubstGroupId"]
      """  Substitution Cash Receipt Group ID  """  
      self.MXSubstCheckRef:str = obj["MXSubstCheckRef"]
      """  Substitution Cash Receipt CheckRef  """  
      self.MXSubstFiscalFolio:str = obj["MXSubstFiscalFolio"]
      """  Substitution Cash Receipt UUID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.CardTypeDescription:str = obj["CardTypeDescription"]
      self.CashBHedPosted:bool = obj["CashBHedPosted"]
      self.CashBHedCashBookNum:int = obj["CashBHedCashBookNum"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CMCurrencyCodeDocumentDesc:str = obj["CMCurrencyCodeDocumentDesc"]
      self.CMCurrencyCodeCurrName:str = obj["CMCurrencyCodeCurrName"]
      self.CMCurrencyCodeCurrSymbol:str = obj["CMCurrencyCodeCurrSymbol"]
      self.CMCurrencyCodeCurrDesc:str = obj["CMCurrencyCodeCurrDesc"]
      self.CMCurrencyCodeCurrencyID:str = obj["CMCurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PCashDocDirection:str = obj["PCashDocDirection"]
      self.PMUIDName:str = obj["PMUIDName"]
      self.PMUIDMXSATCode:str = obj["PMUIDMXSATCode"]
      self.PMUIDSummarizePerCustomer:bool = obj["PMUIDSummarizePerCustomer"]
      self.PMUIDType:int = obj["PMUIDType"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.RcptCurrencyCodeCurrencyID:str = obj["RcptCurrencyCodeCurrencyID"]
      self.RcptCurrencyCodeDocumentDesc:str = obj["RcptCurrencyCodeDocumentDesc"]
      self.RcptCurrencyCodeCurrDesc:str = obj["RcptCurrencyCodeCurrDesc"]
      self.RcptCurrencyCodeCurrSymbol:str = obj["RcptCurrencyCodeCurrSymbol"]
      self.RcptCurrencyCodeCurrName:str = obj["RcptCurrencyCodeCurrName"]
      self.ReverseMXCancelReasonCode:str = obj["ReverseMXCancelReasonCode"]
      self.ReverseMXCancellationMode:str = obj["ReverseMXCancellationMode"]
      self.SourceTranDateTranDate:str = obj["SourceTranDateTranDate"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AdjustCashReceipt_input:
   """ Required : 
   UseDisc
   ds
   ttARInvcAlloc
   """  
   def __init__(self, obj):
      self.UseDisc:bool = obj["UseDisc"]
      """  Indicate to use the discount  """  
      self.ds:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["ds"]
      self.ttARInvcAlloc:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ttARInvcAlloc"]
      pass

class AdjustCashReceipt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["ds"]
      self.postErrorLog:str = obj["parameters"]
      self.legalNumberMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class AutoSelectItem_input:
   """ Required : 
   b_chCreditMemo
   s_chGroupID
   s_chCheckRef
   unAppliedAmt
   forceDiscount
   invcAllocRow
   """  
   def __init__(self, obj):
      self.b_chCreditMemo:bool = obj["b_chCreditMemo"]
      self.s_chGroupID:str = obj["s_chGroupID"]
      self.s_chCheckRef:str = obj["s_chCheckRef"]
      self.unAppliedAmt:int = obj["unAppliedAmt"]
      self.forceDiscount:bool = obj["forceDiscount"]
      self.invcAllocRow:list[Erp_Tablesets_ARInvcAllocRow] = obj["invcAllocRow"]
      pass

class AutoSelectItem_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.unAppliedAmt:int = obj["parameters"]
      pass

      """  output parameters  """  

class BuildCustAddress_input:
   """ Required : 
   CustName
   Address1
   Address2
   Address3
   CustCity
   CustState
   CustCountry
   CustZip
   """  
   def __init__(self, obj):
      self.CustName:str = obj["CustName"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.CustCity:str = obj["CustCity"]
      self.CustState:str = obj["CustState"]
      self.CustCountry:str = obj["CustCountry"]
      self.CustZip:str = obj["CustZip"]
      pass

class BuildCustAddress_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class CalcAllocAmount_input:
   """ Required : 
   unAppliedAmt
   forceDiscount
   ds2
   """  
   def __init__(self, obj):
      self.unAppliedAmt:int = obj["unAppliedAmt"]
      self.forceDiscount:bool = obj["forceDiscount"]
      self.ds2:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds2"]
      pass

class CalcAllocAmount_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds2:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds2"]
      pass

      """  output parameters  """  

class CalcDiscount_input:
   """ Required : 
   ipAmtToAlloc
   LastDiscount
   forceDiscount
   ds
   """  
   def __init__(self, obj):
      self.ipAmtToAlloc:int = obj["ipAmtToAlloc"]
      self.LastDiscount:bool = obj["LastDiscount"]
      self.forceDiscount:bool = obj["forceDiscount"]
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

class CalcDiscount_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CalcInvBal_input:
   """ Required : 
   dDocUnpostedBal
   dDocTotalDN
   """  
   def __init__(self, obj):
      self.dDocUnpostedBal:int = obj["dDocUnpostedBal"]
      self.dDocTotalDN:int = obj["dDocTotalDN"]
      pass

class CalcInvBal_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class CalcSelectedInvcTotal_input:
   """ Required : 
   docUnappliedAmount
   ds
   """  
   def __init__(self, obj):
      self.docUnappliedAmount:int = obj["docUnappliedAmount"]
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

class CalcSelectedInvcTotal_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CashRecGetInvoices_input:
   """ Required : 
   payDay
   custNum
   currencyCode
   tranDate
   ds
   """  
   def __init__(self, obj):
      self.payDay:str = obj["payDay"]
      """  Payment date.  """  
      self.custNum:int = obj["custNum"]
      """  CustNum to get Customer list if National Accounts are enabled  """  
      self.currencyCode:str = obj["currencyCode"]
      """  Currency Code used for the CashHed  """  
      self.tranDate:str = obj["tranDate"]
      """  Transaction date.  """  
      self.ds:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["ds"]
      pass

class CashRecGetInvoices_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARInvcAllocTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeAdjustmentCustID_input:
   """ Required : 
   adjustmentCustID
   ds
   """  
   def __init__(self, obj):
      self.adjustmentCustID:str = obj["adjustmentCustID"]
      self.ds:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["ds"]
      pass

class ChangeAdjustmentCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ARInvcAllocRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenInvoice:bool = obj["OpenInvoice"]
      """  Indicates if invoice is "open".  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  The latest transaction date (CashDtl) which was available when the invoice was closed. This is used to improve record selection performance when selecting invoices that were open as of a certain date. (Used by the aged invoice report). This is updated during the CashReceipt posting process, Adjustment entry or Apply Credit memos programs..  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      """   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  """  
      self.UnappliedCash:bool = obj["UnappliedCash"]
      """  An internal flag that represents Credit Memo was due to Unapplied Receipts. Created by the Cash Receipts Entry program.   This is only applicable with CreditMemo = Yes.  """  
      self.CheckRef:str = obj["CheckRef"]
      """   The Check reference number that the Unapplied Receipt Credit Memo was created from. Cash receipts entry sets this field equal to the CashHead.CheckRef when it creates the Unapplied Receipt Credit Memo.  Primarily used as a reference.
This is used when TranType = PrePay, MisPay or PayInv.  """  
      self.InvoiceSuffix:str = obj["InvoiceSuffix"]
      """  An internally assigned field that further identifies an invoice. This field will be displayed as a suffix to the invoice number.  The possible values are "CM" = Credit memo created by invoice entry, UR = Unapplied Receipt Credit Memo,  DN = Debit Note, and FC = Finance Charge invoice.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the BatchID of the "current " batch that the user is working with.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  """  
      self.DeferredRevenue:bool = obj["DeferredRevenue"]
      """  Only used when InvoiceType = "Adv" (Advanced Billing).  Indicates if the detail line amounts are to be considered as sales or deferred revenue.  If "No" then the G/L accounts on the detail lines are the Sales Accounts otherwise they will be set to the Deferred Revenue accounts established in the ARSyst/ARAcct files.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order #. This is a mandatory entry for all InvoiceType except "Miscellaneous". If entered it must be valid in the OrderHed file. The OrderHed supplies the invoice with many defaults, including; CustNum, PONum, TermsCode,  FOB, RepRate, RepSplit, SalesRepList, InvoiceComments  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  """  
      self.PONum:str = obj["PONum"]
      """  Customer's PO#.   This is a reference field which will be printed on the invoice. Defaults from the OrderHed.PONum.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID that entered the invoice. This is not maintainable by the user.  """  
      self.FOB:str = obj["FOB"]
      """  Defaults from sales order ORderHed.FOB  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date is duplicated from the InvcGrp record.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year is duplicated from the related InvcGrp or based on ShipDate of Packing Slip. This is also refreshed if the InvoiceDate is changed.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of invoice. This is duplicated in from the InvcBatc or during the "get shipments" function it is determined based on the ShipDate of the packing slip or when the invoice date is changed. It is overrideable.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Once posted, maintenance is not allowed.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.UnpostedBal:int = obj["UnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DepositCredit:int = obj["DepositCredit"]
      """  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  """  
      self.DocDepositCredit:int = obj["DocDepositCredit"]
      """  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  """  
      self.SalesRepList:str = obj["SalesRepList"]
      """  Stores the Sales Rep Codes for the invoice. Up to five codes can be  established. This field is not directly maintainable.  Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The defaults are based on the OrderHed.SalesRepList if a valid Order is referenced or first one is defaulted from the Customer master if ship to is blank else from the ShipTo.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """   This field is maintainable/viewable only for Credit Memos. It represents the invoice # that this credit memo relates to. It can be left blank. If entered it must be a valid InvcHead record where the InvcHead.CreditMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the credit memos next to their corresponding invoice. Therefore, this field will always have a value.

For Invoices it is equal to the InvoiceNum.

For Credit memos where they are not related to an invoice it is also set equal to the credit memo's InvoiceNum. In this later case when InvcHead.Credit = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  """  
      self.RefCancelled:int = obj["RefCancelled"]
      """  Value of this field is reference to invoice which has been cancelled by current invoice.  """  
      self.RefCancelledBy:int = obj["RefCancelledBy"]
      """  Value of this field is reference to invoice that cancelled this invoice.  """  
      self.StartUp:bool = obj["StartUp"]
      """  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  """  
      self.PayDates:str = obj["PayDates"]
      """  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayAmounts:str = obj["PayAmounts"]
      """  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.DocPayAmounts:str = obj["DocPayAmounts"]
      """  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.PayDiscDate:str = obj["PayDiscDate"]
      """  Prompt payment discount date. This is calculated based on the Invoice date + Terms.DiscountDays. Not user maintainable. This will default into the cash receipt record if the scheduled due amount is being paid in full.  """  
      self.PayDiscAmt:int = obj["PayDiscAmt"]
      """  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  """  
      self.DocPayDiscAmt:int = obj["DocPayDiscAmt"]
      """  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  """  
      self.BillConNum:int = obj["BillConNum"]
      """  Contains the key  value for the Billing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMBCON as the default.  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No.  This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  The Manufacturing System sets this flag when creating invoices for order line items which had been flagged for "Time & Material Invoicing" (OrderDtl.TMBilling)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number. If ARSyst.ARVoucherInvoices = Yes then this value will be printed on the Invoice.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal that invoice was posted to.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between invoiced with standard lines which are for parts "PART"  and lines for service calls  "CALL" .  """  
      self.RMANum:int = obj["RMANum"]
      """   The RMA number which generated this Credit Memo.
Note: This only applies to Credit Memos. 
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that the invoice is relate to.  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.CardType:str = obj["CardType"]
      """  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  """  
      self.ExpirationMonth:int = obj["ExpirationMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpirationYear:int = obj["ExpirationYear"]
      """  The expiration year of the credit card.  """  
      self.CardID:str = obj["CardID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External Identifier  """  
      self.XRefInvoiceNum:str = obj["XRefInvoiceNum"]
      """  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.DepGainLoss:int = obj["DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.DNComments:str = obj["DNComments"]
      """  For the Debit Note invoices this field contains the detail comments for the Debit Note. For the regular invoices this field contains the list of Debit Notes related to this invoice.  """  
      self.DNCustNbr:str = obj["DNCustNbr"]
      """  For the Debit Note invoice this field contains A Debit Note number assigned by the customer. The Debit Note number is supposed to be unique for the customer.  """  
      self.DebitNote:bool = obj["DebitNote"]
      """   Indicates the type of documents. Yes = Debit Note. This value can't be changed (the record is created on Invoice payment posting).
Debit Notes  also have the InvoiceSuffix field = "DN".  """  
      self.SoldToCustNum:int = obj["SoldToCustNum"]
      """  This is populated from ShipHead.CustNum representing the Sold To customer.  """  
      self.Consolidated:bool = obj["Consolidated"]
      """  Default is false.  This is only set to true if this invoice was generated via Get Shipments and shipments were combined based on common Bill To customer.  This is used by ARInvoice Entry to properly enable/disable Bill To customer field (InvcHead.CustNum) and to identify the record as a consolidated Invoice.  """  
      self.BillToInvoiceAddress:bool = obj["BillToInvoiceAddress"]
      """  If InvcHead.CustNum (BillTo) is different from InvcHead.SoldToCustNum (SoldTo), then this field defaults to the CustBillTo (Alt BillTo). InvoiceAddress status and SoldToInvoiceAddress is set to the opposite status.  """  
      self.SoldToInvoiceAddress:bool = obj["SoldToInvoiceAddress"]
      """  Always the opposite status of BillToInvoiceAddress.  If true, Invoice address for printing will use the Bill To address on the Sold-to customer.  If false, will use the Bill To address of the Bill to customer.  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Stores the encrypted credit card number  """  
      self.RepComm1:int = obj["RepComm1"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm2:int = obj["RepComm2"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm3:int = obj["RepComm3"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm4:int = obj["RepComm4"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm5:int = obj["RepComm5"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepSales1:int = obj["RepSales1"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales2:int = obj["RepSales2"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales3:int = obj["RepSales3"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales4:int = obj["RepSales4"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales5:int = obj["RepSales5"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.CMType:str = obj["CMType"]
      """  Indicates if the Credit Memo is for a Rebate  """  
      self.CCStreetAddr:str = obj["CCStreetAddr"]
      """  Address used during AVS validation for credit transactions  """  
      self.CCZip:str = obj["CCZip"]
      """  Zip used during AVS validation in credit transactions  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding in Base is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding in Customer currency  """  
      self.Rpt1DepositCredit:int = obj["Rpt1DepositCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2DepositCredit:int = obj["Rpt2DepositCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3DepositCredit:int = obj["Rpt3DepositCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt1PayAmounts:str = obj["Rpt1PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt2PayAmounts:str = obj["Rpt2PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt3PayAmounts:str = obj["Rpt3PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt1PayDiscAmt:int = obj["Rpt1PayDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2PayDiscAmt:int = obj["Rpt2PayDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3PayDiscAmt:int = obj["Rpt3PayDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnpostedBal:int = obj["Rpt1UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnpostedBal:int = obj["Rpt2UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnpostedBal:int = obj["Rpt3UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.DocDepApplied:int = obj["DocDepApplied"]
      """  Amount of deposit applied  """  
      self.Rpt1DepGainLoss:int = obj["Rpt1DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2DepGainLoss:int = obj["Rpt2DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3DepGainLoss:int = obj["Rpt3DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.LastChrgCalcDate:str = obj["LastChrgCalcDate"]
      """  The last date finance/late charges have been calculated for this invoice.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.TotFinChrg:int = obj["TotFinChrg"]
      """  Total Finance Charge amount.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.PayDiscDays:str = obj["PayDiscDays"]
      """  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayDiscPer:str = obj["PayDiscPer"]
      """  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  """  
      self.BlockedFinChrg:bool = obj["BlockedFinChrg"]
      """  Blocks certain invoice from generating finance/later charge.  """  
      self.BlockedFinChrgReason:str = obj["BlockedFinChrgReason"]
      """  Reason why invoice has been blocked generating finance/later charge and only is enabled if the invoice is blocked.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.BlockedRemLetters:bool = obj["BlockedRemLetters"]
      """  Blocks certain invoice from being printed on reminder letters.  """  
      self.PayDiscPartPay:bool = obj["PayDiscPartPay"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.BlockedRemLettersReason:str = obj["BlockedRemLettersReason"]
      """  Reason why invoice has been blocked from being printed on reminder letters and only is enabled if the invoice is blocked.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.CurrRateDate:str = obj["CurrRateDate"]
      """  Currency Rate Date  """  
      self.PIPayment:str = obj["PIPayment"]
      """   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.UseAltBillTo:bool = obj["UseAltBillTo"]
      """  If TRUE taxes will be calculated based on the Alternate Bill To, if FALSE it will proceed normally.  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Will be se to Yes if the Invoice was created by the Correction (Reversing) logic.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code  """  
      self.LockTaxRate:bool = obj["LockTaxRate"]
      """  Locks Tax Rate and allows user to edit the tax exchange rate  """  
      self.SEBankRef:str = obj["SEBankRef"]
      """  Sweden Finland Localization field - Banking Reference  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  Government Uniform Invoice Format Code (Taiwan Localization field)  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  Government Uniform Invoice Deduct Code (Taiwan Localization field)  """  
      self.ReversalDocAmount:int = obj["ReversalDocAmount"]
      """  Reversal Doucment Amount  """  
      self.OrigDueDate:str = obj["OrigDueDate"]
      """  Original Due Date at posting time  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The reference to CashHead.HeadNum.Used in deposit invoices  """  
      self.ARLOCID:str = obj["ARLOCID"]
      """  Letter of Credit ID.  """  
      self.ContractRef:str = obj["ContractRef"]
      """  The free text field which can contain reference (such as Contract)  """  
      self.OurBank:str = obj["OurBank"]
      """  Bank for Cash receipts. For Shipment Invoices it comes from Packing Slip. For Deposit Invoices created based on deposit payments it is actual bank money are received to. For other  Invoice types, default comes from 1) Sales Order 2) Bill To Customer 3) System default (Company).  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Addition to Contract  """  
      self.PBProjectID:str = obj["PBProjectID"]
      """  If the invoice was generated in Project Billing then it is reference to the project.  """  
      self.DepositAmt:int = obj["DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment  """  
      self.GUIExportBillNumber:str = obj["GUIExportBillNumber"]
      """   Taiwan Localization
Export Bill Number  """  
      self.DocDepositAmt:int = obj["DocDepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in document currency  """  
      self.GUIDateOfExport:str = obj["GUIDateOfExport"]
      """   Taiwan Localization
Date of Export  """  
      self.Rpt1DepositAmt:int = obj["Rpt1DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in Rpt1 currency  """  
      self.GUIExportType:str = obj["GUIExportType"]
      """   Taiwan Localization
Export Type  """  
      self.Rpt2DepositAmt:int = obj["Rpt2DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in Rpt2 currency  """  
      self.GUIExportMark:str = obj["GUIExportMark"]
      """   Taiwan Localization
Export Mark  """  
      self.Rpt3DepositAmt:int = obj["Rpt3DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in Rpt23currency  """  
      self.GUIExportBillType:str = obj["GUIExportBillType"]
      """   Taiwan Localization
Export Bill Type  """  
      self.DepUnallocatedAmt:int = obj["DepUnallocatedAmt"]
      """  Deposit unallocated amount in base currency  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  Day when a company sums up accounts receivables for each customer.  """  
      self.DocDepUnallocatedAmt:int = obj["DocDepUnallocatedAmt"]
      """  Deposit unallocated amount in document currency  """  
      self.BillingDate:str = obj["BillingDate"]
      """  Date when a company bills the customer  """  
      self.Rpt1DepUnallocatedAmt:int = obj["Rpt1DepUnallocatedAmt"]
      """  Deposit unallocated amount in Rpt1 currency  """  
      self.BillingNumber:str = obj["BillingNumber"]
      """  Billing Number to be generated from Legal Numbering upon printing of billing statement.  """  
      self.Rpt2DepUnallocatedAmt:int = obj["Rpt2DepUnallocatedAmt"]
      """  Deposit unallocated amount in Rpt2 currency  """  
      self.ReadyToBill:bool = obj["ReadyToBill"]
      """  Only records ready to bill will be printed in the Billing Statement  """  
      self.Rpt3DepUnallocatedAmt:int = obj["Rpt3DepUnallocatedAmt"]
      """  Deposit unallocated amount in Rpt3 currency  """  
      self.OvrDefTaxDate:bool = obj["OvrDefTaxDate"]
      """  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  """  
      self.XRefContractNum:str = obj["XRefContractNum"]
      """  Cross Reference Contract Number.  """  
      self.XRefContractDate:str = obj["XRefContractDate"]
      """  Cross Reference Contract Date.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.CustAgentName:str = obj["CustAgentName"]
      """  Customer Agent Name  """  
      self.CustAgentTaxRegNo:str = obj["CustAgentTaxRegNo"]
      """  Customer Agent Tax Region Number  """  
      self.ExportType:str = obj["ExportType"]
      """  Export Type: 0-No Export, 1-Normal Export(S04), 2-Material Export(S05), 3-Service Export(S06)  """  
      self.ExportReportNo:str = obj["ExportReportNo"]
      """  Export Report Number  """  
      self.RealEstateNo:str = obj["RealEstateNo"]
      """  Real Estate Number  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.CycleCode:str = obj["CycleCode"]
      """  CycleCode  """  
      self.Duration:int = obj["Duration"]
      """  Duration  """  
      self.EndDate:str = obj["EndDate"]
      """  EndDate  """  
      self.MaxValueAmt:int = obj["MaxValueAmt"]
      """  MaxValueAmt  """  
      self.DocMaxValueAmt:int = obj["DocMaxValueAmt"]
      """  DocMaxValueAmt  """  
      self.Rpt1MaxValueAmt:int = obj["Rpt1MaxValueAmt"]
      """  Rpt1MaxValueAmt  """  
      self.Rpt2MaxValueAmt:int = obj["Rpt2MaxValueAmt"]
      """  Rpt2MaxValueAmt  """  
      self.Rpt3MaxValueAmt:int = obj["Rpt3MaxValueAmt"]
      """  Rpt3MaxValueAmt  """  
      self.HoldInvoice:bool = obj["HoldInvoice"]
      """  HoldInvoice  """  
      self.CopyLatestInvoice:bool = obj["CopyLatestInvoice"]
      """  CopyLatestInvoice  """  
      self.OverrideEndDate:bool = obj["OverrideEndDate"]
      """  OverrideEndDate  """  
      self.CycleInactive:bool = obj["CycleInactive"]
      """  CycleInactive  """  
      self.RecurSource:bool = obj["RecurSource"]
      """  RecurSource  """  
      self.InstanceNum:int = obj["InstanceNum"]
      """  InstanceNum  """  
      self.RecurBalance:int = obj["RecurBalance"]
      """  RecurBalance  """  
      self.DocRecurBalance:int = obj["DocRecurBalance"]
      """  DocRecurBalance  """  
      self.Rpt1RecurBalance:int = obj["Rpt1RecurBalance"]
      """  Rpt1RecurBalance  """  
      self.Rpt2RecurBalance:int = obj["Rpt2RecurBalance"]
      """  Rpt2RecurBalance  """  
      self.Rpt3RecurBalance:int = obj["Rpt3RecurBalance"]
      """  Rpt3RecurBalance  """  
      self.LastDate:str = obj["LastDate"]
      """  LastDate  """  
      self.RecurringState:str = obj["RecurringState"]
      """  RecurringState  """  
      self.IsRecurring:bool = obj["IsRecurring"]
      """  IsRecurring  """  
      self.InvoiceNumList:str = obj["InvoiceNumList"]
      """  InvoiceNumList  """  
      self.IsAddedToGTI:bool = obj["IsAddedToGTI"]
      """  IsAddedToGTI  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHISRCodeLine:str = obj["CHISRCodeLine"]
      """  CHISRCodeLine  """  
      self.CMReason:str = obj["CMReason"]
      """  CMReason  """  
      self.THIsImmatAdjustment:bool = obj["THIsImmatAdjustment"]
      """  THIsImmatAdjustment  """  
      self.AGAuthorizationCode:str = obj["AGAuthorizationCode"]
      """  AGAuthorizationCode  """  
      self.AGAuthorizationDate:str = obj["AGAuthorizationDate"]
      """  AGAuthorizationDate  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.AGDocumentLetter:str = obj["AGDocumentLetter"]
      """  AGDocumentLetter  """  
      self.AGInvoicingPoint:str = obj["AGInvoicingPoint"]
      """  AGInvoicingPoint  """  
      self.AGLegalNumber:str = obj["AGLegalNumber"]
      """  AGLegalNumber  """  
      self.AGPrintingControlType:str = obj["AGPrintingControlType"]
      """  AGPrintingControlType  """  
      self.RevisionDate:str = obj["RevisionDate"]
      """  RevisionDate  """  
      self.RevisionNum:int = obj["RevisionNum"]
      """  RevisionNum  """  
      self.TWDeclareYear:int = obj["TWDeclareYear"]
      """  TWDeclareYear  """  
      self.TWDeclarePeriod:int = obj["TWDeclarePeriod"]
      """  TWDeclarePeriod  """  
      self.TWGenerationType:str = obj["TWGenerationType"]
      """  TWGenerationType  """  
      self.TWGUIGroup:str = obj["TWGUIGroup"]
      """  TWGUIGroup  """  
      self.TWPeriodPrefix:str = obj["TWPeriodPrefix"]
      """  TWPeriodPrefix  """  
      self.InvInCollections:bool = obj["InvInCollections"]
      """  Indicates if the Invoice is in Collections status  """  
      self.CollectionsCust:bool = obj["CollectionsCust"]
      """   Indicates if the Customer of the Invoice is in Collections
(Peru Localization)  """  
      self.CounterARForm:int = obj["CounterARForm"]
      """  A counter of the number of times an AR Invoice has been transmitted via EDI.  The counter is automatically incremented each time the EDIReady flag changes from False to True.  """  
      self.PostedRecog:bool = obj["PostedRecog"]
      """  flag indicates if Revenue of the invoice has been already posted  """  
      self.CNConfirmDate:str = obj["CNConfirmDate"]
      """  Confirmation Date  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  MXSATSeal  """  
      self.MXSerie:str = obj["MXSerie"]
      """  MXSerie  """  
      self.MXTaxRcptType:str = obj["MXTaxRcptType"]
      """  MXTaxRcptType  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.MXTotalPayments:int = obj["MXTotalPayments"]
      """  MXTotalPayments  """  
      self.MXFolio:str = obj["MXFolio"]
      """  MXFolio  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  MXCertifiedTimestamp  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  MXSATCertificateSN  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  MXDigitalSeal  """  
      self.MXPostedTimeStamp:str = obj["MXPostedTimeStamp"]
      """  MXPostedTimeStamp  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  MXCertificate  """  
      self.MXApprovalYear:int = obj["MXApprovalYear"]
      """  MXApprovalYear  """  
      self.MXCBB:str = obj["MXCBB"]
      """  MXCBB  """  
      self.MXApprovalNum:int = obj["MXApprovalNum"]
      """  MXApprovalNum  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  MXOriginalStringTFD  """  
      self.MXPaymentNum:int = obj["MXPaymentNum"]
      """  MXPaymentNum  """  
      self.MXPaidAs:str = obj["MXPaidAs"]
      """  MXPaidAs  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  MXCertificateSN  """  
      self.MXOriginalAmount:int = obj["MXOriginalAmount"]
      """  MXOriginalAmount  """  
      self.MXAccountNumber:str = obj["MXAccountNumber"]
      """  MXAccountNumber  """  
      self.MXOriginalDate:str = obj["MXOriginalDate"]
      """  MXOriginalDate  """  
      self.MXOriginalSeries:str = obj["MXOriginalSeries"]
      """  MXOriginalSeries  """  
      self.MXOriginalFolio:str = obj["MXOriginalFolio"]
      """  MXOriginalFolio  """  
      self.MXTaxRegime:str = obj["MXTaxRegime"]
      """  MXTaxRegime  """  
      self.MXOriginalString:str = obj["MXOriginalString"]
      """  MXOriginalString  """  
      self.MXPaymentName:str = obj["MXPaymentName"]
      """  MXPaymentName  """  
      self.EInvoice:bool = obj["EInvoice"]
      """  EInvoice  """  
      self.EInvStatus:int = obj["EInvStatus"]
      """  EInvStatus  """  
      self.EInvTimestamp:str = obj["EInvTimestamp"]
      """  EInvTimestamp  """  
      self.EInvUpdatedBy:str = obj["EInvUpdatedBy"]
      """  EInvUpdatedBy  """  
      self.EInvException:str = obj["EInvException"]
      """  EInvException  """  
      self.WithTaxConfirm:bool = obj["WithTaxConfirm"]
      """  Flagged that this invoice has taxes which were necessary or is necessary now.  """  
      self.UseAltBillToID:bool = obj["UseAltBillToID"]
      """  UseAltBillToID  """  
      self.MXCancelledDate:str = obj["MXCancelledDate"]
      """  MXCancelledDate  """  
      self.Overpaid:bool = obj["Overpaid"]
      """  Overpaid  """  
      self.OrdExchangeRate:int = obj["OrdExchangeRate"]
      """  OrdExchangeRate  """  
      self.PEAPPayNum:int = obj["PEAPPayNum"]
      """  PEAPPayNum  """  
      self.PEBankNumber:str = obj["PEBankNumber"]
      """  PEBankNumber  """  
      self.PECharges:int = obj["PECharges"]
      """  PECharges  """  
      self.PECommissions:int = obj["PECommissions"]
      """  PECommissions  """  
      self.PEDetTaxAmt:int = obj["PEDetTaxAmt"]
      """  PEDetTaxAmt  """  
      self.PEDetTaxCurrencyCode:str = obj["PEDetTaxCurrencyCode"]
      """  PEDetTaxCurrencyCode  """  
      self.PEDischargeAmt:int = obj["PEDischargeAmt"]
      """  PEDischargeAmt  """  
      self.PEDischargeDate:str = obj["PEDischargeDate"]
      """  PEDischargeDate  """  
      self.PEInterest:int = obj["PEInterest"]
      """  PEInterest  """  
      self.PENoPayPenalty:int = obj["PENoPayPenalty"]
      """  PENoPayPenalty  """  
      self.PESUNATDepAmt:int = obj["PESUNATDepAmt"]
      """  CSF Peru - SUNAT Deposit Amount  """  
      self.PESUNATDepDate:str = obj["PESUNATDepDate"]
      """  CSF Peru - SUNAT Deposit Date  """  
      self.PESUNATDepNum:str = obj["PESUNATDepNum"]
      """  CSF Peru -  SUNAT Deposit Number  """  
      self.PEBOEPosted:bool = obj["PEBOEPosted"]
      """  PEBOEPosted  """  
      self.DocPEInterest:int = obj["DocPEInterest"]
      """  DocPEInterest  """  
      self.DocPECommissions:int = obj["DocPECommissions"]
      """  DocPECommissions  """  
      self.DocPECharges:int = obj["DocPECharges"]
      """  DocPECharges  """  
      self.DocPENoPayPenalty:int = obj["DocPENoPayPenalty"]
      """  DocPENoPayPenalty  """  
      self.DocPEDischargeAmt:int = obj["DocPEDischargeAmt"]
      """  DocPEDischargeAmt  """  
      self.DocPEDetTaxAmt:int = obj["DocPEDetTaxAmt"]
      """  DocPEDetTaxAmt  """  
      self.Rpt1PEInterest:int = obj["Rpt1PEInterest"]
      """  Rpt1PEInterest  """  
      self.Rpt1PECommissions:int = obj["Rpt1PECommissions"]
      """  Rpt1PECommissions  """  
      self.Rpt1PECharges:int = obj["Rpt1PECharges"]
      """  Rpt1PECharges  """  
      self.Rpt1PENoPayPenalty:int = obj["Rpt1PENoPayPenalty"]
      """  Rpt1PENoPayPenalty  """  
      self.Rpt1PEDischargeAmt:int = obj["Rpt1PEDischargeAmt"]
      """  Rpt1PEDischargeAmt  """  
      self.Rpt2PEInterest:int = obj["Rpt2PEInterest"]
      """  Rpt2PEInterest  """  
      self.Rpt2PECommissions:int = obj["Rpt2PECommissions"]
      """  Rpt2PECommissions  """  
      self.Rpt2PECharges:int = obj["Rpt2PECharges"]
      """  Rpt2PECharges  """  
      self.Rpt2PENoPayPenalty:int = obj["Rpt2PENoPayPenalty"]
      """  Rpt2PENoPayPenalty  """  
      self.Rpt2PEDischargeAmt:int = obj["Rpt2PEDischargeAmt"]
      """  Rpt2PEDischargeAmt  """  
      self.Rpt3PEInterest:int = obj["Rpt3PEInterest"]
      """  Rpt3PEInterest  """  
      self.Rpt3PECommissions:int = obj["Rpt3PECommissions"]
      """  Rpt3PECommissions  """  
      self.Rpt3PECharges:int = obj["Rpt3PECharges"]
      """  Rpt3PECharges  """  
      self.Rpt3PENoPayPenalty:int = obj["Rpt3PENoPayPenalty"]
      """  Rpt3PENoPayPenalty  """  
      self.Rpt3PEDischargeAmt:int = obj["Rpt3PEDischargeAmt"]
      """  Rpt3PEDischargeAmt  """  
      self.OurSupplierCode:str = obj["OurSupplierCode"]
      """  Our Supplier Code  """  
      self.PEGuaranteeName:str = obj["PEGuaranteeName"]
      """  PEGuaranteeName  """  
      self.PEGuaranteeAddress1:str = obj["PEGuaranteeAddress1"]
      """  PEGuaranteeAddress1  """  
      self.PEGuaranteeAddress2:str = obj["PEGuaranteeAddress2"]
      """  PEGuaranteeAddress2  """  
      self.PEGuaranteeAddress3:str = obj["PEGuaranteeAddress3"]
      """  PEGuaranteeAddress3  """  
      self.PEGuaranteeCity:str = obj["PEGuaranteeCity"]
      """  PEGuaranteeCity  """  
      self.PEGuaranteeState:str = obj["PEGuaranteeState"]
      """  PEGuaranteeState  """  
      self.PEGuaranteeZip:str = obj["PEGuaranteeZip"]
      """  PEGuaranteeZip  """  
      self.PEGuaranteeCountry:str = obj["PEGuaranteeCountry"]
      """  PEGuaranteeCountry  """  
      self.PEGuaranteeTaxID:str = obj["PEGuaranteeTaxID"]
      """  PEGuaranteeTaxID  """  
      self.PEGuaranteePhoneNum:str = obj["PEGuaranteePhoneNum"]
      """  PEGuaranteePhoneNum  """  
      self.PEBOEStatus:str = obj["PEBOEStatus"]
      """  PEBOEStatus  """  
      self.PEBOEIsMultiGen:bool = obj["PEBOEIsMultiGen"]
      """  PEBOEIsMultiGen  """  
      self.PERefDocID:str = obj["PERefDocID"]
      """  PE Reference Document ID  """  
      self.PEReasonCode:str = obj["PEReasonCode"]
      """  PE Reason Code  """  
      self.PEReasonDesc:str = obj["PEReasonDesc"]
      """  PE Reason Description  """  
      self.TWGUIRegNumSeller:str = obj["TWGUIRegNumSeller"]
      """  TW GUI Code Seller  """  
      self.TWGUIRegNumBuyer:str = obj["TWGUIRegNumBuyer"]
      """  TW GUI Code Buyer  """  
      self.TWGUIExportDocumentName:str = obj["TWGUIExportDocumentName"]
      """  Document Name  """  
      self.TWGUIExportRemarks:str = obj["TWGUIExportRemarks"]
      """  Remarks  """  
      self.TWGUIExportVerification:str = obj["TWGUIExportVerification"]
      """  Verification  """  
      self.PEDebitNoteReasonCode:str = obj["PEDebitNoteReasonCode"]
      """  PEDebitNoteReasonCode  """  
      self.PEDebitNote:bool = obj["PEDebitNote"]
      """  PEDebitNote  """  
      self.MXPartPmt:bool = obj["MXPartPmt"]
      """  MXPartPmt  """  
      self.CNTaxInvoiceType:int = obj["CNTaxInvoiceType"]
      """  Tax Invoice Type  """  
      self.MXExportOperationType:str = obj["MXExportOperationType"]
      """  MXExportOperationType  """  
      self.MXExportCustDocCode:str = obj["MXExportCustDocCode"]
      """  MXExportCustDocCode  """  
      self.MXExportCertOriginNum:str = obj["MXExportCertOriginNum"]
      """  MXExportCertOriginNum  """  
      self.MXExportConfNum:str = obj["MXExportConfNum"]
      """  MXExportConfNum  """  
      self.MXExportCertOrigin:bool = obj["MXExportCertOrigin"]
      """  MXExportCertOrigin  """  
      self.MXIncoterm:str = obj["MXIncoterm"]
      """  MXIncoterm  """  
      self.AGDocConcept:int = obj["AGDocConcept"]
      """  AGDocConcept  """  
      self.EInvRefNum:str = obj["EInvRefNum"]
      """  Electronic Invoice reference number  """  
      self.ExportDocRefNum:str = obj["ExportDocRefNum"]
      """  Export document reference number  """  
      self.ExportDocDate:str = obj["ExportDocDate"]
      """  Export document date  """  
      self.INTaxTransactionID:str = obj["INTaxTransactionID"]
      """  Tax Transaction ID  """  
      self.MXMovingReasonFlag:bool = obj["MXMovingReasonFlag"]
      """  MXMovingReasonFlag  """  
      self.MXMovingReason:str = obj["MXMovingReason"]
      """  MXMovingReason  """  
      self.MXNumRegIdTrib:str = obj["MXNumRegIdTrib"]
      """  MXNumRegIdTrib  """  
      self.MXResidenCountryNum:int = obj["MXResidenCountryNum"]
      """  MXResidenCountryNum  """  
      self.MXPurchaseType:str = obj["MXPurchaseType"]
      """  MXPurchaseType  """  
      self.MXConfirmationCode:str = obj["MXConfirmationCode"]
      """  MXConfirmationCode  """  
      self.MXExternalCode:str = obj["MXExternalCode"]
      """  MXExternalCode  """  
      self.ServiceInvoice:bool = obj["ServiceInvoice"]
      """  This invoice was created via an integration with a third-party field service.  """  
      self.MXDomesticTransfer:bool = obj["MXDomesticTransfer"]
      """  MXDomesticTransfer  """  
      self.MXCancellationMode:str = obj["MXCancellationMode"]
      """  MXCancellationMode  """  
      self.INShippingPortCode:str = obj["INShippingPortCode"]
      """  Shipping Port Code  """  
      self.INExportProcedure:str = obj["INExportProcedure"]
      """  Export Procedure  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.DigitalSignature:str = obj["DigitalSignature"]
      """  DigitalSignature  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.FirstPrintDate:str = obj["FirstPrintDate"]
      """  FirstPrintDate  """  
      self.DocCopyNum:int = obj["DocCopyNum"]
      """  DocCopyNum  """  
      self.DepositBalance:int = obj["DepositBalance"]
      """  DepositBalance  """  
      self.DocDepositBalance:int = obj["DocDepositBalance"]
      """  DocDepositBalance  """  
      self.Rpt1DepositBalance:int = obj["Rpt1DepositBalance"]
      """  Rpt1DepositBalance  """  
      self.Rpt2DepositBalance:int = obj["Rpt2DepositBalance"]
      """  Rpt2DepositBalance  """  
      self.Rpt3DepositBalance:int = obj["Rpt3DepositBalance"]
      """  Rpt3DepositBalance  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this invoice record is associated with.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case related to this invoice.  """  
      self.CreditOverride:bool = obj["CreditOverride"]
      """  Indicates that the credit hold was overridden for this invoice.  """  
      self.CreditOverrideDate:str = obj["CreditOverrideDate"]
      """  Description	Indicates that the credit hold was overridden for this invoice.	The date and time the user override the invoice credit hold.  """  
      self.CreditOverrideUserID:str = obj["CreditOverrideUserID"]
      """  The user id that override the invoice credit hold.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates the invoice is on credit hold.  Applicable to miscellaneous invoices only.  """  
      self.PEXMLType:int = obj["PEXMLType"]
      """  Peru Electronic Invoice XML Type  """  
      self.COCreditMemoReasonCode:str = obj["COCreditMemoReasonCode"]
      """  COCreditMemoReasonCode  """  
      self.CODebitMemoReasonCode:str = obj["CODebitMemoReasonCode"]
      """  CODebitMemoReasonCode  """  
      self.COReasonDesc:str = obj["COReasonDesc"]
      """  COReasonDesc  """  
      self.CODebitNote:bool = obj["CODebitNote"]
      """  CODebitNote  """  
      self.PEDetractionTranNum:int = obj["PEDetractionTranNum"]
      """  PEDetractionTranNum  """  
      self.PEProductCode:str = obj["PEProductCode"]
      """  PEProductCode  """  
      self.PECollectionGroupID:str = obj["PECollectionGroupID"]
      """  PECollectionGroupID  """  
      self.PECaptionCode:str = obj["PECaptionCode"]
      """  PE Caption Code  """  
      self.PECaption:str = obj["PECaption"]
      """  PE Caption Code Description  """  
      self.PERefDocumentType:str = obj["PERefDocumentType"]
      """  PE Reference DocumentType 1  """  
      self.PERefDocumentNumber:str = obj["PERefDocumentNumber"]
      """  PE Reference Document Number 1  """  
      self.PEDetrGoodServiceCode:str = obj["PEDetrGoodServiceCode"]
      """  PE Detraction good or service code  """  
      self.PERefDocumentType2:str = obj["PERefDocumentType2"]
      """  PE Reference DocumentType 2  """  
      self.PERefDocumentType3:str = obj["PERefDocumentType3"]
      """  PE Reference DocumentType 3  """  
      self.PERefDocumentType4:str = obj["PERefDocumentType4"]
      """  PE Reference DocumentType 4  """  
      self.PERefDocumentType5:str = obj["PERefDocumentType5"]
      """  PE Reference DocumentType 5  """  
      self.PERefDocumentNumber2:str = obj["PERefDocumentNumber2"]
      """  PE Reference Document Number 2  """  
      self.PERefDocumentNumber3:str = obj["PERefDocumentNumber3"]
      """  PE Reference Document Number 3  """  
      self.PERefDocumentNumber4:str = obj["PERefDocumentNumber4"]
      """  PE Reference Document Number 4  """  
      self.PERefDocumentNumber5:str = obj["PERefDocumentNumber5"]
      """  PE Reference Document Number 5  """  
      self.ELIEInvoice:bool = obj["ELIEInvoice"]
      """  E-invoice  """  
      self.ELIEInvStatus:int = obj["ELIEInvStatus"]
      """  Status of E-invoice (1 - Open, 2 - Generated, 3 - Sent, 4 - Error).  """  
      self.ELIEInvUpdatedBy:str = obj["ELIEInvUpdatedBy"]
      """  User Id of the person generated E-invoice.  """  
      self.ELIEInvException:str = obj["ELIEInvException"]
      """  E-invoice error description.  """  
      self.ELIEInvUpdatedOn:str = obj["ELIEInvUpdatedOn"]
      """  Date and Time of E-invoice generation.  """  
      self.COOperType:str = obj["COOperType"]
      """  COOperType  """  
      self.CentralCollection:bool = obj["CentralCollection"]
      """  Flag that indicates if the Invoice is for Central Collection.  """  
      self.CColChildCompany:str = obj["CColChildCompany"]
      """  Company that created this invoice.  """  
      self.CColParentCompany:str = obj["CColParentCompany"]
      """  Central Collection company.  """  
      self.CColOrderNum:int = obj["CColOrderNum"]
      """  Order number on the invoicing company.  """  
      self.CColChildInvoiceNum:int = obj["CColChildInvoiceNum"]
      """  Invoice number on the invoicing company.  """  
      self.CColInvoiceNum:int = obj["CColInvoiceNum"]
      """  Invoice number on central collection company  """  
      self.CColChildLegalNumber:str = obj["CColChildLegalNumber"]
      """  Legal number on the invoicing company invoice.  """  
      self.CColLegalNumber:str = obj["CColLegalNumber"]
      """  Legal number on central collection company.  """  
      self.CColInvoiceRef:int = obj["CColInvoiceRef"]
      """  Invoice reference on the Invoicing Company.  """  
      self.CColInvBal:int = obj["CColInvBal"]
      """  Invoice Balance in the Central Collection company.  """  
      self.DocCColInvBal:int = obj["DocCColInvBal"]
      """  Central Collection Doc Invoice Balance.  """  
      self.CColInvAmt:int = obj["CColInvAmt"]
      """  Invoice Amount on the Invoicing Company.  """  
      self.DocCColInvAmt:int = obj["DocCColInvAmt"]
      """  Invoice Amount on the Invoicing Company.  """  
      self.Rpt1CColInvBal:int = obj["Rpt1CColInvBal"]
      """  Rpt 1 Parent Invoice Balance  """  
      self.Rpt2CColInvBal:int = obj["Rpt2CColInvBal"]
      """  Rpt 2 Parent Invoice Balance  """  
      self.Rpt3CColInvBal:int = obj["Rpt3CColInvBal"]
      """  Rpt 3 Parent Invoice Balance  """  
      self.Rpt1CColInvAmt:int = obj["Rpt1CColInvAmt"]
      """  Rpt 1 Child Invoice Amount  """  
      self.Rpt2CColInvAmt:int = obj["Rpt2CColInvAmt"]
      """  Rpt 2 Child Invoice Amount  """  
      self.Rpt3CColInvAmt:int = obj["Rpt3CColInvAmt"]
      """  Rpt 3 Child Invoice Amount  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.ELIEInvTerminalName:str = obj["ELIEInvTerminalName"]
      """  User terminal name  """  
      self.ELIEInvTerminalIP:str = obj["ELIEInvTerminalIP"]
      """  User terminal IP  """  
      self.Description:str = obj["Description"]
      """  GL Description  """  
      self.WithholdAcctToInterim:bool = obj["WithholdAcctToInterim"]
      """  WithholdAcctToInterim  """  
      self.CColOpenInvoice:bool = obj["CColOpenInvoice"]
      """  Indicates if the Central Collection parent invoice is open.  """  
      self.AGQRCodeData:str = obj["AGQRCodeData"]
      """  AGQRCodeData  """  
      self.ExemptReasonCode:str = obj["ExemptReasonCode"]
      """  Exempt Reason Code  """  
      self.ELIEInvID:str = obj["ELIEInvID"]
      """  EInvoice ID  """  
      self.CallNum:int = obj["CallNum"]
      """  this is a link to the service call that this invoice is for.  Linetype = "CALL"  """  
      self.CallLine:int = obj["CallLine"]
      """  this is a link to the service call line that this invoice is for.  Linetype = "CALL"  """  
      self.JobNum:str = obj["JobNum"]
      """  Associates the Call Line record back its linked jobnum  """  
      self.MXCancelReasonCode:str = obj["MXCancelReasonCode"]
      """  MXCancelReasonCode  """  
      self.MXSubstInvoiceNum:int = obj["MXSubstInvoiceNum"]
      """  MXSubstInvoiceNum  """  
      self.MXExportType:str = obj["MXExportType"]
      """  MXExportType  """  
      self.MXGlobalInvoicePeriod:str = obj["MXGlobalInvoicePeriod"]
      """  MXGlobalInvoicePeriod  """  
      self.MXGlobalInvoiceMonth:str = obj["MXGlobalInvoiceMonth"]
      """  MXGlobalInvoiceMonth  """  
      self.ELIEInvServiceProviderStatus:int = obj["ELIEInvServiceProviderStatus"]
      """  ELIEInvServiceProviderStatus  """  
      self.IncotermCode:str = obj["IncotermCode"]
      """  Incoterm Code  """  
      self.IncotermLocation:str = obj["IncotermLocation"]
      """  Incoterm Location  """  
      self.CovenantDiscPercent:int = obj["CovenantDiscPercent"]
      """  CovenantDiscPercent  """  
      self.TotalCovenantDiscount:int = obj["TotalCovenantDiscount"]
      """  TotalCovenantDiscount  """  
      self.DocCovenantDiscount:int = obj["DocCovenantDiscount"]
      """  DocCovenantDiscount  """  
      self.Rpt1CovenantDiscount:int = obj["Rpt1CovenantDiscount"]
      """  Rpt1CovenantDiscount  """  
      self.Rpt2CovenantDiscount:int = obj["Rpt2CovenantDiscount"]
      """  Rpt2CovenantDiscount  """  
      self.Rpt3CovenantDiscount:int = obj["Rpt3CovenantDiscount"]
      """  Rpt3CovenantDiscount  """  
      self.TotalInCovenantDiscount:int = obj["TotalInCovenantDiscount"]
      """  TotalInCovenantDiscount  """  
      self.AdjustAmtTax:int = obj["AdjustAmtTax"]
      self.AllocAmount:int = obj["AllocAmount"]
      """  This new column should enable the user to enter a draft payment amount ? a part of the check amount that is to be allocated to the invoice  """  
      self.DocInCovenantDiscount:int = obj["DocInCovenantDiscount"]
      """  DocInCovenantDiscount  """  
      self.AllowNegativeWriteOff:bool = obj["AllowNegativeWriteOff"]
      """  Indicates that negative Write Off could be applied for AR Invoices.  """  
      self.Rpt1InCovenantDiscount:int = obj["Rpt1InCovenantDiscount"]
      """  Rpt1InCovenantDiscount  """  
      self.Rpt2InCovenantDiscount:int = obj["Rpt2InCovenantDiscount"]
      """  Rpt2InCovenantDiscount  """  
      self.AllowOverpaidInv:bool = obj["AllowOverpaidInv"]
      """  Indicates that AR Invoices can be overpaid.  """  
      self.AmountDue:int = obj["AmountDue"]
      """  Amount of the next schedule due. This amount is calculated based on the Cash Receipt Transaction Apply Date and the Due Dates of each payment of the Payment Schedule of the invoice.  """  
      self.Rpt3InCovenantDiscount:int = obj["Rpt3InCovenantDiscount"]
      """  Rpt3InCovenantDiscount  """  
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      """  when InvcHead.PIPayment = O then populate ARPaymentInstrumentID with a value of PI.  """  
      self.CalcDocUnpostedBal:int = obj["CalcDocUnpostedBal"]
      """  Calculates the revised invoice balance after specifying an allocated amount.  """  
      self.CashApplied:int = obj["CashApplied"]
      """  This column should display the Allocated amount less Discount amount (automatically calculated).  """  
      self.CurrDecGeneral:int = obj["CurrDecGeneral"]
      """  Currency Decimals General  """  
      self.DepBal:int = obj["DepBal"]
      """  Deposit balance from CashHed  """  
      self.Discount:int = obj["Discount"]
      """  This new column should display payment discount amounts for invoices that are still within discount terms  """  
      self.DiscountApplicable:bool = obj["DiscountApplicable"]
      """  Flags in this new column should mark invoices that are still within discount terms  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      self.DispBalDN:int = obj["DispBalDN"]
      """  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  """  
      self.DisplayCurrencyID:str = obj["DisplayCurrencyID"]
      self.DNPmtAmt:int = obj["DNPmtAmt"]
      """  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  """  
      self.DocTotalDN:int = obj["DocTotalDN"]
      """  Total Debit Notes applied  """  
      self.DspDepBal:int = obj["DspDepBal"]
      """  Display deposit balance.  """  
      self.DspDocDepBal:int = obj["DspDocDepBal"]
      """  Display document deposit balance  """  
      self.DspDocInvoiceAmt:int = obj["DspDocInvoiceAmt"]
      """  Display document invoice amount  """  
      self.DspDocInvoiceBal:int = obj["DspDocInvoiceBal"]
      """  Display document invoice balance  """  
      self.DspInvoiceAmt:int = obj["DspInvoiceAmt"]
      """  Display invoice amount  """  
      self.DspInvoiceBal:int = obj["DspInvoiceBal"]
      """  Display Invoice Balance.  """  
      self.ERSInvoice:bool = obj["ERSInvoice"]
      """  It will be displayed to identify invoices automatically generated due ERS shipments.  """  
      self.InvcNegBal:bool = obj["InvcNegBal"]
      """  Invoice with negative balance.  """  
      self.InvcSelected:bool = obj["InvcSelected"]
      """  Flags in this new column should mark invoices that are selected to be applied to the check  """  
      self.IsDiscountforCreditM:bool = obj["IsDiscountforCreditM"]
      self.ManAddTaxesExist:bool = obj["ManAddTaxesExist"]
      """  Set to true if Manually added taxes exist  """  
      self.NextDiscDate:str = obj["NextDiscDate"]
      """  This field is to display in Cash Receipt Entry the Discount Date that the payment will take.  """  
      self.OriginalDiscount:int = obj["OriginalDiscount"]
      """  The original discount amount.  Used when manual taxes were added, in which case amounts cannot be changed.  The discount applied in this case must be the same as the orignal discoun  """  
      self.PackSlipNum:int = obj["PackSlipNum"]
      """  Pack slip number from the 1st line item.  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  Sold to customer id  """  
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  Sold to customer name.  """  
      self.TaxableWriteOff:bool = obj["TaxableWriteOff"]
      """  Taxable Write Off  """  
      self.WithholdTaxCalcPay:bool = obj["WithholdTaxCalcPay"]
      """  Indicates if the invoice has withholding tax calculated at full or partial payment  """  
      self.WriteOff:bool = obj["WriteOff"]
      """  Write Off  """  
      self.WriteOffAccount:str = obj["WriteOffAccount"]
      """  Write Off Account  """  
      self.WriteOffAccountDesc:str = obj["WriteOffAccountDesc"]
      """  Write Off Account Description  """  
      self.WriteOffAmount:int = obj["WriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffComment:str = obj["WriteOffComment"]
      """  Allows uset to enter comment for Write Off.  """  
      self.DocDepBal:int = obj["DocDepBal"]
      """  Document deposit amount from cashhead.  """  
      self.DocDispBalDN:int = obj["DocDispBalDN"]
      """  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  """  
      self.DocDNPmtAmt:int = obj["DocDNPmtAmt"]
      """  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  """  
      self.WhInterimAdj:int = obj["WhInterimAdj"]
      """  The adjustment  to  allocate amount  in case of WH taxes are posted through interim account for AR Invoice.  """  
      self.Apply:bool = obj["Apply"]
      """  Technical field not for display. Flag determine applied invoice or not.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARInvcAllocTGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  InvoiceNum of ARInvcAlloc  """  
      self.Apply:bool = obj["Apply"]
      """  Technical field not for display. Flag determine applied invoice or not.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARInvcAllocTableset:
   def __init__(self, obj):
      self.ARInvcAlloc:list[Erp_Tablesets_ARInvcAllocRow] = obj["ARInvcAlloc"]
      self.ARInvcAllocTGLC:list[Erp_Tablesets_ARInvcAllocTGLCRow] = obj["ARInvcAllocTGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CDTaxDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this tax detail.  This is assigned by the system.
Values can be; AR, AP.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.APTranNo:int = obj["APTranNo"]
      """  Integer assigned by the system copied from APTran.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice. Manually entered if the currency is the base currency.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. Manually entered if the currency is the base currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency. Manually entered.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Reverse Charge.  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution Date  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Tax Rate Date  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.Rpt1DefTaxableAmt:int = obj["Rpt1DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxableAmt:int = obj["Rpt2DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxableAmt:int = obj["Rpt3DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.DefTaxAmt:int = obj["DefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.DocDefTaxAmt:int = obj["DocDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.Rpt1DefTaxAmt:int = obj["Rpt1DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxAmt:int = obj["Rpt2DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxAmt:int = obj["Rpt3DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Relates record to a BankAcct.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID of the Transaction.  """  
      self.DedTaxAmt:int = obj["DedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.DocDedTaxAmt:int = obj["DocDedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.Rpt1DedTaxAmt:int = obj["Rpt1DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DedTaxAmt:int = obj["Rpt2DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DedTaxAmt:int = obj["Rpt3DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.FixedAmount:int = obj["FixedAmount"]
      """  Fixed Tax Amount  """  
      self.DocFixedAmount:int = obj["DocFixedAmount"]
      """  Document Fixed Tax Amount  """  
      self.Rpt1FixedAmount:int = obj["Rpt1FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2FixedAmount:int = obj["Rpt2FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3FixedAmount:int = obj["Rpt3FixedAmount"]
      """  Reporting currency value of this field  """  
      self.DiscTaxAdj:int = obj["DiscTaxAdj"]
      """  Discount Tax Adjustment  """  
      self.DocDiscTaxAdj:int = obj["DocDiscTaxAdj"]
      """  Discount Tax Adjustment in foreign currency.  """  
      self.Rpt1DiscTaxAdj:int = obj["Rpt1DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxAdj:int = obj["Rpt2DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxAdj:int = obj["Rpt3DiscTaxAdj"]
      """  Reporting currency value of this field  """  
      self.DiscTaxableAdj:int = obj["DiscTaxableAdj"]
      """  Discount Taxable Adjustment  """  
      self.DocDiscTaxableAdj:int = obj["DocDiscTaxableAdj"]
      """  Discount Taxable Adjustment in foreign currency.  """  
      self.Rpt1DiscTaxableAdj:int = obj["Rpt1DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxableAdj:int = obj["Rpt2DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxableAdj:int = obj["Rpt3DiscTaxableAdj"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates if transaction was voided.  The rest of the unique key will contain the original transaction values (like APTran)  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DiscTaxAdjVar:int = obj["DiscTaxAdjVar"]
      """  Discount Tax Adjustment Variance  """  
      self.DocDiscTaxAdjVar:int = obj["DocDiscTaxAdjVar"]
      """  Discount Tax Adjustment Variance  """  
      self.Rpt1DiscTaxAdjVar:int = obj["Rpt1DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscTaxAdjVar:int = obj["Rpt2DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscTaxAdjVar:int = obj["Rpt3DiscTaxAdjVar"]
      """  Reporting currency value of this field  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGOrigTaxableAmt:int = obj["AGOrigTaxableAmt"]
      """  AGOrigTaxableAmt  """  
      self.GainLoss:int = obj["GainLoss"]
      """  GainLoss  """  
      self.DocGainLoss:int = obj["DocGainLoss"]
      """  DocGainLoss  """  
      self.Rpt1GainLoss:int = obj["Rpt1GainLoss"]
      """  Rpt1GainLoss  """  
      self.Rpt2GainLoss:int = obj["Rpt2GainLoss"]
      """  Rpt2GainLoss  """  
      self.Rpt3GainLoss:int = obj["Rpt3GainLoss"]
      """  Rpt3GainLoss  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  APInvoiceNum  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.GroupID:str = obj["GroupID"]
      """  Group ID - used to link to Cash Head  """  
      self.CTDescription:str = obj["CTDescription"]
      self.DisableManual:bool = obj["DisableManual"]
      """  Flag to indicate if Manual checkbox should be Read Only  """  
      self.EnableTax:bool = obj["EnableTax"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "Group" to which is transaction is assigned. This is not user maintainable. It is duplicated from the corresponding CashHead record.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The foreign key that relates this detail record to a CashHead record. Duplicated from CashHead.HeadNum when record is created. Not applicable to user interface.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.TranType:str = obj["TranType"]
      """   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction cannot be maintained; it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted to the General Ledger Module.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date. Duplicated from the CashBatc.TranDate. Not user maintainable. This is refreshed as part of the post process.  """  
      self.CheckRef:str = obj["CheckRef"]
      """   The customer's Check number of the receipt transaction. Duplicated from CashHead.CheckRef. This is a mandatory field used only for Cash Receipt type of translations.  Primarily used as a reference. The only validation is that it can't be blank.
This is used when TranType = PrePay, MisPay or PayInv.  """  
      self.TranAmt:int = obj["TranAmt"]
      """   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.
For records based in Debit Note applied  it carries a negative sign.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction, it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  """  
      self.Discount:int = obj["Discount"]
      """   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  """  
      self.Comment:str = obj["Comment"]
      """  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adjust".  """  
      self.Reference:str = obj["Reference"]
      """  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this CashDtl, only differs from cashead when the invoice is locked.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.DebitNote:bool = obj["DebitNote"]
      """  The internally set flag to indicate if this detail line of the Cash payment is Debit Note type.  """  
      self.DNComments:str = obj["DNComments"]
      """  Debit Note Detail Comments.  """  
      self.DNAmount:int = obj["DNAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DocDnAmount:int = obj["DocDnAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DNCustNbr:str = obj["DNCustNbr"]
      """  The Debit Note Number assigned by the customer.  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding difference arises when invoice in one currency are settled in another currency  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1DnAmount:int = obj["Rpt1DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2DnAmount:int = obj["Rpt2DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3DnAmount:int = obj["Rpt3DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.TaxReceiptDate:str = obj["TaxReceiptDate"]
      """  Tax Receipt Date (Thailand Localization)  """  
      self.TaxReceiptNo:str = obj["TaxReceiptNo"]
      """  Tax Receipt No. (Thailand Localization)  """  
      self.WHTCertificateDate:str = obj["WHTCertificateDate"]
      """  Withholding Tax Certificate Date  (Thailand Localization)  """  
      self.WHTCertificateNo:str = obj["WHTCertificateNo"]
      """  Withholding Tax Certificate No. (Thailand Localization)  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  Invoice Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Invoice Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.TaxRemarks:str = obj["TaxRemarks"]
      """  Tax Remarks  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.SEPADDMsgID:str = obj["SEPADDMsgID"]
      """  SEPADDMsgID  """  
      self.SEPADDPmtID:str = obj["SEPADDPmtID"]
      """  SEPADDPmtID  """  
      self.PmtDueDate:str = obj["PmtDueDate"]
      """  PmtDueDate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.MXPaymentNum:int = obj["MXPaymentNum"]
      """  MX Payment Number for AR Invoice  """  
      self.WriteOffHeadNumRef:int = obj["WriteOffHeadNumRef"]
      """  Reference to HeadNum of main CashHead record.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  EpicorFSA  """  
      self.TaxableAdjustment:bool = obj["TaxableAdjustment"]
      """  Taxable Adjustment  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BaseAdjAmt:int = obj["BaseAdjAmt"]
      """  Adjustment amount in Base Currency  """  
      self.BaseCurrDesc:str = obj["BaseCurrDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.BillConNum:int = obj["BillConNum"]
      """  The Billing Contact Number.  Obtained from InvcHead.BillConNum.  """  
      self.CopyRate:bool = obj["CopyRate"]
      """  If this flag is true the AR Invoice exchange rates is used when the Adjustment is applied and no currency Gain/Loss is calculated  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Indicates if invoice related to  this detail line is Correction invoice with negatice balance  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyDescription:str = obj["CurrencyDescription"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol  """  
      self.DebitNotesApplied:str = obj["DebitNotesApplied"]
      """  This field displays all Debit Note customer defined numbers applied.  """  
      self.DispDocSelfAssessAmt:int = obj["DispDocSelfAssessAmt"]
      self.DispDocWithholdAmt:int = obj["DispDocWithholdAmt"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display gl account  """  
      self.DispSelfAssessAmt:int = obj["DispSelfAssessAmt"]
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DispWithholdAmt:int = obj["DispWithholdAmt"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Doc Invoice Amount  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Doc Invoice Balance  """  
      self.DocNetCash:int = obj["DocNetCash"]
      self.DocNewBalance:int = obj["DocNewBalance"]
      """  Doc New Invoice Balance  """  
      self.DocWriteOffAmount:int = obj["DocWriteOffAmount"]
      """  Write Off Amount  """  
      self.DsblCopyRate:bool = obj["DsblCopyRate"]
      """  If this flag is true then CopyRate checkbox is Read Only  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Legal Number Field  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Legal Number Field  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  """  
      self.GainLossAmt:int = obj["GainLossAmt"]
      self.GLRefCodeDesc:str = obj["GLRefCodeDesc"]
      """  G/L Reference Code Description  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Legal Number Field  """  
      self.InvDiscountDate:str = obj["InvDiscountDate"]
      self.InvDueDate:str = obj["InvDueDate"]
      self.InvExchRate:int = obj["InvExchRate"]
      """  Invoice Exchange Rate  """  
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      self.InvLockRate:bool = obj["InvLockRate"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Invoice Amount  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoice Balance  """  
      self.InvTermsCode:str = obj["InvTermsCode"]
      self.InvXRateLabel:str = obj["InvXRateLabel"]
      self.IsCreditPayment:bool = obj["IsCreditPayment"]
      """  This flag is used to differentiate between a normal Invoice Credit Memo and a Credit Payment.  """  
      self.IsDiscountforCreditM:bool = obj["IsDiscountforCreditM"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      self.NetCash:int = obj["NetCash"]
      self.NewBalance:int = obj["NewBalance"]
      """  New Invoice Balance  """  
      self.OldGainLoss:int = obj["OldGainLoss"]
      self.OrderNum:int = obj["OrderNum"]
      """  The related order number (InvcHead.OrderNum)  """  
      self.PNRef:str = obj["PNRef"]
      """  Processing company's Reference ID, unique to each transaction  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions  """  
      self.RecalcTranAmt:bool = obj["RecalcTranAmt"]
      """  Whether to recalculate the CashDtl.TranAmt and all related columns prior to saving.  """  
      self.RedStornoOpt:str = obj["RedStornoOpt"]
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.RemoveForAdjustment:bool = obj["RemoveForAdjustment"]
      """  This will indicate the information on this CashDtl record will not be included in the Cash Receipt Adjustment.  """  
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt1GainLossAmt:int = obj["Rpt1GainLossAmt"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt1NetCash:int = obj["Rpt1NetCash"]
      self.Rpt1NewBalance:int = obj["Rpt1NewBalance"]
      self.Rpt1OldGainLoss:int = obj["Rpt1OldGainLoss"]
      self.Rpt1WriteOffAmount:int = obj["Rpt1WriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt1WriteOffGainLossAmt:int = obj["Rpt1WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt2GainLossAmt:int = obj["Rpt2GainLossAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt2NetCash:int = obj["Rpt2NetCash"]
      self.Rpt2NewBalance:int = obj["Rpt2NewBalance"]
      self.Rpt2OldGainLoss:int = obj["Rpt2OldGainLoss"]
      self.Rpt2WriteOffAmount:int = obj["Rpt2WriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt2WriteOffGainLossAmt:int = obj["Rpt2WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt3GainLossAmt:int = obj["Rpt3GainLossAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.Rpt3NetCash:int = obj["Rpt3NetCash"]
      self.Rpt3NewBalance:int = obj["Rpt3NewBalance"]
      self.Rpt3OldGainLoss:int = obj["Rpt3OldGainLoss"]
      self.Rpt3WriteOffAmount:int = obj["Rpt3WriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt3WriteOffGainLossAmt:int = obj["Rpt3WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  CustID associated with CashDtl.SoldToCustNum  """  
      self.SoldToCustNum:int = obj["SoldToCustNum"]
      """  Populated from InvcHead.SoldToCustNum.  """  
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  CustName associated with CashDtl.SoldToCustNum  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  Legal Number Field  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Description of the Tran Type  """  
      self.Type:str = obj["Type"]
      """  This field shows if this CashDtl line is 'Debit Note' type , created as a result of Debit Note(s) applied.  """  
      self.WriteOff:bool = obj["WriteOff"]
      """  Write Off  """  
      self.WriteOffAccount:str = obj["WriteOffAccount"]
      """  Write Off Account  """  
      self.WriteOffAccountDesc:str = obj["WriteOffAccountDesc"]
      """  Write Off Account Description  """  
      self.WriteOffAmount:int = obj["WriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffGainLossAmt:int = obj["WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.XRateLabel:str = obj["XRateLabel"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Legal Number Field  """  
      self.OldWriteOffAmount:int = obj["OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffAccountDisp:str = obj["WriteOffAccountDisp"]
      self.TaxableWriteOff:bool = obj["TaxableWriteOff"]
      self.TotalGainLossAmt:int = obj["TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.OldWriteOffGainLossAmt:int = obj["OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt1OldWriteOffGainLossAmt:int = obj["Rpt1OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt2OldWriteOffGainLossAmt:int = obj["Rpt2OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt3OldWriteOffGainLossAmt:int = obj["Rpt3OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt1TotalGainLossAmt:int = obj["Rpt1TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.Rpt2TotalGainLossAmt:int = obj["Rpt2TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.Rpt3TotalGainLossAmt:int = obj["Rpt3TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.DocOldWriteOffAmount:int = obj["DocOldWriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt1OldWriteOffAmount:int = obj["Rpt1OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt2OldWriteOffAmount:int = obj["Rpt2OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt3OldWriteOffAmount:int = obj["Rpt3OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffComment:str = obj["WriteOffComment"]
      """  Allows uset to enter comment for Write Off.  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.ReferenceTranDate:str = obj["ReferenceTranDate"]
      self.ReferenceTranNum:int = obj["ReferenceTranNum"]
      self.ReferenceTranTime:int = obj["ReferenceTranTime"]
      self.EnableManualWHTax:bool = obj["EnableManualWHTax"]
      """  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  """  
      self.WHTaxManualChange:bool = obj["WHTaxManualChange"]
      """  Indicates if the withholding amount tax was manually modified.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.InvoiceNumInvoiceType:str = obj["InvoiceNumInvoiceType"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Displays the ID of the group the transaction is assigned to.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Displays the receipt header number used for internal reference.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.TranType:str = obj["TranType"]
      """  Displays the transaction type.  """  
      self.CheckRef:str = obj["CheckRef"]
      """  Displays the number of the check.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Displays the transaction amount.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Displays the transaction amount in customer currency.  """  
      self.CustID:str = obj["CustID"]
      """  Displays the customer ID.  """  
      self.TranDate:str = obj["TranDate"]
      """  Displays the date of the transaction.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  """  
      self.UnAppliedAmt:int = obj["UnAppliedAmt"]
      """  Displays the unapplied amount.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Displays the unapplied amount in base currency.  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Displays the amount applied to invoices.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Displays the amount in document currency applied to invoices.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Displays the fiscal year that the check is posted to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Displays the fiscal period that the check is posted to.  """  
      self.Reference:str = obj["Reference"]
      """  Displays any reference.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted.  """  
      self.CreditMemoNum:int = obj["CreditMemoNum"]
      """  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Displays the customer currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Displays the exchange rate that is used for this check.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Displays the tax amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Displays the legal number of the check.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.CardType:str = obj["CardType"]
      """  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  """  
      self.ExpirationMonth:int = obj["ExpirationMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpirationYear:int = obj["ExpirationYear"]
      """  The expiration year of the credit card.  """  
      self.CardID:str = obj["CardID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Stores the encrypted credit card number  """  
      self.CCAmount:int = obj["CCAmount"]
      """  Credit Transaction Amount, makes up part of CCTotal  """  
      self.CCFreight:int = obj["CCFreight"]
      """  Credit Card transaction freight amount, part of CCTotal  """  
      self.CCTax:int = obj["CCTax"]
      """  Credit Card Transaction Tax amount, part of CCTotal  """  
      self.CCTotal:int = obj["CCTotal"]
      """  Total amount being sent to the credit card processor  """  
      self.CCDocAmount:int = obj["CCDocAmount"]
      """  See CCAmount  """  
      self.CCDocFreight:int = obj["CCDocFreight"]
      """  See CCFreight  """  
      self.CCDocTax:int = obj["CCDocTax"]
      """  See CCTax  """  
      self.CCDocTotal:int = obj["CCDocTotal"]
      """  See CCTotal  """  
      self.CCStreetAddr:str = obj["CCStreetAddr"]
      """  Address used during AVS validation for credit transactions  """  
      self.CCZip:str = obj["CCZip"]
      """  Zip used during AVS validation in credit transactions  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnAppliedAmt:int = obj["Rpt1UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnAppliedAmt:int = obj["Rpt2UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnAppliedAmt:int = obj["Rpt3UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.DocDepApplied:int = obj["DocDepApplied"]
      """  Amount of deposit applied  """  
      self.Rpt1CCAmount:int = obj["Rpt1CCAmount"]
      """  See CCAmount  """  
      self.Rpt2CCAmount:int = obj["Rpt2CCAmount"]
      """  See CCAmount  """  
      self.Rpt3CCAmount:int = obj["Rpt3CCAmount"]
      """  See CCAmount  """  
      self.Rpt1CCFreight:int = obj["Rpt1CCFreight"]
      """  See CCFreight  """  
      self.Rpt2CCFreight:int = obj["Rpt2CCFreight"]
      """  See CCFreight  """  
      self.Rpt3CCFreight:int = obj["Rpt3CCFreight"]
      """  See CCFreight  """  
      self.Rpt1CCTax:int = obj["Rpt1CCTax"]
      """  See CCTax  """  
      self.Rpt2CCTax:int = obj["Rpt2CCTax"]
      """  See CCTax  """  
      self.Rpt3CCTax:int = obj["Rpt3CCTax"]
      """  See CCTax  """  
      self.Rpt1CCTotal:int = obj["Rpt1CCTotal"]
      """  See CCTotal  """  
      self.Rpt2CCTotal:int = obj["Rpt2CCTotal"]
      """  See CCTotal  """  
      self.Rpt3CCTotal:int = obj["Rpt3CCTotal"]
      """  See CCTotal  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.ReceiptCurrencyCode:str = obj["ReceiptCurrencyCode"]
      """  The unique code of Receipt Currency.  """  
      self.ReceiptAmt:int = obj["ReceiptAmt"]
      """  Amount of Receipt in Receipt Currency.  """  
      self.BankRcptExchangeRate:int = obj["BankRcptExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  """  
      self.SettlementExchangeRate:int = obj["SettlementExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  """  
      self.CMCurrencyCode:str = obj["CMCurrencyCode"]
      """  The unique Currency code for Credit Memo.  """  
      self.CMAmount:int = obj["CMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.ReverseRef:int = obj["ReverseRef"]
      """  Reference to cash receipt which had been reversed.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Date when cash receipt had been reversed  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.TaxWhld:int = obj["TaxWhld"]
      """  Withhold Tax  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Dsicount Date  """  
      self.TaxWhldCalc:int = obj["TaxWhldCalc"]
      """  Calculate Withhold Tax  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Addition to Contract  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.UnallocatedAmt:int = obj["UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  """  
      self.DocUnallocatedAmt:int = obj["DocUnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  """  
      self.Rpt1UnallocatedAmt:int = obj["Rpt1UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  """  
      self.Rpt2UnallocatedAmt:int = obj["Rpt2UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  """  
      self.Rpt3UnallocatedAmt:int = obj["Rpt3UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  """  
      self.ApplyHeadNum:int = obj["ApplyHeadNum"]
      """  Number of the unallocated deposit payment to be apply.  """  
      self.AllocatedAmt:int = obj["AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Base currency.  """  
      self.DocAllocatedAmt:int = obj["DocAllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Document currency.  """  
      self.Rpt1AllocatedAmt:int = obj["Rpt1AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  """  
      self.Rpt2AllocatedAmt:int = obj["Rpt2AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  """  
      self.Rpt3AllocatedAmt:int = obj["Rpt3AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  """  
      self.Comment:str = obj["Comment"]
      """  Comments related to the cash receipt.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment Method Unique Identifier  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.BankTranID:str = obj["BankTranID"]
      """  ID Given by the Bank assigned during matching  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.TaxRemarks:str = obj["TaxRemarks"]
      """  Tax Remarks  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.BankTransDate:str = obj["BankTransDate"]
      """  Bank Transaction Date  """  
      self.Payee:str = obj["Payee"]
      """  Payee  """  
      self.AccountNumber:str = obj["AccountNumber"]
      """  AccountNumber  """  
      self.OtherDetails:str = obj["OtherDetails"]
      """  OtherDetails  """  
      self.MandateReference:str = obj["MandateReference"]
      """  MandateReference  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SEPADDExportDate:str = obj["SEPADDExportDate"]
      """  SEPADDExportDate  """  
      self.BOEInvoiceNum:int = obj["BOEInvoiceNum"]
      """  BOE Invoice Number  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.OwnReference:str = obj["OwnReference"]
      """  OwnReference  """  
      self.DocumentType:str = obj["DocumentType"]
      """  DocumentType  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.BankRcptExchangeRate10D:int = obj["BankRcptExchangeRate10D"]
      """  BankRcptExchangeRate10D  """  
      self.SettlementExchangeRate10D:int = obj["SettlementExchangeRate10D"]
      """  SettlementExchangeRate10D  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.PayMethodReference:str = obj["PayMethodReference"]
      """  PayMethodReference  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MX Receipt’s Fiscal Folio (UUID)  """  
      self.AllowUpdSettlementCurr:bool = obj["AllowUpdSettlementCurr"]
      """  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.AVSAddr:str = obj["AVSAddr"]
      """  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.AVSZip:str = obj["AVSZip"]
      """  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.BankAcctDesc:str = obj["BankAcctDesc"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Currency Value  """  
      self.BankBaseXRateLabel:str = obj["BankBaseXRateLabel"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      """  Bank Currency Symbol  """  
      self.BankExchangeRate:int = obj["BankExchangeRate"]
      self.BankRcptXRateLabel:str = obj["BankRcptXRateLabel"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      """  Bill To Name  """  
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  """  
      self.CardStore:str = obj["CardStore"]
      """  Stored Credit Card Number  """  
      self.CardTypeDescription:str = obj["CardTypeDescription"]
      """  The credit card description. For example, American Express, Visa, Master Card, Discover, etc.  """  
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      """  Description  """  
      self.CCAllowSales:bool = obj["CCAllowSales"]
      """  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  """  
      self.CCApprovalNum:str = obj["CCApprovalNum"]
      self.CCCSCID:str = obj["CCCSCID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  """  
      self.CCEnableAddress:bool = obj["CCEnableAddress"]
      """  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  """  
      self.CCEnableCSC:bool = obj["CCEnableCSC"]
      """  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  """  
      self.CCResponse:str = obj["CCResponse"]
      """  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  """  
      self.CCTranID:str = obj["CCTranID"]
      """  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  """  
      self.CCTranType:str = obj["CCTranType"]
      """  Credit Card Transaction Type  """  
      self.CMCurrencyCodeCurrDesc:str = obj["CMCurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CMCurrencyCodeCurrencyID:str = obj["CMCurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CMCurrencyCodeCurrName:str = obj["CMCurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CMCurrencyCodeCurrSymbol:str = obj["CMCurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CMCurrencyCodeDocumentDesc:str = obj["CMCurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CSCResult:str = obj["CSCResult"]
      """  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustFullAddr:str = obj["CustFullAddr"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustomerName:str = obj["CustomerName"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.DocumentNum:int = obj["DocumentNum"]
      """  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  """  
      self.DspCMAmount:int = obj["DspCMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.DspDocTranAmt:int = obj["DspDocTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user enters this amount and then it is used as a limit/control when applying it to the invoices.  """  
      self.DspSalesOrderValue:int = obj["DspSalesOrderValue"]
      self.DspTranAmt:int = obj["DspTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  """  
      self.EnableTransactionDate:bool = obj["EnableTransactionDate"]
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  """  
      self.InvcLegalNumber:str = obj["InvcLegalNumber"]
      """  The InvcHead legal number  """  
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      """  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumberDsp:str = obj["LegalNumberDsp"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockRate:bool = obj["LockRate"]
      """  Copied from OrderHed.LockRate  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.PaymentMethod:str = obj["PaymentMethod"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      """  Description  """  
      self.RcptCurrencyCodeCurrDesc:str = obj["RcptCurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.RcptCurrencyCodeCurrencyID:str = obj["RcptCurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.RcptCurrencyCodeCurrName:str = obj["RcptCurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.RcptCurrencyCodeCurrSymbol:str = obj["RcptCurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.RcptCurrencyCodeDocumentDesc:str = obj["RcptCurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.ReferencePNRef:str = obj["ReferencePNRef"]
      """  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  """  
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SalesOrderValue:int = obj["SalesOrderValue"]
      self.SettlementXRateLabel:str = obj["SettlementXRateLabel"]
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  """  
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      """  Sum of all rounding differences of the payments for one Cash Receipt and one Check  """  
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Description of TranType  """  
      self.UnappliedAmountApplied:bool = obj["UnappliedAmountApplied"]
      """  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  """  
      self.XRateLabel:str = obj["XRateLabel"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashHeadListTableset:
   def __init__(self, obj):
      self.CashHeadList:list[Erp_Tablesets_CashHeadListRow] = obj["CashHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CashHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Displays the ID of the group the transaction is assigned to.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Displays the receipt header number used for internal reference.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.TranType:str = obj["TranType"]
      """  Displays the transaction type.  """  
      self.CheckRef:str = obj["CheckRef"]
      """  Displays the number of the check.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Displays the transaction amount.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Displays the transaction amount in customer currency.  """  
      self.CustID:str = obj["CustID"]
      """  Displays the customer ID.  """  
      self.TranDate:str = obj["TranDate"]
      """  Displays the date of the transaction.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  """  
      self.UnAppliedAmt:int = obj["UnAppliedAmt"]
      """  Displays the unapplied amount.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Displays the unapplied amount in base currency.  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Displays the amount applied to invoices.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Displays the amount in document currency applied to invoices.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Displays the fiscal year that the check is posted to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Displays the fiscal period that the check is posted to.  """  
      self.Reference:str = obj["Reference"]
      """  Displays any reference.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted.  """  
      self.CreditMemoNum:int = obj["CreditMemoNum"]
      """  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Displays the customer currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Displays the exchange rate that is used for this check.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Displays the tax amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Displays the legal number of the check.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.CardType:str = obj["CardType"]
      """  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  """  
      self.ExpirationMonth:int = obj["ExpirationMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpirationYear:int = obj["ExpirationYear"]
      """  The expiration year of the credit card.  """  
      self.CardID:str = obj["CardID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Stores the encrypted credit card number  """  
      self.CCAmount:int = obj["CCAmount"]
      """  Credit Transaction Amount, makes up part of CCTotal  """  
      self.CCFreight:int = obj["CCFreight"]
      """  Credit Card transaction freight amount, part of CCTotal  """  
      self.CCTax:int = obj["CCTax"]
      """  Credit Card Transaction Tax amount, part of CCTotal  """  
      self.CCTotal:int = obj["CCTotal"]
      """  Total amount being sent to the credit card processor  """  
      self.CCDocAmount:int = obj["CCDocAmount"]
      """  See CCAmount  """  
      self.CCDocFreight:int = obj["CCDocFreight"]
      """  See CCFreight  """  
      self.CCDocTax:int = obj["CCDocTax"]
      """  See CCTax  """  
      self.CCDocTotal:int = obj["CCDocTotal"]
      """  See CCTotal  """  
      self.CCStreetAddr:str = obj["CCStreetAddr"]
      """  Address used during AVS validation for credit transactions  """  
      self.CCZip:str = obj["CCZip"]
      """  Zip used during AVS validation in credit transactions  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnAppliedAmt:int = obj["Rpt1UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnAppliedAmt:int = obj["Rpt2UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnAppliedAmt:int = obj["Rpt3UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.DocDepApplied:int = obj["DocDepApplied"]
      """  Amount of deposit applied  """  
      self.Rpt1CCAmount:int = obj["Rpt1CCAmount"]
      """  See CCAmount  """  
      self.Rpt2CCAmount:int = obj["Rpt2CCAmount"]
      """  See CCAmount  """  
      self.Rpt3CCAmount:int = obj["Rpt3CCAmount"]
      """  See CCAmount  """  
      self.Rpt1CCFreight:int = obj["Rpt1CCFreight"]
      """  See CCFreight  """  
      self.Rpt2CCFreight:int = obj["Rpt2CCFreight"]
      """  See CCFreight  """  
      self.Rpt3CCFreight:int = obj["Rpt3CCFreight"]
      """  See CCFreight  """  
      self.Rpt1CCTax:int = obj["Rpt1CCTax"]
      """  See CCTax  """  
      self.Rpt2CCTax:int = obj["Rpt2CCTax"]
      """  See CCTax  """  
      self.Rpt3CCTax:int = obj["Rpt3CCTax"]
      """  See CCTax  """  
      self.Rpt1CCTotal:int = obj["Rpt1CCTotal"]
      """  See CCTotal  """  
      self.Rpt2CCTotal:int = obj["Rpt2CCTotal"]
      """  See CCTotal  """  
      self.Rpt3CCTotal:int = obj["Rpt3CCTotal"]
      """  See CCTotal  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.ReceiptCurrencyCode:str = obj["ReceiptCurrencyCode"]
      """  The unique code of Receipt Currency.  """  
      self.ReceiptAmt:int = obj["ReceiptAmt"]
      """  Amount of Receipt in Receipt Currency.  """  
      self.BankRcptExchangeRate:int = obj["BankRcptExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  """  
      self.SettlementExchangeRate:int = obj["SettlementExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  """  
      self.CMCurrencyCode:str = obj["CMCurrencyCode"]
      """  The unique Currency code for Credit Memo.  """  
      self.CMAmount:int = obj["CMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.ReverseRef:int = obj["ReverseRef"]
      """  Reference to cash receipt which had been reversed.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Date when cash receipt had been reversed  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.TaxWhld:int = obj["TaxWhld"]
      """  Withhold Tax  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Dsicount Date  """  
      self.TaxWhldCalc:int = obj["TaxWhldCalc"]
      """  Calculate Withhold Tax  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Addition to Contract  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.UnallocatedAmt:int = obj["UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  """  
      self.DocUnallocatedAmt:int = obj["DocUnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  """  
      self.Rpt1UnallocatedAmt:int = obj["Rpt1UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  """  
      self.Rpt2UnallocatedAmt:int = obj["Rpt2UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  """  
      self.Rpt3UnallocatedAmt:int = obj["Rpt3UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  """  
      self.ApplyHeadNum:int = obj["ApplyHeadNum"]
      """  Number of the unallocated deposit payment to be apply.  """  
      self.AllocatedAmt:int = obj["AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Base currency.  """  
      self.DocAllocatedAmt:int = obj["DocAllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Document currency.  """  
      self.Rpt1AllocatedAmt:int = obj["Rpt1AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  """  
      self.Rpt2AllocatedAmt:int = obj["Rpt2AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  """  
      self.Rpt3AllocatedAmt:int = obj["Rpt3AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  """  
      self.Comment:str = obj["Comment"]
      """  Comments related to the cash receipt.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment Method Unique Identifier  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.BankTranID:str = obj["BankTranID"]
      """  ID Given by the Bank assigned during matching  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.TaxRemarks:str = obj["TaxRemarks"]
      """  Tax Remarks  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.BankTransDate:str = obj["BankTransDate"]
      """  Bank Transaction Date  """  
      self.Payee:str = obj["Payee"]
      """  Payee  """  
      self.AccountNumber:str = obj["AccountNumber"]
      """  AccountNumber  """  
      self.OtherDetails:str = obj["OtherDetails"]
      """  OtherDetails  """  
      self.MandateReference:str = obj["MandateReference"]
      """  MandateReference  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SEPADDExportDate:str = obj["SEPADDExportDate"]
      """  SEPADDExportDate  """  
      self.BOEInvoiceNum:int = obj["BOEInvoiceNum"]
      """  BOE Invoice Number  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.OwnReference:str = obj["OwnReference"]
      """  OwnReference  """  
      self.DocumentType:str = obj["DocumentType"]
      """  DocumentType  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.BankRcptExchangeRate10D:int = obj["BankRcptExchangeRate10D"]
      """  BankRcptExchangeRate10D  """  
      self.SettlementExchangeRate10D:int = obj["SettlementExchangeRate10D"]
      """  SettlementExchangeRate10D  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.PayMethodReference:str = obj["PayMethodReference"]
      """  PayMethodReference  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.RcptCurAppliedAmt:int = obj["RcptCurAppliedAmt"]
      """  The amount of the cash receipt applied to invoices in receipt currency  """  
      self.RcptCurUnAppliedAmt:int = obj["RcptCurUnAppliedAmt"]
      """  The amount of the cash receipt that is unapplied in receipt currency  """  
      self.MXAccountNumber:str = obj["MXAccountNumber"]
      """  MXAccountNumber  """  
      self.MXPaidAs:str = obj["MXPaidAs"]
      """  MX Method of Payment: single, multiple, etc.  """  
      self.MXPaySupplementFlag:bool = obj["MXPaySupplementFlag"]
      """  If TRUE then MX Electronic Payment XML is required  """  
      self.LockboxID:str = obj["LockboxID"]
      """  LockboxID  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MX Receipt’s Fiscal Folio (UUID)  """  
      self.MXOriginalCheckRef:str = obj["MXOriginalCheckRef"]
      """  MX UUID of the original Receipt being corrected  """  
      self.MXConfirmationCode:str = obj["MXConfirmationCode"]
      """  MX Confirmation Code for special Cash Receipts  """  
      self.MXBankID:str = obj["MXBankID"]
      """  MX Customer’s Bank ID  """  
      self.ReversedReason:str = obj["ReversedReason"]
      """  Text entered by the user to indicate the reason Cash receipt was Reversed.  """  
      self.CCCity:str = obj["CCCity"]
      """  Credit Card Holder City.  """  
      self.CCState:str = obj["CCState"]
      """  Credit Card Holder State.  """  
      self.ccToken:str = obj["ccToken"]
      """  ccToken  """  
      self.DepositBalance:int = obj["DepositBalance"]
      """  DepositBalance  """  
      self.DocDepositBalance:int = obj["DocDepositBalance"]
      """  DocDepositBalance  """  
      self.Rpt1DepositBalance:int = obj["Rpt1DepositBalance"]
      """  Rpt1DepositBalance  """  
      self.Rpt2DepositBalance:int = obj["Rpt2DepositBalance"]
      """  Rpt2DepositBalance  """  
      self.Rpt3DepositBalance:int = obj["Rpt3DepositBalance"]
      """  Rpt3DepositBalance  """  
      self.Adjustment:bool = obj["Adjustment"]
      """  Indicates this record is an adjustment CashHead.  """  
      self.AdjustmentRef:int = obj["AdjustmentRef"]
      """  Reference to cash receipt which had been adjusted.  """  
      self.AdjustmentReason:str = obj["AdjustmentReason"]
      """  The reason for the adjustment entered by the user  """  
      self.WriteOffAmount:int = obj["WriteOffAmount"]
      """  Total Check Write Off Amount  """  
      self.DocWriteOffAmount:int = obj["DocWriteOffAmount"]
      """  DocWriteOffAmount  """  
      self.Rpt1WriteOffAmount:int = obj["Rpt1WriteOffAmount"]
      """  Rpt1WriteOffAmount  """  
      self.Rpt2WriteOffAmount:int = obj["Rpt2WriteOffAmount"]
      """  Rpt2WriteOffAmount  """  
      self.Rpt3WriteOffAmount:int = obj["Rpt3WriteOffAmount"]
      """  Rpt3WriteOffAmount  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  Mexico Certified Timestamp  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  Mexico SAT Seal  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  Mexico Digital Seal  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  Mexico SAT Certificate Serial Number  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  Mexico Original String Timbre Fiscal Digital  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  Mexico Certificate  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  Mexico Certificate Serial Number  """  
      self.SourceGroupID:str = obj["SourceGroupID"]
      """  SourceGroupID  """  
      self.SourceHeadNum:int = obj["SourceHeadNum"]
      """  SourceHeadNum  """  
      self.SEC:str = obj["SEC"]
      """  Standard Entry Class Code  """  
      self.ACHTranCode:int = obj["ACHTranCode"]
      """  ACH Transaction Code  """  
      self.CustomerBankID:str = obj["CustomerBankID"]
      """  ID of the Customer's bank.  """  
      self.CustomerBankAcctNumber:str = obj["CustomerBankAcctNumber"]
      """  The Bank account number for the Customer.  """  
      self.CustomerBankSwiftNum:str = obj["CustomerBankSwiftNum"]
      """  CustomerBankSwiftNum  """  
      self.CustomerBankIBANCode:str = obj["CustomerBankIBANCode"]
      """  The Bank account IBAN Code  """  
      self.CustomerBankNameOnAccount:str = obj["CustomerBankNameOnAccount"]
      """  Name on the Bank Account.  """  
      self.CustomerBankAddress1:str = obj["CustomerBankAddress1"]
      """  First address line of customer bank.  """  
      self.CustomerBankAddress2:str = obj["CustomerBankAddress2"]
      """  Second address line of customer bank.  """  
      self.CustomerBankAddress3:str = obj["CustomerBankAddress3"]
      """  Third address line of customer bank.  """  
      self.CustomerBankCity:str = obj["CustomerBankCity"]
      """  Bank City  """  
      self.CustomerBankState:str = obj["CustomerBankState"]
      """  Bank State/Prov  """  
      self.CustomerBankPostalCode:str = obj["CustomerBankPostalCode"]
      """  Postal Code or zip code  """  
      self.CustomerBankCountryNum:int = obj["CustomerBankCountryNum"]
      """  Bank account Country Number.  """  
      self.ARRemittanceSlipPrinted:bool = obj["ARRemittanceSlipPrinted"]
      """  ARRemittanceSlipPrinted  """  
      self.CustomerBankName:str = obj["CustomerBankName"]
      """  Customer Bank Name  """  
      self.MXPostedTimeStamp:str = obj["MXPostedTimeStamp"]
      """  MXPostedTimeStamp  """  
      self.MXSerie:str = obj["MXSerie"]
      """  MXSerie  """  
      self.MXFolio:str = obj["MXFolio"]
      """  MXFolio  """  
      self.MXEPaymentType:str = obj["MXEPaymentType"]
      """  MXEPaymentType  """  
      self.MXEPaymentCertificateNumber:str = obj["MXEPaymentCertificateNumber"]
      """  MXEPaymentCertificateNumber  """  
      self.MXEPaymentOriginalString:str = obj["MXEPaymentOriginalString"]
      """  MXEPaymentOriginalString  """  
      self.MXEPaymentDigitalSeal:str = obj["MXEPaymentDigitalSeal"]
      """  MXEPaymentDigitalSeal  """  
      self.Source:str = obj["Source"]
      """  Source  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  GL Description for the Reverse process  """  
      self.CMDescription:str = obj["CMDescription"]
      """  GL Description for AR - Apply Credit Memo  """  
      self.BankReceiptAmt:int = obj["BankReceiptAmt"]
      """  Receipt Amount in Bank Currency  """  
      self.MXCancelReasonCode:str = obj["MXCancelReasonCode"]
      """  MXCancelReasonCode  """  
      self.MXSubstHeadNum:int = obj["MXSubstHeadNum"]
      """  MXSubstHeadNum  """  
      self.MXCancellationMode:str = obj["MXCancellationMode"]
      """  MXCancellationMode  """  
      self.ELIEInvException:str = obj["ELIEInvException"]
      """  E-invoice error description.  """  
      self.ELIEInvID:str = obj["ELIEInvID"]
      """  EInvoice ID  """  
      self.ELIEInvoice:bool = obj["ELIEInvoice"]
      """  E-invoice  """  
      self.ELIEInvServiceProviderStatus:int = obj["ELIEInvServiceProviderStatus"]
      """  E-invoice Service Provider Status  """  
      self.ELIEInvStatus:int = obj["ELIEInvStatus"]
      """  E-invoice Status  """  
      self.ELIEInvUpdatedBy:str = obj["ELIEInvUpdatedBy"]
      """  User Id of the person generated E-invoice.  """  
      self.ELIEInvUpdatedOn:str = obj["ELIEInvUpdatedOn"]
      """  E-invoice Updated On  """  
      self.AdjustmentCustName:str = obj["AdjustmentCustName"]
      """  Adjustment Customer Name  """  
      self.AdjustmentCustNum:int = obj["AdjustmentCustNum"]
      """  Customer to which the new invoices will be applied.  """  
      self.AdjustmentDate:str = obj["AdjustmentDate"]
      """  Date the adjustment was made.  """  
      self.AdjustmentDocUnAppliedAmt:int = obj["AdjustmentDocUnAppliedAmt"]
      """  Displays the amount available to apply to the invoices.  """  
      self.AdjustmentOnAccount:bool = obj["AdjustmentOnAccount"]
      """  On Account  """  
      self.AdjustmentTranDocTypeID:str = obj["AdjustmentTranDocTypeID"]
      """  Temp TranDocTypeID used when adjusting a Cash Rececipt  """  
      self.AllocDepBal:int = obj["AllocDepBal"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.AllowUpdSettlementCurr:bool = obj["AllowUpdSettlementCurr"]
      """  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  """  
      self.AmtToAlloc:int = obj["AmtToAlloc"]
      """  Amount to Allocate  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.AVSAddr:str = obj["AVSAddr"]
      """  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.AVSZip:str = obj["AVSZip"]
      """  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Currency Value  """  
      self.BankBaseXRateLabel:str = obj["BankBaseXRateLabel"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      """  Bank Currency Symbol  """  
      self.BankExchangeRate:int = obj["BankExchangeRate"]
      self.BankRcptXRateLabel:str = obj["BankRcptXRateLabel"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Base Currency Symbol  """  
      self.BillToName:str = obj["BillToName"]
      """  Bill To Name  """  
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  """  
      self.CardStore:str = obj["CardStore"]
      """  Stored Credit Card Number  """  
      self.CCAllowSales:bool = obj["CCAllowSales"]
      """  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  """  
      self.CCApprovalNum:str = obj["CCApprovalNum"]
      self.CCCSCID:str = obj["CCCSCID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  """  
      self.CCCSCIDToken:str = obj["CCCSCIDToken"]
      """  Tokenized value of CSCID  """  
      self.CCEnableAddress:bool = obj["CCEnableAddress"]
      """  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  """  
      self.CCEnableCSC:bool = obj["CCEnableCSC"]
      """  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  """  
      self.CCIsTraining:bool = obj["CCIsTraining"]
      """   Indicates if the credit card setup will be using a testing Paygate instance for transactions.
Force requests to use Paygate test url: paygate-test1.eaglesoa.com  """  
      self.CCResponse:str = obj["CCResponse"]
      """  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  """  
      self.CCTranID:str = obj["CCTranID"]
      """  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  """  
      self.CCTranType:str = obj["CCTranType"]
      """  Credit Card Transaction Type  """  
      self.CentralCollectionCheck:bool = obj["CentralCollectionCheck"]
      """  Check Box on the UI to filter records by Central Collection flag  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Correction Invoice with negative amount  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      """  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Credit Memo  """  
      self.CREProcessor:bool = obj["CREProcessor"]
      """  CREProcessor is true when Credit Card Configuration is CRE Server.  """  
      self.CSCResult:str = obj["CSCResult"]
      """  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.CurrAmtSelected:int = obj["CurrAmtSelected"]
      """  Current Amount Selected on Invoice Select Tab  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustFullAddr:str = obj["CustFullAddr"]
      """  Displays the address of the customer that paid the receipt.  """  
      self.CustomerName:str = obj["CustomerName"]
      self.DisableFieldsForPCashDoc:bool = obj["DisableFieldsForPCashDoc"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocAllocDepBal:int = obj["DocAllocDepBal"]
      self.DocAmtToAlloc:int = obj["DocAmtToAlloc"]
      """  Doc Amount to Allocate  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  Displays the discount applied to the receipt.  """  
      self.DocReceipt:int = obj["DocReceipt"]
      """  Displays the invoice amount paid by this receipt. The amount includes both discount and payment amounts.  """  
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.DocumentNum:int = obj["DocumentNum"]
      """  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  """  
      self.DocWhldTax:int = obj["DocWhldTax"]
      self.DspBankBatchID:str = obj["DspBankBatchID"]
      self.DspCMAmount:int = obj["DspCMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.DspDocTranAmt:int = obj["DspDocTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  """  
      self.DspSalesOrderValue:int = obj["DspSalesOrderValue"]
      self.DspTranAmt:int = obj["DspTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableGetDefaultAcct:bool = obj["EnableGetDefaultAcct"]
      """  Indicates if the option to get the default account is enable.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableTransactionDate:bool = obj["EnableTransactionDate"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  """  
      self.GLRefCodeDescription:str = obj["GLRefCodeDescription"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.InvcLegalNumber:str = obj["InvcLegalNumber"]
      """  The InvcHead legal number  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumberDsp:str = obj["LegalNumberDsp"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockRate:bool = obj["LockRate"]
      """  Copied from OrderHed.LockRate  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.ManualTaxAdj:bool = obj["ManualTaxAdj"]
      self.MXCancellationID:str = obj["MXCancellationID"]
      """  MXCancellationID  """  
      self.MXCancellationStatus:str = obj["MXCancellationStatus"]
      self.MXECEPXml:str = obj["MXECEPXml"]
      """  MXECEPXml  """  
      self.MXOriginalRefNum:str = obj["MXOriginalRefNum"]
      """  Mexico Calculated field - shows Check Reference number of the original Receipt being corrected  """  
      self.PayGateHostAddress:str = obj["PayGateHostAddress"]
      """  Host Address for the Paygate Hosted Token Service.  """  
      self.PayGateNameSpace:str = obj["PayGateNameSpace"]
      """  NameSpace for the Paygate Hosted Token Service.  """  
      self.PayGatePublicKey:str = obj["PayGatePublicKey"]
      """  Public Key for the Paygate Hosted Token Service EWA component.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  This column is used within cash receipt tracker to show either the receipt date or the source/ original receipt date if the cash receipt has been adjusted.  """  
      self.ReferencePNRef:str = obj["ReferencePNRef"]
      """  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  """  
      self.Rpt1AllocDepBal:int = obj["Rpt1AllocDepBal"]
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt1WhldTax:int = obj["Rpt1WhldTax"]
      self.Rpt2AllocDepBal:int = obj["Rpt2AllocDepBal"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt2WhldTax:int = obj["Rpt2WhldTax"]
      self.Rpt3AllocDepBal:int = obj["Rpt3AllocDepBal"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt3WhldTax:int = obj["Rpt3WhldTax"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SalesOrderValue:int = obj["SalesOrderValue"]
      self.SettlementXRateLabel:str = obj["SettlementXRateLabel"]
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  """  
      self.SystemTranType:str = obj["SystemTranType"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      """  Sum of all rounding differences of the payments for one Cash Receipt and one Check  """  
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Description of TranType  """  
      self.UnappliedAmountApplied:bool = obj["UnappliedAmountApplied"]
      """  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  """  
      self.WhldTax:int = obj["WhldTax"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.AdjustmentCustID:str = obj["AdjustmentCustID"]
      """  Displays the customer ID.  """  
      self.ReferenceTranDate:str = obj["ReferenceTranDate"]
      self.ReferenceTranNum:int = obj["ReferenceTranNum"]
      self.ReferenceTranTime:int = obj["ReferenceTranTime"]
      self.CustFullAddrFormatted:str = obj["CustFullAddrFormatted"]
      """  Displays the address of the customer that paid the receipt with newline delimiter.  """  
      self.EnableManualWHTax:bool = obj["EnableManualWHTax"]
      """  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  """  
      self.WHTaxManualChange:bool = obj["WHTaxManualChange"]
      """  Indicates if the withholding tax was manually modified.  """  
      self.TranTypeDescCaption:str = obj["TranTypeDescCaption"]
      """  Payment type description, displayed in the Details page header.  """  
      self.AdjustmentCustAddress:str = obj["AdjustmentCustAddress"]
      self.MXSubstGroupId:str = obj["MXSubstGroupId"]
      """  Substitution Cash Receipt Group ID  """  
      self.MXSubstCheckRef:str = obj["MXSubstCheckRef"]
      """  Substitution Cash Receipt CheckRef  """  
      self.MXSubstFiscalFolio:str = obj["MXSubstFiscalFolio"]
      """  Substitution Cash Receipt UUID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.CardTypeDescription:str = obj["CardTypeDescription"]
      self.CashBHedPosted:bool = obj["CashBHedPosted"]
      self.CashBHedCashBookNum:int = obj["CashBHedCashBookNum"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CMCurrencyCodeDocumentDesc:str = obj["CMCurrencyCodeDocumentDesc"]
      self.CMCurrencyCodeCurrName:str = obj["CMCurrencyCodeCurrName"]
      self.CMCurrencyCodeCurrSymbol:str = obj["CMCurrencyCodeCurrSymbol"]
      self.CMCurrencyCodeCurrDesc:str = obj["CMCurrencyCodeCurrDesc"]
      self.CMCurrencyCodeCurrencyID:str = obj["CMCurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PCashDocDirection:str = obj["PCashDocDirection"]
      self.PMUIDName:str = obj["PMUIDName"]
      self.PMUIDMXSATCode:str = obj["PMUIDMXSATCode"]
      self.PMUIDSummarizePerCustomer:bool = obj["PMUIDSummarizePerCustomer"]
      self.PMUIDType:int = obj["PMUIDType"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.RcptCurrencyCodeCurrencyID:str = obj["RcptCurrencyCodeCurrencyID"]
      self.RcptCurrencyCodeDocumentDesc:str = obj["RcptCurrencyCodeDocumentDesc"]
      self.RcptCurrencyCodeCurrDesc:str = obj["RcptCurrencyCodeCurrDesc"]
      self.RcptCurrencyCodeCurrSymbol:str = obj["RcptCurrencyCodeCurrSymbol"]
      self.RcptCurrencyCodeCurrName:str = obj["RcptCurrencyCodeCurrName"]
      self.ReverseMXCancelReasonCode:str = obj["ReverseMXCancelReasonCode"]
      self.ReverseMXCancellationMode:str = obj["ReverseMXCancellationMode"]
      self.SourceTranDateTranDate:str = obj["SourceTranDateTranDate"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashReceiptAdjustmentTableset:
   def __init__(self, obj):
      self.CashHead:list[Erp_Tablesets_CashHeadRow] = obj["CashHead"]
      self.CashDtl:list[Erp_Tablesets_CashDtlRow] = obj["CashDtl"]
      self.CDTaxDtl:list[Erp_Tablesets_CDTaxDtlRow] = obj["CDTaxDtl"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtCashReceiptAdjustmentTableset:
   def __init__(self, obj):
      self.CashHead:list[Erp_Tablesets_CashHeadRow] = obj["CashHead"]
      self.CashDtl:list[Erp_Tablesets_CashDtlRow] = obj["CashDtl"]
      self.CDTaxDtl:list[Erp_Tablesets_CDTaxDtlRow] = obj["CDTaxDtl"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ForceTakeDiscount_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

class ForceTakeDiscount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCDTaxDtl_input:
   """ Required : 
   ds
   sourceModule
   headNum
   apTranNo
   invoiceNum
   invoiceRef
   bankAcctID
   tranNum
   voided
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["ds"]
      self.sourceModule:str = obj["sourceModule"]
      self.headNum:int = obj["headNum"]
      self.apTranNo:int = obj["apTranNo"]
      self.invoiceNum:int = obj["invoiceNum"]
      self.invoiceRef:int = obj["invoiceRef"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.tranNum:int = obj["tranNum"]
      self.voided:bool = obj["voided"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewCDTaxDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCashDtl_input:
   """ Required : 
   ds
   groupID
   headNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      self.invoiceNum:int = obj["invoiceNum"]
      pass

class GetNewCashDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCashHead_input:
   """ Required : 
   ds
   groupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      pass

class GetNewCashHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPendingToPostAdjustments_input:
   """ Required : 
   invoiceNum
   """  
   def __init__(self, obj):
      self.invoiceNum:int = obj["invoiceNum"]
      pass

class GetPendingToPostAdjustments_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.messageList:str = obj["parameters"]
      self.docUnPostedBal:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCashHead
   whereClauseCashDtl
   whereClauseCDTaxDtl
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCashHead:str = obj["whereClauseCashHead"]
      self.whereClauseCashDtl:str = obj["whereClauseCashDtl"]
      self.whereClauseCDTaxDtl:str = obj["whereClauseCDTaxDtl"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class OnChangeTranDocTypeID_input:
   """ Required : 
   ipTranDocTypeID
   """  
   def __init__(self, obj):
      self.ipTranDocTypeID:str = obj["ipTranDocTypeID"]
      """  TranDocTypeID supplied  """  
      pass

class OnChangeTranDocTypeID_output:
   def __init__(self, obj):
      pass

class OnChangedAllocAmount_input:
   """ Required : 
   headNum
   forceDiscount
   ds
   """  
   def __init__(self, obj):
      self.headNum:int = obj["headNum"]
      self.forceDiscount:bool = obj["forceDiscount"]
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

class OnChangedAllocAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedCashApplied_input:
   """ Required : 
   forceDiscount
   headNum
   ds
   """  
   def __init__(self, obj):
      self.forceDiscount:bool = obj["forceDiscount"]
      self.headNum:int = obj["headNum"]
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

class OnChangedCashApplied_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedDiscount_input:
   """ Required : 
   forceDiscount
   headNum
   ds
   """  
   def __init__(self, obj):
      self.forceDiscount:bool = obj["forceDiscount"]
      self.headNum:int = obj["headNum"]
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

class OnChangedDiscount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedInvcSelected_input:
   """ Required : 
   forceDiscount
   headNum
   unappliedAmount
   ds
   """  
   def __init__(self, obj):
      self.forceDiscount:bool = obj["forceDiscount"]
      self.headNum:int = obj["headNum"]
      self.unappliedAmount:int = obj["unappliedAmount"]
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

class OnChangedInvcSelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingAllocAmount_input:
   """ Required : 
   proposedAllocAmountValue
   forceDiscount
   headNum
   ds
   """  
   def __init__(self, obj):
      self.proposedAllocAmountValue:int = obj["proposedAllocAmountValue"]
      self.forceDiscount:bool = obj["forceDiscount"]
      self.headNum:int = obj["headNum"]
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

class OnChangingAllocAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingCashApplied_input:
   """ Required : 
   proposedCashAppliedValue
   forceDiscount
   headNum
   ds
   """  
   def __init__(self, obj):
      self.proposedCashAppliedValue:int = obj["proposedCashAppliedValue"]
      self.forceDiscount:bool = obj["forceDiscount"]
      self.headNum:int = obj["headNum"]
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

class OnChangingCashApplied_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingDiscount_input:
   """ Required : 
   proposedDiscountValue
   forceDiscount
   headNum
   ds
   """  
   def __init__(self, obj):
      self.proposedDiscountValue:int = obj["proposedDiscountValue"]
      self.forceDiscount:bool = obj["forceDiscount"]
      self.headNum:int = obj["headNum"]
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

class OnChangingDiscount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingInvcSelected_input:
   """ Required : 
   proposedInvcSelectedValue
   forceDiscount
   headNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.proposedInvcSelectedValue:bool = obj["proposedInvcSelectedValue"]
      self.forceDiscount:bool = obj["forceDiscount"]
      self.headNum:int = obj["headNum"]
      self.invoiceNum:int = obj["invoiceNum"]
      pass

class OnChangingInvcSelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.messageList:str = obj["parameters"]
      self.docUnPostedBal:int = obj["parameters"]
      pass

      """  output parameters  """  

class PreAdjustCashReceipt_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["ds"]
      pass

class PreAdjustCashReceipt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["ds"]
      self.promptForLegalNumber:bool = obj["promptForLegalNumber"]
      pass

      """  output parameters  """  

class SelectInvoiceAlloc_input:
   """ Required : 
   flag
   d_chAmtToAlloc
   d_chAdjustmentDocUnAppliedAmt
   b_chCreditMemo
   i_chHeadNum
   forceDiscount
   ds
   matchingInfo
   """  
   def __init__(self, obj):
      self.flag:bool = obj["flag"]
      self.d_chAmtToAlloc:int = obj["d_chAmtToAlloc"]
      self.d_chAdjustmentDocUnAppliedAmt:int = obj["d_chAdjustmentDocUnAppliedAmt"]
      self.b_chCreditMemo:bool = obj["b_chCreditMemo"]
      self.i_chHeadNum:int = obj["i_chHeadNum"]
      self.forceDiscount:bool = obj["forceDiscount"]
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      self.matchingInfo:str = obj["matchingInfo"]
      pass

class SelectInvoiceAlloc_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetDisplayBalance_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

class SetDisplayBalance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcAllocTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCashReceiptAdjustmentTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCashReceiptAdjustmentTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CashReceiptAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

