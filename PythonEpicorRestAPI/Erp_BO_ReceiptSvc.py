import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ReceiptSvc
# Description: Receipt Entry
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Receipts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Receipts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Receipts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts",headers=creds) as resp:
           return await resp.json()

async def post_Receipts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Receipts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RcvHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Receipts_Company_VendorNum_PurPoint_PackSlip(Company, VendorNum, PurPoint, PackSlip, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Receipt item
   Description: Calls GetByID to retrieve the Receipt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Receipt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Receipts_Company_VendorNum_PurPoint_PackSlip(Company, VendorNum, PurPoint, PackSlip, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Receipt for the service
   Description: Calls UpdateExt to update Receipt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Receipt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Receipts_Company_VendorNum_PurPoint_PackSlip(Company, VendorNum, PurPoint, PackSlip, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Receipt item
   Description: Call UpdateExt to delete Receipt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Receipt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")",headers=creds) as resp:
           return await resp.json()

async def get_Receipts_Company_VendorNum_PurPoint_PackSlip_RcvHeadTaxes(Company, VendorNum, PurPoint, PackSlip, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RcvHeadTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvHeadTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvHeadTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/RcvHeadTaxes",headers=creds) as resp:
           return await resp.json()

async def get_Receipts_Company_VendorNum_PurPoint_PackSlip_RcvHeadTaxes_Company_VendorNum_PurPoint_PackSlip_TaxCode_RateCode_ECAcquisitionSeq(Company, VendorNum, PurPoint, PackSlip, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvHeadTax item
   Description: Calls GetByID to retrieve the RcvHeadTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvHeadTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvHeadTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/RcvHeadTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_Receipts_Company_VendorNum_PurPoint_PackSlip_RcvDtls(Company, VendorNum, PurPoint, PackSlip, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RcvDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/RcvDtls",headers=creds) as resp:
           return await resp.json()

async def get_Receipts_Company_VendorNum_PurPoint_PackSlip_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine(Company, VendorNum, PurPoint, PackSlip, PackLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvDtl item
   Description: Calls GetByID to retrieve the RcvDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_Receipts_Company_VendorNum_PurPoint_PackSlip_RcvMiscs(Company, VendorNum, PurPoint, PackSlip, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RcvMiscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvMiscs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/RcvMiscs",headers=creds) as resp:
           return await resp.json()

async def get_Receipts_Company_VendorNum_PurPoint_PackSlip_RcvMiscs_Company_VendorNum_PurPoint_PackSlip_MiscSeq(Company, VendorNum, PurPoint, PackSlip, MiscSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvMisc item
   Description: Calls GetByID to retrieve the RcvMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvMisc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param MiscSeq: Desc: MiscSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/RcvMiscs(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_Receipts_Company_VendorNum_PurPoint_PackSlip_RcvHeadAttches(Company, VendorNum, PurPoint, PackSlip, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RcvHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvHeadAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/RcvHeadAttches",headers=creds) as resp:
           return await resp.json()

async def get_Receipts_Company_VendorNum_PurPoint_PackSlip_RcvHeadAttches_Company_VendorNum_PurPoint_PackSlip_DrawingSeq(Company, VendorNum, PurPoint, PackSlip, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvHeadAttch item
   Description: Calls GetByID to retrieve the RcvHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvHeadAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/Receipts(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + ")/RcvHeadAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RcvHeadTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RcvHeadTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvHeadTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvHeadTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadTaxes",headers=creds) as resp:
           return await resp.json()

async def post_RcvHeadTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvHeadTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvHeadTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RcvHeadTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RcvHeadTaxes_Company_VendorNum_PurPoint_PackSlip_TaxCode_RateCode_ECAcquisitionSeq(Company, VendorNum, PurPoint, PackSlip, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvHeadTax item
   Description: Calls GetByID to retrieve the RcvHeadTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvHeadTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvHeadTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RcvHeadTaxes_Company_VendorNum_PurPoint_PackSlip_TaxCode_RateCode_ECAcquisitionSeq(Company, VendorNum, PurPoint, PackSlip, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RcvHeadTax for the service
   Description: Calls UpdateExt to update RcvHeadTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvHeadTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvHeadTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RcvHeadTaxes_Company_VendorNum_PurPoint_PackSlip_TaxCode_RateCode_ECAcquisitionSeq(Company, VendorNum, PurPoint, PackSlip, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RcvHeadTax item
   Description: Call UpdateExt to delete RcvHeadTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvHeadTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RcvDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RcvDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls",headers=creds) as resp:
           return await resp.json()

async def post_RcvDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RcvDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine(Company, VendorNum, PurPoint, PackSlip, PackLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvDtl item
   Description: Calls GetByID to retrieve the RcvDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine(Company, VendorNum, PurPoint, PackSlip, PackLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RcvDtl for the service
   Description: Calls UpdateExt to update RcvDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine(Company, VendorNum, PurPoint, PackSlip, PackLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RcvDtl item
   Description: Call UpdateExt to delete RcvDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine_RcvDtlAttrValueSets(Company, VendorNum, PurPoint, PackSlip, PackLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RcvDtlAttrValueSets items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvDtlAttrValueSets1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlAttrValueSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")/RcvDtlAttrValueSets",headers=creds) as resp:
           return await resp.json()

async def get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine_RcvDtlAttrValueSets_Company_VendorNum_PurPoint_PackSlip_PackLine_AttributeValueSeq(Company, VendorNum, PurPoint, PackSlip, PackLine, AttributeValueSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvDtlAttrValueSet item
   Description: Calls GetByID to retrieve the RcvDtlAttrValueSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtlAttrValueSet1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param AttributeValueSeq: Desc: AttributeValueSeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvDtlAttrValueSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")/RcvDtlAttrValueSets(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + AttributeValueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine_RcvDtlTaxes(Company, VendorNum, PurPoint, PackSlip, PackLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RcvDtlTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvDtlTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")/RcvDtlTaxes",headers=creds) as resp:
           return await resp.json()

async def get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine_RcvDtlTaxes_Company_VendorNum_PurPoint_PackSlip_PackLine_TaxCode_RateCode_ECAcquisitionSeq(Company, VendorNum, PurPoint, PackSlip, PackLine, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvDtlTax item
   Description: Calls GetByID to retrieve the RcvDtlTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtlTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvDtlTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")/RcvDtlTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine_RcvDuties(Company, VendorNum, PurPoint, PackSlip, PackLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RcvDuties items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvDuties1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDutyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")/RcvDuties",headers=creds) as resp:
           return await resp.json()

async def get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine_RcvDuties_Company_VendorNum_PurPoint_PackSlip_PackLine_DutySeq(Company, VendorNum, PurPoint, PackSlip, PackLine, DutySeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvDuty item
   Description: Calls GetByID to retrieve the RcvDuty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDuty1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param DutySeq: Desc: DutySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvDutyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")/RcvDuties(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + DutySeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine_RcvDtlAttches(Company, VendorNum, PurPoint, PackSlip, PackLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RcvDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvDtlAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")/RcvDtlAttches",headers=creds) as resp:
           return await resp.json()

async def get_RcvDtls_Company_VendorNum_PurPoint_PackSlip_PackLine_RcvDtlAttches_Company_VendorNum_PurPoint_PackSlip_PackLine_DrawingSeq(Company, VendorNum, PurPoint, PackSlip, PackLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvDtlAttch item
   Description: Calls GetByID to retrieve the RcvDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtlAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")/RcvDtlAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RcvDtlAttrValueSets(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RcvDtlAttrValueSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvDtlAttrValueSets
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlAttrValueSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttrValueSets",headers=creds) as resp:
           return await resp.json()

async def post_RcvDtlAttrValueSets(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvDtlAttrValueSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvDtlAttrValueSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RcvDtlAttrValueSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttrValueSets", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RcvDtlAttrValueSets_Company_VendorNum_PurPoint_PackSlip_PackLine_AttributeValueSeq(Company, VendorNum, PurPoint, PackSlip, PackLine, AttributeValueSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvDtlAttrValueSet item
   Description: Calls GetByID to retrieve the RcvDtlAttrValueSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtlAttrValueSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param AttributeValueSeq: Desc: AttributeValueSeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvDtlAttrValueSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttrValueSets(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + AttributeValueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RcvDtlAttrValueSets_Company_VendorNum_PurPoint_PackSlip_PackLine_AttributeValueSeq(Company, VendorNum, PurPoint, PackSlip, PackLine, AttributeValueSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RcvDtlAttrValueSet for the service
   Description: Calls UpdateExt to update RcvDtlAttrValueSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvDtlAttrValueSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param AttributeValueSeq: Desc: AttributeValueSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvDtlAttrValueSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttrValueSets(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + AttributeValueSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RcvDtlAttrValueSets_Company_VendorNum_PurPoint_PackSlip_PackLine_AttributeValueSeq(Company, VendorNum, PurPoint, PackSlip, PackLine, AttributeValueSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RcvDtlAttrValueSet item
   Description: Call UpdateExt to delete RcvDtlAttrValueSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvDtlAttrValueSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param AttributeValueSeq: Desc: AttributeValueSeq   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttrValueSets(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + AttributeValueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RcvDtlTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RcvDtlTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvDtlTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlTaxes",headers=creds) as resp:
           return await resp.json()

async def post_RcvDtlTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvDtlTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvDtlTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RcvDtlTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RcvDtlTaxes_Company_VendorNum_PurPoint_PackSlip_PackLine_TaxCode_RateCode_ECAcquisitionSeq(Company, VendorNum, PurPoint, PackSlip, PackLine, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvDtlTax item
   Description: Calls GetByID to retrieve the RcvDtlTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtlTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvDtlTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RcvDtlTaxes_Company_VendorNum_PurPoint_PackSlip_PackLine_TaxCode_RateCode_ECAcquisitionSeq(Company, VendorNum, PurPoint, PackSlip, PackLine, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RcvDtlTax for the service
   Description: Calls UpdateExt to update RcvDtlTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvDtlTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvDtlTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RcvDtlTaxes_Company_VendorNum_PurPoint_PackSlip_PackLine_TaxCode_RateCode_ECAcquisitionSeq(Company, VendorNum, PurPoint, PackSlip, PackLine, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RcvDtlTax item
   Description: Call UpdateExt to delete RcvDtlTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvDtlTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RcvDuties(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RcvDuties items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvDuties
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDutyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDuties",headers=creds) as resp:
           return await resp.json()

async def post_RcvDuties(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvDuties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvDutyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RcvDutyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDuties", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RcvDuties_Company_VendorNum_PurPoint_PackSlip_PackLine_DutySeq(Company, VendorNum, PurPoint, PackSlip, PackLine, DutySeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvDuty item
   Description: Calls GetByID to retrieve the RcvDuty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDuty
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param DutySeq: Desc: DutySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvDutyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDuties(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + DutySeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RcvDuties_Company_VendorNum_PurPoint_PackSlip_PackLine_DutySeq(Company, VendorNum, PurPoint, PackSlip, PackLine, DutySeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RcvDuty for the service
   Description: Calls UpdateExt to update RcvDuty. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvDuty
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param DutySeq: Desc: DutySeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvDutyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDuties(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + DutySeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RcvDuties_Company_VendorNum_PurPoint_PackSlip_PackLine_DutySeq(Company, VendorNum, PurPoint, PackSlip, PackLine, DutySeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RcvDuty item
   Description: Call UpdateExt to delete RcvDuty item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvDuty
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param DutySeq: Desc: DutySeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDuties(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + DutySeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RcvDtlAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RcvDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvDtlAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttches",headers=creds) as resp:
           return await resp.json()

async def post_RcvDtlAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvDtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RcvDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RcvDtlAttches_Company_VendorNum_PurPoint_PackSlip_PackLine_DrawingSeq(Company, VendorNum, PurPoint, PackSlip, PackLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvDtlAttch item
   Description: Calls GetByID to retrieve the RcvDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RcvDtlAttches_Company_VendorNum_PurPoint_PackSlip_PackLine_DrawingSeq(Company, VendorNum, PurPoint, PackSlip, PackLine, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RcvDtlAttch for the service
   Description: Calls UpdateExt to update RcvDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RcvDtlAttches_Company_VendorNum_PurPoint_PackSlip_PackLine_DrawingSeq(Company, VendorNum, PurPoint, PackSlip, PackLine, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RcvDtlAttch item
   Description: Call UpdateExt to delete RcvDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvDtlAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RcvMiscs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RcvMiscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvMiscs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscs",headers=creds) as resp:
           return await resp.json()

async def post_RcvMiscs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvMiscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvMiscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RcvMiscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RcvMiscs_Company_VendorNum_PurPoint_PackSlip_MiscSeq(Company, VendorNum, PurPoint, PackSlip, MiscSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvMisc item
   Description: Calls GetByID to retrieve the RcvMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param MiscSeq: Desc: MiscSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscs(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RcvMiscs_Company_VendorNum_PurPoint_PackSlip_MiscSeq(Company, VendorNum, PurPoint, PackSlip, MiscSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RcvMisc for the service
   Description: Calls UpdateExt to update RcvMisc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param MiscSeq: Desc: MiscSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvMiscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscs(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RcvMiscs_Company_VendorNum_PurPoint_PackSlip_MiscSeq(Company, VendorNum, PurPoint, PackSlip, MiscSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RcvMisc item
   Description: Call UpdateExt to delete RcvMisc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param MiscSeq: Desc: MiscSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscs(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RcvMiscs_Company_VendorNum_PurPoint_PackSlip_MiscSeq_RcvMiscTaxes(Company, VendorNum, PurPoint, PackSlip, MiscSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RcvMiscTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RcvMiscTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param MiscSeq: Desc: MiscSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvMiscTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscs(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + ")/RcvMiscTaxes",headers=creds) as resp:
           return await resp.json()

async def get_RcvMiscs_Company_VendorNum_PurPoint_PackSlip_MiscSeq_RcvMiscTaxes_Company_VendorNum_PurPoint_PackSlip_MiscSeq_TaxCode_RateCode_ECAcquisitionSeq(Company, VendorNum, PurPoint, PackSlip, MiscSeq, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvMiscTax item
   Description: Calls GetByID to retrieve the RcvMiscTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvMiscTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param MiscSeq: Desc: MiscSeq   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvMiscTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscs(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + ")/RcvMiscTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RcvMiscTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RcvMiscTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvMiscTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvMiscTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscTaxes",headers=creds) as resp:
           return await resp.json()

async def post_RcvMiscTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvMiscTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvMiscTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RcvMiscTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RcvMiscTaxes_Company_VendorNum_PurPoint_PackSlip_MiscSeq_TaxCode_RateCode_ECAcquisitionSeq(Company, VendorNum, PurPoint, PackSlip, MiscSeq, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvMiscTax item
   Description: Calls GetByID to retrieve the RcvMiscTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvMiscTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param MiscSeq: Desc: MiscSeq   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvMiscTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RcvMiscTaxes_Company_VendorNum_PurPoint_PackSlip_MiscSeq_TaxCode_RateCode_ECAcquisitionSeq(Company, VendorNum, PurPoint, PackSlip, MiscSeq, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RcvMiscTax for the service
   Description: Calls UpdateExt to update RcvMiscTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvMiscTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param MiscSeq: Desc: MiscSeq   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvMiscTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RcvMiscTaxes_Company_VendorNum_PurPoint_PackSlip_MiscSeq_TaxCode_RateCode_ECAcquisitionSeq(Company, VendorNum, PurPoint, PackSlip, MiscSeq, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RcvMiscTax item
   Description: Call UpdateExt to delete RcvMiscTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvMiscTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param MiscSeq: Desc: MiscSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvMiscTaxes(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + MiscSeq + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RcvHeadAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RcvHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvHeadAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadAttches",headers=creds) as resp:
           return await resp.json()

async def post_RcvHeadAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RcvHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RcvHeadAttches_Company_VendorNum_PurPoint_PackSlip_DrawingSeq(Company, VendorNum, PurPoint, PackSlip, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvHeadAttch item
   Description: Calls GetByID to retrieve the RcvHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RcvHeadAttches_Company_VendorNum_PurPoint_PackSlip_DrawingSeq(Company, VendorNum, PurPoint, PackSlip, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RcvHeadAttch for the service
   Description: Calls UpdateExt to update RcvHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RcvHeadAttches_Company_VendorNum_PurPoint_PackSlip_DrawingSeq(Company, VendorNum, PurPoint, PackSlip, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RcvHeadAttch item
   Description: Call UpdateExt to delete RcvHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/RcvHeadAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + DrawingSeq + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/LegalNumGenOpts",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PendingRcvDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PendingRcvDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PendingRcvDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PendingRcvDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/PendingRcvDtls",headers=creds) as resp:
           return await resp.json()

async def post_PendingRcvDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PendingRcvDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PendingRcvDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PendingRcvDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/PendingRcvDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PendingRcvDtls_Company_VendorNum_PurPoint_PackSlip_PONum_POLine_PORel(Company, VendorNum, PurPoint, PackSlip, PONum, POLine, PORel, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PendingRcvDtl item
   Description: Calls GetByID to retrieve the PendingRcvDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PendingRcvDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORel: Desc: PORel   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PendingRcvDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/PendingRcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PONum + "," + POLine + "," + PORel + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PendingRcvDtls_Company_VendorNum_PurPoint_PackSlip_PONum_POLine_PORel(Company, VendorNum, PurPoint, PackSlip, PONum, POLine, PORel, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PendingRcvDtl for the service
   Description: Calls UpdateExt to update PendingRcvDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PendingRcvDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORel: Desc: PORel   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PendingRcvDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/PendingRcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PONum + "," + POLine + "," + PORel + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PendingRcvDtls_Company_VendorNum_PurPoint_PackSlip_PONum_POLine_PORel(Company, VendorNum, PurPoint, PackSlip, PONum, POLine, PORel, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PendingRcvDtl item
   Description: Call UpdateExt to delete PendingRcvDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PendingRcvDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORel: Desc: PORel   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/PendingRcvDtls(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PONum + "," + POLine + "," + PORel + ")",headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SelectedSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedSerialNumbers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SelectedSerialNumbers",headers=creds) as resp:
           return await resp.json()

async def post_SelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SelectedSerialNumbers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SelectedSerialNumber item
   Description: Calls GetByID to retrieve the SelectedSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SelectedSerialNumber for the service
   Description: Calls UpdateExt to update SelectedSerialNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SelectedSerialNumber item
   Description: Call UpdateExt to delete SelectedSerialNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_SNFormats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SNFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNFormats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SNFormats",headers=creds) as resp:
           return await resp.json()

async def post_SNFormats(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SNFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SNFormats", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SNFormat item
   Description: Calls GetByID to retrieve the SNFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SNFormat for the service
   Description: Calls UpdateExt to update SNFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SNFormat item
   Description: Call UpdateExt to delete SNFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def get_SupplierXRefs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SupplierXRefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SupplierXRefs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SupplierXRefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SupplierXRefs",headers=creds) as resp:
           return await resp.json()

async def post_SupplierXRefs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SupplierXRefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SupplierXRefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SupplierXRefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SupplierXRefs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SupplierXRefs_Company_PartNum_VendNum_VendPartNum_MfgNum_MfgPartNum(Company, PartNum, VendNum, VendPartNum, MfgNum, MfgPartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SupplierXRef item
   Description: Calls GetByID to retrieve the SupplierXRef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SupplierXRef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param VendNum: Desc: VendNum   Required: True
      :param VendPartNum: Desc: VendPartNum   Required: True   Allow empty value : True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SupplierXRefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SupplierXRefs_Company_PartNum_VendNum_VendPartNum_MfgNum_MfgPartNum(Company, PartNum, VendNum, VendPartNum, MfgNum, MfgPartNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SupplierXRef for the service
   Description: Calls UpdateExt to update SupplierXRef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SupplierXRef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param VendNum: Desc: VendNum   Required: True
      :param VendPartNum: Desc: VendPartNum   Required: True   Allow empty value : True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SupplierXRefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SupplierXRefs_Company_PartNum_VendNum_VendPartNum_MfgNum_MfgPartNum(Company, PartNum, VendNum, VendPartNum, MfgNum, MfgPartNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SupplierXRef item
   Description: Call UpdateExt to delete SupplierXRef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SupplierXRef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param VendNum: Desc: VendNum   Required: True
      :param VendPartNum: Desc: VendPartNum   Required: True   Allow empty value : True
      :param MfgNum: Desc: MfgNum   Required: True
      :param MfgPartNum: Desc: MfgPartNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/SupplierXRefs(" + Company + "," + PartNum + "," + VendNum + "," + VendPartNum + "," + MfgNum + "," + MfgPartNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRcvHead, whereClauseRcvHeadAttch, whereClauseRcvHeadTax, whereClauseRcvDtl, whereClauseRcvDtlAttch, whereClauseRcvDtlAttrValueSet, whereClauseRcvDtlTax, whereClauseRcvDuty, whereClauseRcvMisc, whereClauseRcvMiscTax, whereClauseLegalNumGenOpts, whereClausePendingRcvDtl, whereClauseSelectedSerialNumbers, whereClauseSNFormat, whereClauseSupplierXRef, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseRcvHead=" + whereClauseRcvHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRcvHeadAttch=" + whereClauseRcvHeadAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRcvHeadTax=" + whereClauseRcvHeadTax
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRcvDtl=" + whereClauseRcvDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRcvDtlAttch=" + whereClauseRcvDtlAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRcvDtlAttrValueSet=" + whereClauseRcvDtlAttrValueSet
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRcvDtlTax=" + whereClauseRcvDtlTax
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRcvDuty=" + whereClauseRcvDuty
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRcvMisc=" + whereClauseRcvMisc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRcvMiscTax=" + whereClauseRcvMiscTax
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
   params += "whereClausePendingRcvDtl=" + whereClausePendingRcvDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSelectedSerialNumbers=" + whereClauseSelectedSerialNumbers
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSNFormat=" + whereClauseSNFormat
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSupplierXRef=" + whereClauseSupplierXRef
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(vendorNum, purPoint, packSlip, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "purPoint=" + purPoint
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "packSlip=" + packSlip

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_MassReceiptsGeneratePCIDUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MassReceiptsGeneratePCIDUpdate
   Description: This method updates the new PCID Generated data for all RcvDtls selected via Mass Receipt.
   OperationID: MassReceiptsGeneratePCIDUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassReceiptsGeneratePCIDUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassReceiptsGeneratePCIDUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedTaxManual(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedTaxManual
   Description: Method to call when changing the manual tax calculation value on a line or indirect cost tax record. Updates RcvDtlTax / RcvMiscTax
tax amounts based on the new value of the flag back to system-calculated tax.
   OperationID: OnChangedTaxManual
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedTaxManual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedTaxManual_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxFixedAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxFixedAmount
   Description: Method to call when changing the fixed amount on the RcvDtlTax table currently
   OperationID: OnChangeTaxFixedAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxFixedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxFixedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxReportableAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxReportableAmt
   Description: Method to call when changing the reportable amount on either RcvMiscTax or RcvDtlTax
reportable amounts based on the new reportable amount.
   OperationID: OnChangeTaxReportableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxReportableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxReportableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxTaxableAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxTaxableAmt
   Description: Method to call when changing the taxable amount on either RcvMiscTax or RcvDtlTax
taxable amounts based on the new taxable amount.
   OperationID: OnChangeTaxTaxableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxTaxAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxTaxAmt
   Description: Method to call when changing the tax amount on a either a RcvMiscTax or a RcvDtlTax row
tax amounts based on the new tax amount.
   OperationID: OnChangeTaxTaxAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxDeductable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxDeductable
   Description: Method to call when changing the tax deductable on a Release line tax record.
   OperationID: OnChangeTaxDeductable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxDeductable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxDeductable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxTaxCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxTaxCode
   Description: Method to call when changing the tax code on a the RcvMiscTax or RcvDtlTax.  Validates the tax code and
updates RcvDtlTax tax amounts based on the new tax code.
   OperationID: OnChangeTaxTaxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxRateCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxRateCode
   Description: Method to call when changing the rate code on a tax record related to Release Tax Line.  Validates the rate and tax code
   OperationID: OnChangeTaxRateCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxPercent
   Description: Method to call when changing the tax percent on a tax release line record.  Updates RcvDtlTax
tax amounts based on the new tax percent only when one tax record exists.
   OperationID: OnChangeTaxPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDutyTariffCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDutyTariffCode
   Description: This method should be invoked when the Tariff Code changes. This method will validate
the tariffcode and defaults the duty amount.
   OperationID: OnChangeDutyTariffCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDutyTariffCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDutyTariffCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscApplyDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscApplyDate
   Description: This method should be invoked when the Apply Date in RcvMisc changes.
This method will validate the date and get new exchange rate.
   OperationID: OnChangeMiscApplyDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscCharge(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscCharge
   Description: This method should be invoked when the Miscellaneous Charge ID changes. This
method will validate the misc. charge and pull in the new default information.
   OperationID: OnChangeMiscCharge
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscCharge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscCharge_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscCurrencyCode
   Description: This method should be invoked when the Currency Code in RcvMisc changes.
This method will validate the currency code and pull in the new default information.
   OperationID: OnChangeMiscCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscDocActualAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscDocActualAmt
   Description: This method should be invoked when the RcvMisc.ActualAmt changes. This
method will validate the amount and convert it to the base currency.
   OperationID: OnChangeMiscDocActualAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscDocActualAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscDocActualAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscExchangeRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscExchangeRate
   Description: This method should be invoked when the Currency Exchange Rate in RcvMisc changes.
   OperationID: OnChangeMiscExchangeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscInvoiceLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscInvoiceLine
   Description: This method should be invoked when the Invoice Line in RcvMisc changes.
This method will validate the invoice line and pull in the new default information.
   OperationID: OnChangeMiscInvoiceLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscInvoiceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscInvoiceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscInvoiceNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscInvoiceNum
   Description: This method should be invoked when the Invoice Number in RcvMisc changes.
This method will validate the invoice number and pull in the new default information.
   OperationID: OnChangeMiscInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscMscNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscMscNum
   Description: This method should be invoked when the MscNum in RcvMisc changes.
This method will validate the MscNum and pull in the new default information.
   OperationID: OnChangeMiscMscNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscMscNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscMscNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscPercent
   Description: This method should be invoked when the RcvMisc.Percentage changes.
This method will calculate the amount and convert it to the base currency.
   OperationID: OnChangeMiscPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscRateGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscRateGrp
   Description: This method should be invoked when the Currency Rate Group in RcvMisc changes.
This method will validate the rate group and get new exchange rate.
   OperationID: OnChangeMiscRateGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscTaxCatID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscTaxCatID
   Description: This method should be invoked when TaxCatID changes. It will retrieve the default tax flag based on entered Tax Cat ID.
   OperationID: OnChangeMiscTaxCatID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscTaxCatID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscTaxCatID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscVendor
   Description: This method should be invoked when the vendor ID in RcvMisc changes.
This method will validate the vendor and pull in the new default vendor information.
   OperationID: OnChangeMiscVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPartNum">ipPartNum</param><param name="ipAttributeSetID">ipAttributeSetID</param><param name="ipQuantity">ipQuantity</param><param name="ipUOM">ipUOM</param><param name="ipVendNum">ipVendNum</param><param name="ipVendPP">ipVendPP</param><param name="ipPackSlip">ipPackSlip</param><param name="ipPackSlipLine">ipPackSlipLine</param><param name="ipJobNum">ipJobNum</param><param name="ipAsmSeq">ipAssmSeq</param><param name="ipSubOprSeq">ipSubOprSeq</param><param name="ipReceivedTo">ipReceivedTo</param><returns></returns>
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSNStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSNStatus
   OperationID: GetSNStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSNStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSNStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPartNum">Part Number</param><param name="ipAttributeSetID">Serial Number</param><param name="ipSerialNo">Serial Number</param><param name="ipVendorNum">Vendor Number</param><param name="ipJobNum">Job Number</param><param name="ipAsmSeq">Vendor Number</param><param name="ipSubOprSeq">Job Operation Number</param><param name="ipPackSlip">Pack Slip</param><param name="ipPackLine">Pack Slip Line</param><param name="ipReceivedTo">Received To</param><param name="ipJobSeqType">Job Sequence type</param><param name="warningMsg">Warning Message</param>
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckMassReceiptChangeWhseBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckMassReceiptChangeWhseBin
   Description: This method is obsolete use OnChangeDtlWarehouseCode / OnChangeDtlBin instead.
            
If warehouse or bin is changed in MassReceipts and this is a Planning Contract receipt
then we need to validate against the Contract
   OperationID: CheckMassReceiptChangeWhseBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckMassReceiptChangeWhseBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckMassReceiptChangeWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CommitRcvDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CommitRcvDtl
   Description: This method creates the Lines Received from MassReceipt option directly
into the DB. This was done for performance purposes.
   OperationID: CommitRcvDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CommitRcvDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitRcvDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateMassReceipts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateMassReceipts
   Description: This method is used to populate the ShipDtl datatable for Mass Receipts
and Intercompany Receipt linking
   OperationID: CreateMassReceipts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateMassReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMassReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HHCanEditPackSlip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HHCanEditPackSlip
   Description: This method was developed for HandHeld version to validate if a
pack slipt exist. In the handheld version users can't edit the lines.
   OperationID: HHCanEditPackSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HHCanEditPackSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHCanEditPackSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HHOnChangeDtlPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HHOnChangeDtlPartNum
   Description: This method is called by HHPOReceipt when a Part is entered.  It will check for multiple parts using the LibFindpart library.  It will then find the first open PO line for the entered part and populate the RcvDtl with the details for the PODetail and PORel.
   OperationID: HHOnChangeDtlPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HHOnChangeDtlPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHOnChangeDtlPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HHOnChangeDtlPOLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HHOnChangeDtlPOLine
   Description: This method is called by HHPOReceipt when a PO Line is entered.  It will make sure an open PO line exists for the entered Part and Line and populate the RcvDtl with details for the PODetail and PORel.
   OperationID: HHOnChangeDtlPOLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HHOnChangeDtlPOLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHOnChangeDtlPOLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HHOnChangeDtlPORelNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HHOnChangeDtlPORelNum
   Description: This method is called by HHPOReceipt when a PO Release Number is entered.  It will make sure an open PO line exists for the entered Part, Line and Release and populate the RcvDtl with details for the PODetail and PORel.
   OperationID: HHOnChangeDtlPORelNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HHOnChangeDtlPORelNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHOnChangeDtlPORelNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HHValRecDocReq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HHValRecDocReq
   Description: This method is to be called by the Hand Held PO Receipt program.
It can be called before or after calling the update for the RcvDtl.
It checks to see if receipt documents are required for a given Part/Lot number.
If they are then message text is returned in the infoMsg parameter.
The client displays this in a message box.
Note: For Hand Held this is only an informational and not an exception.
   OperationID: HHValRecDocReq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HHValRecDocReq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHValRecDocReq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSMIReceiptAttrPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSMIReceiptAttrPart
   Description: This method is used to Validate if the Receipt Line contains a Part with Track inventory Attributes and the POType equals SMI
and Intercompany Receipt linking
   OperationID: ValidateSMIReceiptAttrPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSMIReceiptAttrPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSMIReceiptAttrPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRcvHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRcvHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRcvHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRcvHeadAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRcvHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRcvHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRcvHeadTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRcvHeadTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvHeadTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRcvHeadTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvHeadTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRcvDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRcvDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRcvDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRcvDtlAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRcvDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvDtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRcvDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRcvDtlAttrValueSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRcvDtlAttrValueSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvDtlAttrValueSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRcvDtlAttrValueSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvDtlAttrValueSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRcvDtlTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRcvDtlTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvDtlTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRcvDtlTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvDtlTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRcvDuty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRcvDuty
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvDuty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRcvDuty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvDuty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRcvMisc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRcvMisc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvMisc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRcvMisc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvMisc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRcvMiscTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRcvMiscTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvMiscTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRcvMiscTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvMiscTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMtlQueueSeqValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMtlQueueSeqValue
   Description: Search for the MtlQueueSeq value from the MtlQueue row related to the current Non Conformance.
   OperationID: GetMtlQueueSeqValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlQueueSeqValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlQueueSeqValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignLegalNumber
   Description: Assign Legal Number to Packing Slip.
   OperationID: AssignLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateReceiptTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateReceiptTaxes
   Description: CALCULATE VANTAGE\TAX CONNECT TAX CALCULATIONS UI NEEDS TO CALL A SAVE BEFORE CALLING THIS PROCEDURE
   OperationID: CalculateReceiptTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateReceiptTaxes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateReceiptTaxes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCNCustomsDeclarationBillLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCNCustomsDeclarationBillLine
   Description: Purpose:  Check Declaration Bill Line
Parameters:
<param name="sMessage">Warning</param><param name="ds"></param>
   OperationID: CheckCNCustomsDeclarationBillLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCNCustomsDeclarationBillLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCNCustomsDeclarationBillLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CNPreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CNPreUpdate
   Description: Purpose:  Method should be called before Update to check China specific data
Parameters:
<param name="sMessage">Warning</param><param name="ds"></param>
   OperationID: CNPreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CNPreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CNPreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCompliance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCompliance
   Description: .
   OperationID: CheckCompliance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCompliance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCompliance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckContainersBeforeUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckContainersBeforeUpdate
   Description: This method is to be called right before the update of a ContainerReceipt.  If
there is a discrepancy between the quantities, serial numbers the
user is asked if they are sure they want to continue.
            
qQuestion and sQuestion are provided so the UI can format the message box
and make it easier for the end user to read the text.
   OperationID: CheckContainersBeforeUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckContainersBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckContainersBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckForDefaultRcvInfo(epicorHeaders = None):
   """  
   Summary: Invoke method CheckForDefaultRcvInfo
   Description: This method is to be run right after the form opens to determine whether the
default receiving warehouse and bin have been populated for the cur-plant.
If not, the form will close.
   OperationID: CheckForDefaultRcvInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForDefaultRcvInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CheckShipmentReceived(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckShipmentReceived
   Description: Validates if the Shipment has been received
   OperationID: CheckShipmentReceived
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckShipmentReceived_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckShipmentReceived_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ContainerReceiptsBeforeUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ContainerReceiptsBeforeUpdate
   Description: This is invoked before the Update in Container Receipts. The following checks are done:
1. Return a warning message if any of the partial receipt lines needs to recalculate container landed costs
2. Return a warning if there is a discrepancy between the quantities
3. Return a warning if there are none compliant lines
4. Return a bool indicating if user input is required for legal numbers
   OperationID: ContainerReceiptsBeforeUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ContainerReceiptsBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ContainerReceiptsBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ContainerReceiptsUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ContainerReceiptsUpdate
   Description: Invokes ReceiveContainerUpdateCore but returns an updated ContainerTrackingTableset
   OperationID: ContainerReceiptsUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ContainerReceiptsUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ContainerReceiptsUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateMaterialQueueForPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateMaterialQueueForPCID
   Description: This will invoke a shared function that will check that there are no Staged items on the PCID and if not, retrieves the first Item on the PCID that is associated with a Receipt line and creates a MtlQueue using these details.
   OperationID: CreateMaterialQueueForPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateMaterialQueueForPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMaterialQueueForPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DisburseLandedCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DisburseLandedCost
   Description: This method is used to disburse the Total Landed Cost across the receipt details.
The RcvDtl records will be updated to distribute the receipt Indirect Costs according
to the specified disburse method.  The Specific DutyAmt if available will be divided
equally among lines or by the percentage of the line's duties against total duties.
   OperationID: DisburseLandedCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisburseLandedCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisburseLandedCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   Description: Get "POReceipt" TranDocTypes in a filter string.
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetExistingRcvHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExistingRcvHead
   Description: Check if RcvHead information exists in DB. If so, data in CurrentTableSet is replaced.
   OperationID: GetExistingRcvHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExistingRcvHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExistingRcvHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListReceipts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListReceipts
   Description: <param name="whereClauseRcvDtl">Whereclause for RcvDtl table.</param>
<param name="pageSize">Page size.</param>
<param name="absolutePage">Absolute page.</param>
<param name="morePages">More pages.</param>
<returns>Epicor.Mfg.BO.InvcCustTrkDataSet</returns>
   OperationID: GetListReceipts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContainerReceiptPartTranPKs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContainerReceiptPartTranPKs
   Description: Returns PartTran primary key details of a Container Receipt for the Pack Slip / PO Num / Vendor Num entered
   OperationID: GetContainerReceiptPartTranPKs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContainerReceiptPartTranPKs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContainerReceiptPartTranPKs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartTranPKs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartTranPKs
   Description: Returns PartTran primary key details for the Pack Slip / PO Num / Vendor Num entered
   OperationID: GetPartTranPKs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartTranPKs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartTranPKs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPendingDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPendingDtl
   Description: Updates Receipt data set with PendingDtl.
   OperationID: GetPendingDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPendingDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPendingDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePONum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePONum
   Description: Validates if the Purchase Order Exists
   OperationID: ValidatePONum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPOInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPOInfo
   Description: This method returns default information for the PO Number and the new Vendor ID
information.
   OperationID: GetPOInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPOInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPurPointInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPurPointInfo
   Description: This method returns default information for the Vendor Purchase Point.
   OperationID: GetPurPointInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPurPointInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPurPointInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForAPInvoice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForAPInvoice
   Description: Invokes GetRows filtering on Receipts for the specified Invoice
   OperationID: GetRowsForAPInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForAPInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForAPInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForPayment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForPayment
   Description: Invokes GetRows filtering on Receipts for the specified Payment
   OperationID: GetRowsForPayment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForPO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForPO
   Description: Invokes GetRows filtering on Receipts for the specified PO
   OperationID: GetRowsForPO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReceiptDetailsFromContainer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReceiptDetailsFromContainer
   Description: Similar function to RecieveContainer, written to obtain the RcvDetail records for the Container Landed costs tracker
   OperationID: GetReceiptDetailsFromContainer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReceiptDetailsFromContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReceiptDetailsFromContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReceiptRelationshipMap(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReceiptRelationshipMap
   Description: Returns a serialized json string to show a Relationship Map for Receipt
   OperationID: GetReceiptRelationshipMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReceiptRelationshipMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReceiptRelationshipMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetWarningPOClosed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWarningPOClosed
   Description: Set cWarning to POClosed if PO is Closed,  OpenOrder = false
   OperationID: GetWarningPOClosed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWarningPOClosed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWarningPOClosed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportReceipt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportReceipt
   Description: This method imports the Receipt Head record from the IMRcvHead table.  It returns
the unique key information on the newly created Receipt header needed to import
the detail lines.  The detail records are imported by processing Mass Receipts for
the same IntQueId as indicated here.
   OperationID: ImportReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InitializeLandedCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InitializeLandedCost
   Description: This method is used to populate the MassReceipt dataset for use in Landed Costs
it also returns the default recovery account information
   OperationID: InitializeLandedCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InitializeLandedCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitializeLandedCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsContainerReceived(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsContainerReceived
   OperationID: IsContainerReceived
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsContainerReceived_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsContainerReceived_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumberGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessLandedCosts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessLandedCosts
   Description: This method is used to process the Landed Costs into the RcvHead and RcvDtl tables
All the MassReceipt records need to be marked as modified for this
   OperationID: ProcessLandedCosts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessLandedCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessLandedCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessIM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessIM
   Description: Finish processing a successful IC import
   OperationID: ProcessIM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessIM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessIM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReceiveAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReceiveAll
   Description: This method updates the Quantity for the lines created from MassReceipt
   OperationID: ReceiveAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReceiveAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReceiveAllLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReceiveAllLines
   Description: Sets ttRcvDtl.Received to true in all lines selected for MassReceipt.
   OperationID: ReceiveAllLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReceiveAllLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveAllLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReceiveContainerUsingArrivedDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReceiveContainerUsingArrivedDate
   Description: Purpose:  Gather existing rvcdtls and create new ones for remaining balances using a specific ArrivedDate.
This method builds the receipt data for a Container.
<param name="ds">Epicor.Mfg.BO.ReceiptDataSet</param><param name="inContainerID">ContainerID</param><param name="ipArrivedDate">Arrived Date to use for new receipt lines</param><returns>Epicor.Mfg.BO.ContainerTrackingDataSet</returns>
Notes:
   OperationID: ReceiveContainerUsingArrivedDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReceiveContainerUsingArrivedDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveContainerUsingArrivedDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreReceiveContainer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreReceiveContainer
   Description: Purpose:  Check to see if we can run ReceiveContainer.
Checks modules and for the existence of the
<param name="inContainerID">ContainerID</param><returns>Epicor.Mfg.BO.ContainerTrackingDataSet</returns>
Notes:
   OperationID: PreReceiveContainer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreReceiveContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreReceiveContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReceiveContainer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReceiveContainer
   Description: Purpose:  Gather existing rvcdtls and create new ones for remaining balances.
This method builds the receipt data for a Container.
<param name="ds">Epicor.Mfg.BO.ReceiptDataSet</param><param name="inContainerID">ContainerID</param><returns>Epicor.Mfg.BO.ContainerTrackingDataSet</returns>
Notes:
   OperationID: ReceiveContainer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReceiveContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReceiveContainerUpdateUsingArriveDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReceiveContainerUpdateUsingArriveDate
   Description: Mass Receive the po lines on a container with ArrivedDate specified to control the calcUnitCost currency conversion date.
   OperationID: ReceiveContainerUpdateUsingArriveDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReceiveContainerUpdateUsingArriveDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveContainerUpdateUsingArriveDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReceiveContainerUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReceiveContainerUpdate
   Description: Mass Receive the po lines on a container.
   OperationID: ReceiveContainerUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReceiveContainerUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveContainerUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetPrimaryBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetPrimaryBin
   Description: Set the Part Warehouse's Primary Bin when the Warehouse is changed.
   OperationID: SetPrimaryBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetPrimaryBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetPrimaryBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeRevisionNum
   Description: Processing when the Receipt Revision Number changes
   OperationID: OnChangeRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeContainerHdrArrivedDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeContainerHdrArrivedDate
   Description: This method should be invoked when the ContainerHeader ArrivedDate changes in the container receipt form.
This method will validate whether any POs associated with the container have a different currency rate based on the old arived date
than would be the currency rate based on the new arrived date.
opNeedsRecalc = true is returned if the UI needs to run logic to refresh the RcvDtl records in the ds
   OperationID: OnChangeContainerHdrArrivedDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeContainerHdrArrivedDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeContainerHdrArrivedDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResetLandedCostDisbursements(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResetLandedCostDisbursements
   Description: Initialize landed cost amounts to 0 and updates the landed cost disburse method.
   OperationID: ResetLandedCostDisbursements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetLandedCostDisbursements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetLandedCostDisbursements_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateMaster(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateMaster
   Description: Perform all validations associated with the Update.  We have combined all method calls that were being called
at update into this one method.  Making multiple BL calls is a performance issue and this increases performance.
   OperationID: UpdateMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateMRPONum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateMRPONum
   Description: This method validates that the PO Number is a valid PO before the Mass Receipts UI calls
   OperationID: ValidateMRPONum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMRPONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMRPONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateReceiptRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateReceiptRecords
   Description: Check if the receipt records exists.
   OperationID: ValidateReceiptRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateReceiptRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateReceiptRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLegalNumber
   Description: Voids the Legal Number and removes it from the Packing slip.
   OperationID: VoidLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckIfAttributeQtyMismatch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckIfAttributeQtyMismatch
   Description: Validates if there is a remaining qty difference between the attribute quantity and the receipt line quantity
   OperationID: CheckIfAttributeQtyMismatch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIfAttributeQtyMismatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIfAttributeQtyMismatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckHdrBeforeUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckHdrBeforeUpdate
   Description: This method will return three warning messages if the Receipt Header changes
any of the UpliftPercent, ReceiptDate and ArrivedDate. The user will be asked
if the changes should be applied to all the Receipt Details as well. This method
should be called before the Update method is called.
   OperationID: CheckHdrBeforeUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckHdrBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckHdrBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckLCAmtBeforeUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckLCAmtBeforeUpdate
   Description: This method will return a warning message if any of the partial receipt lines
needs to recalculate container landed costs. The user will be asked if he wants to
continue to receive the line(s) or undo update to review the container landed
costs first.
   OperationID: CheckLCAmtBeforeUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckLCAmtBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckLCAmtBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckOnLeaveHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckOnLeaveHead
   Description: This method needs to be run when leaving the RcvHead record either by going to another
RcvHead record or leaving the screen.  It checks that the landed cost has been evenly
disbursed between all the lines.  If not, the landed cost needs to be corrected before
leaving
It also verifies that attachements have been entered for all the parts which require them.
   OperationID: CheckOnLeaveHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOnLeaveHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOnLeaveHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPOClosedInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPOClosedInfo
   Description: This method checks how many numbers of PO Releases are closed in the current PONum
   OperationID: CheckPOClosedInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPOClosedInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPOClosedInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistsRcvHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsRcvHead
   Description: Check if RcvHead already exists in DB.
   OperationID: ExistsRcvHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsRcvHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsRcvHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistsRcvHeadWithDifferentPO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsRcvHeadWithDifferentPO
   Description: Check if the already existing RcvHead has a different PONum than the one that is being tried to receive.
   OperationID: ExistsRcvHeadWithDifferentPO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsRcvHeadWithDifferentPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsRcvHeadWithDifferentPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIdChkContainerID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIdChkContainerID
   Description: This method throws an error if the entered pack slip is for a container receipt,
used in place of GetByID
   OperationID: GetByIdChkContainerID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIdChkContainerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIdChkContainerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRcvHeadWithPONum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRcvHeadWithPONum
   Description: Override of GetNewRcvHead() but with PONum so that we it can be used to default values
   OperationID: GetNewRcvHeadWithPONum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRcvHeadWithPONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvHeadWithPONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendorInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendorInfo
   Description: This method returns default information for the Vendor.
   OperationID: GetVendorInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendorInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RcvHeadNegInvCheck(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RcvHeadNegInvCheck
   Description: Called to check for negative inventory on RcvHead before delete or unreceive
   OperationID: RcvHeadNegInvCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RcvHeadNegInvCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RcvHeadNegInvCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeHdrReceived(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeHdrReceived
   Description: This method should be invoked when the Received flag in RcvHead has changed.
   OperationID: OnChangeHdrReceived
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeHdrReceived_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHdrReceived_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeHdrTaxRegionCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeHdrTaxRegionCode
   Description: Change RcvHead Tax Region Code
   OperationID: OnChangeHdrTaxRegionCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeHdrTaxRegionCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHdrTaxRegionCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeContainerImportFld(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeContainerImportFld
   Description: This method is to be run from Container Receipt Entry when import Number or Imported From values
are changed on the Container.
   OperationID: OnChangeContainerImportFld
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeContainerImportFld_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeContainerImportFld_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedHeaderTaxManual(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedHeaderTaxManual
   Description: Method to call when the Manual Tax Flag has Changed from True to False.  Updates RcvHeadTax
tax amounts based on the new tax percent.
   OperationID: OnChangedHeaderTaxManual
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedHeaderTaxManual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedHeaderTaxManual_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeHeaderTaxFixedAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeHeaderTaxFixedAmount
   Description: Method to call when changing the fixed amount on a tax record.  Updates RcvHeadTax
tax amounts based on the new fixed amount.
   OperationID: OnChangeHeaderTaxFixedAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxFixedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxFixedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeHeaderTaxTaxPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeHeaderTaxTaxPercent
   Description: Method to call when changing the tax percent on a tax record.  Updates RcvHeadTax
tax amounts based on the new tax percent.
   OperationID: OnChangeHeaderTaxTaxPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeHeaderTaxRateCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeHeaderTaxRateCode
   Description: Method to call when changing the tax percent on a tax record.  Updates RcvHeadTax
tax amounts based on the new tax percent.
   OperationID: OnChangeHeaderTaxRateCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeHeaderTaxRateCodeMaster(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeHeaderTaxRateCodeMaster
   Description: Method to call when changing the rate code on a tax record.  Validates the rate and tax code
   OperationID: OnChangeHeaderTaxRateCodeMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxRateCodeMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxRateCodeMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeHeaderTaxReportableAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeHeaderTaxReportableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates RcvHeadTax
tax amounts based on the new taxable amount.
   OperationID: OnChangeHeaderTaxReportableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxReportableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxReportableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeHeaderTaxTaxableAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeHeaderTaxTaxableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates RcvHeadTax
tax amounts based on the new taxable amount.
   OperationID: OnChangeHeaderTaxTaxableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeHeaderTaxTaxAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeHeaderTaxTaxAmt
   Description: Method to call when changing the fixed tax amount on a tax record.  Updates RcvHeadTax
tax amounts based on the new tax amount.
   OperationID: OnChangeHeaderTaxTaxAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeHeaderTaxTaxCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeHeaderTaxTaxCode
   Description: Method to call when changing the tax code on a RcvHeadTax record.  Validates the tax code and
updates RcvHeadTax tax amounts based on the new tax code.
   OperationID: OnChangeHeaderTaxTaxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeHeaderTaxTaxDeductable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeHeaderTaxTaxDeductable
   Description: Method to call when changing the tax deductable on a tax record.  Updates RcvHeadTax
tax amounts based on the new tax percent.
   OperationID: OnChangeHeaderTaxTaxDeductable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeHeaderTaxTaxDeductable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHeaderTaxTaxDeductable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AutoSetToLocation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoSetToLocation
   Description: This procedure sets RcvDtl.SetToLocation to yes in given data set.
If the receipt line is associated with a PCID then only update if the PCID is EMPTY.
If mass receipts only update if not associated with a PCID regardless of status.
   OperationID: AutoSetToLocation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoSetToLocation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoSetToLocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AutoSetToLocationToDflt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoSetToLocationToDflt
   Description: This procedure sets RcvDtl.SetToLocation to yes in given data set.
To be used to set the part location or the default receiving whse
from plant/company depending on the preset SetToLocation flag
If the receipt line is associated with a PCID then only update if the PCID is EMPTY.
If mass receipts only update if not associated with a PCID regardless of status.
   OperationID: AutoSetToLocationToDflt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoSetToLocationToDflt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoSetToLocationToDflt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDtlBeforeUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDtlBeforeUpdate
   Description: This method is to be called right before the update method is called.  If there
is a discrepancy between the vendorqty and ourqty, the user will be asked if they're
sure they want to continue.
   OperationID: CheckDtlBeforeUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDtlBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDtlBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDtlCompliance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDtlCompliance
   Description: .
   OperationID: CheckDtlCompliance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDtlCompliance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDtlCompliance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDtlJobStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDtlJobStatus
   Description: This method is to be run before the GetDtlPOLine and GetDtlPORel and GetDtlJobInfo methods
are called If the Job/PO to a closed or complete job, a question or a warning will be returned
   OperationID: CheckDtlJobStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDtlJobStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDtlJobStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDtlLotInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDtlLotInfo
   Description: This method returns an error or question if the LotNum field does not exist
depending upon the security of the user
   OperationID: CheckDtlLotInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDtlLotInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDtlLotInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDtlSeqChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDtlSeqChange
   Description: This method is run when the JobSeq field is changed along with GetSeqInfo.
If the JobMtl is marked as IssuedComplete, the user is asked whether they are sure
they want to change the sequence number.  Only move forward if the answer is yes.
   OperationID: CheckDtlSeqChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDtlSeqChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDtlSeqChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDtlSSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDtlSSN
   Description: This method tests to see if Serial Numbers exist that may be deleted if the
ReceivedTo field or PartNum changes.  The update method assumes the user answered yes
and will delete the Serial Numbers.
   OperationID: CheckDtlSSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDtlSSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDtlSSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckIssuedComplete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckIssuedComplete
   Description: This method is to be run after the IssuedComplete flag is changed.  Any questions
returned require a yes/no response from the user.
   OperationID: CheckIssuedComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIssuedComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIssuedComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckReceivedComplete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckReceivedComplete
   Description: This method is to be run after the ReceivedComplete flag is changed.  Any questions
returned require a yes/no response from the user.
   OperationID: CheckReceivedComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckReceivedComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckReceivedComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSupplierPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSupplierPrice
   Description: This method validates that if Supplier Price was change it satisfies Company options.
   OperationID: CheckSupplierPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSupplierPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSupplierPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_chkUnReceive(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method chkUnReceive
   Description: Checks if the SMI Receipt has been transfered to a standard BIN
   OperationID: chkUnReceive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/chkUnReceive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/chkUnReceive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreatePartLot(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreatePartLot
   Description: Purpose: Create a PartLot on the fly
Parameters:  none
Notes:
   OperationID: CreatePartLot
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreatePartLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePartLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlAssemblyInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlAssemblyInfo
   Description: This method updates the dataset when the AssemblySeq number changes
   OperationID: GetDtlAssemblyInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlAssemblyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlAssemblyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlJobInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlJobInfo
   Description: This method default the  Job Information when the RcvDtl.JobNum field changes
   OperationID: GetDtlJobInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlJobInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlJobInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlLotInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlLotInfo
   Description: This method updates the unitCost when the LotNum field changes
   OperationID: GetDtlLotInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlLotInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlLotInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlPartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlPartInfo
   Description: This method updates the dataset when the part number has changed.
CheckDtlSSN should be run first.
   OperationID: GetDtlPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlPOInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlPOInfo
   Description: This method updates the dataset when the detail Line PONum field has changed.
   OperationID: GetDtlPOInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlPOInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlPOInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlPOLineInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlPOLineInfo
   Description: This method updates the dataset when the detail Line POLine field has changed.
   OperationID: GetDtlPOLineInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlPOLineInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlPOLineInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlPORelInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlPORelInfo
   Description: This method updates the dataset when the detail Line PORelNum field has changed.
   OperationID: GetDtlPORelInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlPORelInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlPORelInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlQtyInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlQtyInfo
   Description: This method updates the dataset when the InputOurQty field changes
   OperationID: GetDtlQtyInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlQtyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlQtyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateOurQtyFromAttributes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateOurQtyFromAttributes
   Description: This method gets total and sets OurQty when the InputOurQty field changes
   OperationID: UpdateOurQtyFromAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateOurQtyFromAttributes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateOurQtyFromAttributes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlRcvdToInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlRcvdToInfo
   Description: This method is run when the ReceivedTo field is changed after the CheckSSN method is called
   OperationID: GetDtlRcvdToInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlRcvdToInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlRcvdToInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlSeqInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlSeqInfo
   Description: This method updates the dataset when the JobSeq field changes.  Fields will be defaulted
from JobMtl for PUR-MTL and from JobOper for PUR-SUB.
   OperationID: GetDtlSeqInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlSeqInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlSeqInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlVenQtyInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlVenQtyInfo
   Description: This method updates the dataset when the VendorQty field changes
   OperationID: GetDtlVenQtyInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlVenQtyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlVenQtyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLotImportInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLotImportInfo
   Description: This method should be called from Container Receipt Entry and Receipt Entry when the
ImportNumber or ImportedFromDesc values have changed for a receipt line.
   OperationID: GetLotImportInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLotImportInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLotImportInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRcvDtlMisc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRcvDtlMisc
   Description: This method creates a new Miscellaneous receipt line entry
   OperationID: GetNewRcvDtlMisc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRcvDtlMisc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvDtlMisc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartXRefInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartXRefInfo
   Description: This method will review if the entered part exists in any other PartXRef table.
CheckDtlSSN should be run first.
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DisplayWarnMsg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DisplayWarnMsg
   OperationID: DisplayWarnMsg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisplayWarnMsg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisplayWarnMsg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LCChangeLCAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LCChangeLCAmt
   Description: This method updates the dataset record when the LCAmt field changes
   OperationID: LCChangeLCAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LCChangeLCAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LCChangeLCAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedDtlPOTransValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedDtlPOTransValue
   Description: This method should be invoked when the POTransValue of RcvDtl has changed.
   OperationID: OnChangedDtlPOTransValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedDtlPOTransValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedDtlPOTransValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlBinNum
   Description: This method should be invoked when the BinNum on the receipt line changes
If the receipt line is associated with a planning contract it will validate if the Bin against the planning contract header.
   OperationID: OnChangeDtlBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlCommodity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlCommodity
   Description: This method should be invoked when the CommodityCode in RcvDtl changes.
This method will validate the commodity code and get defaults.
   OperationID: OnChangeDtlCommodity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlCommodity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlCommodity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlCountryNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlCountryNum
   Description: This method should be invoked when the OrigCountryNum in RcvDtl changes.
This method will validate country of origin.
   OperationID: OnChangeDtlCountryNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlCountryNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlCountryNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlLCIndCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlLCIndCost
   Description: This method should be invoked when the LCIndCost in RcvDtl changes.
This method will validate the manually disbursed indirect cost.
   OperationID: OnChangeDtlLCIndCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlLCIndCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlLCIndCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRcvDtlLCIndCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRcvDtlLCIndCost
   Description: Get sum of LCIndCost value for RcvDtl rows
   OperationID: GetRcvDtlLCIndCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRcvDtlLCIndCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRcvDtlLCIndCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlPCID
   Description: This method should be invoked when the Receipt line PCID has changed and it will validate if it exists on the Inventory (EMPTY / STOCK) or
Staged (EMPTY / ARRIVED) PCID tables. If the PCID is not EMPTY and it is situated in a different location to that of the receipt line it will change the
warehouse / bin on the receipt line to match that of the PCID Header.
   OperationID: OnChangeDtlPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlPOSelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlPOSelected
   Description: This method is called when a PO has been selected on Mass Receipt process.
Returns an Exception or a Warning if the PO is not approved/confirmed, depending on Company Config.
   OperationID: OnChangeDtlPOSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlPOSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlPOSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlSelectedSinglePO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlSelectedSinglePO
   Description: This method is called when a PO has been selected on Mass Receipt process. This method checks a single PO
and does not send the ReceiptTableset for better performance.
Returns an Exception or a Warning if the PO is not approved/confirmed, depending on Company Config.
   OperationID: OnChangeDtlSelectedSinglePO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlSelectedSinglePO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlSelectedSinglePO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlReceived(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlReceived
   Description: This method should be invoked when the Received flag in RcvDtl has changed.
   OperationID: OnChangeDtlReceived
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlReceived_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlReceived_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlReceiptType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlReceiptType
   Description: This method should be invoked when the Receipt Type in RcvDtl has changed.
   OperationID: OnChangeDtlReceiptType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlReceiptType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlReceiptType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlReceiptTypeTranType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlReceiptTypeTranType
   Description: /// This method should be invoked when the Receipt Type or TranType in RcvDtl has changed. This will reset all fields.
   OperationID: OnChangeDtlReceiptTypeTranType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlReceiptTypeTranType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlReceiptTypeTranType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlSupplierPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlSupplierPrice
   Description: This method should be invoked when the Supplier Price in RcvDtl changes.
This method calculates Base and Reporting values.
   OperationID: OnChangeDtlSupplierPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlSupplierPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlSupplierPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlTaxCatID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlTaxCatID
   Description: This method should be invoked when TaxCatID changes and is used to set the Taxable flag
   OperationID: OnChangeDtlTaxCatID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlTaxCatID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlTaxCatID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlTaxExempt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlTaxExempt
   Description: This method should be invoked when TaxExempt changes and is used to set the Taxable flag
   OperationID: OnChangeDtlTaxExempt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlTaxExempt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlTaxExempt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlUpliftPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlUpliftPercent
   Description: This method should be invoked when the UpliftPercent in RcvDtl changes.
This method will validate the UpliftPercent and calculate the Uplift Indirect Cost.
   OperationID: OnChangeDtlUpliftPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlUpliftPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlUpliftPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeReceiptDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeReceiptDate
   Description: This method should be invoked when the Receipt Date on the header or on the lines changes.
If the receipt date is from header, it must receive as parameter partNum = "" and poLine = 0, otherwise you must receive the correct values.
In this method you can identify the lines where the receipt date can be changed or not.
   OperationID: OnChangeReceiptDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeReceiptDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeReceiptDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDtlWareHouseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDtlWareHouseCode
   Description: This method should be invoked when the Warehouse on the receipt line changes.
If the receipt line is associated with a planning contract it will validate that the warehouse matches that of a contract and will prompt the user to confirm.
If the receipt line contains serial numbers it will check if the warehouse supports full tracking and if not will warn the user that it will delete the serial numbers.
   OperationID: OnChangeDtlWareHouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDtlWareHouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDtlWareHouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeInspReq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeInspReq
   Description: This method updates the dataset when the Inspection Required flag changes
   OperationID: OnChangeInspReq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInspReq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInspReq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RcvDtlNegInvCheck(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RcvDtlNegInvCheck
   Description: Called to check for negative inventory on RcvDtl before delete or unreceive
   OperationID: RcvDtlNegInvCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RcvDtlNegInvCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RcvDtlNegInvCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetToLocation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetToLocation
   Description: This method gets the Warehouse and Bin to the defaults for the Part/Job
   OperationID: SetToLocation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetToLocation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetToLocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PendingRcvDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PendingRcvDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RcvDtlAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlAttrValueSetRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RcvDtlAttrValueSetRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RcvDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RcvDtlTaxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDutyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RcvDutyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RcvHeadAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RcvHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RcvHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvHeadTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RcvHeadTaxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvMiscRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RcvMiscRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvMiscTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RcvMiscTaxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SNFormatRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SupplierXRefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SupplierXRefRow] = obj["value"]
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

class Erp_Tablesets_PendingRcvDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORel:int = obj["PORel"]
      self.PartNum:str = obj["PartNum"]
      self.LineDesc:str = obj["LineDesc"]
      self.OurQuantity:int = obj["OurQuantity"]
      self.UOM:str = obj["UOM"]
      self.JobNum:str = obj["JobNum"]
      self.Type:str = obj["Type"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvDtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
      self.PackLine:int = obj["PackLine"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvDtlAttrValueSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Indentifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Supplier master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Supplier purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Supplier Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      """  Unique identifier for this Attribute Value for this receipt detail.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  Dynamic Attribute Value Set ID for this receipt detail.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.OurQty:int = obj["OurQty"]
      """  Receipt quantity in our unit of measure for this attribute set.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether the Attribute Value was auto-generated by the system.  """  
      self.PUM:str = obj["PUM"]
      """  Supplier selling Unit of Measure.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the Supplier unit of measure.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.NumberOfPiecesUOM:str = obj["NumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  Indicates if the receipt is pending inspection.  Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  """  
      self.InspectionReq:bool = obj["InspectionReq"]
      """  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectedDate:str = obj["InspectedDate"]
      """  Date when item was inspected.  """  
      self.InspectedTime:int = obj["InspectedTime"]
      """  Time of day when inspection transaction was recorded.  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number on which this receipt detail was invoiced. This is updated from the A\P invoice entry process.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line on which this receipt detail was invoiced. Updated by the A\P invoice entry process.  """  
      self.PartNum:str = obj["PartNum"]
      """  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location of the warehouse which received the item. Only applicable for a receipt of Stock.  """  
      self.OurQty:int = obj["OurQty"]
      """  Receipt quantity in our unit of measure.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that received the item. Only applicable for receipt to Job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.TranReference:str = obj["TranReference"]
      """  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.VendorUnitCost:int = obj["VendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  """  
      self.ReceiptType:str = obj["ReceiptType"]
      """  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  """  
      self.ReceivedTo:str = obj["ReceivedTo"]
      """  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  """  
      self.ReceivedComplete:bool = obj["ReceivedComplete"]
      """   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.PUM:str = obj["PUM"]
      """  Vendor's selling Unit of Measure.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Vendor's Part Number. Defaulted from PODetail.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.NumLabels:int = obj["NumLabels"]
      """  Number of labels  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.InspectionReq:bool = obj["InspectionReq"]
      """  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """   Indicates if the receipt is pending inspection.
Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectedDate:str = obj["InspectedDate"]
      """  Date when item was inspected.  """  
      self.InspectedTime:int = obj["InspectedTime"]
      """   Time of day when inspection transaction was recorded.
(seconds since midnight format)  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt date. Mirror image of related RCVHead.ReceiptDate.  Maintained by the RcvHead/RcvDtl write triggers.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  DMRs use Reason type "D".  Only used if failing quantity from inspection.  """  
      self.TotCostVariance:int = obj["TotCostVariance"]
      """  Total Purchase Price Variance amount placed on a receipt in inspection when the variance is received.  Only set if the receipt is currently in inspection (not moved to DMR, job, or stock).  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.NonConformnce:bool = obj["NonConformnce"]
      """  Indicates if the transaction is a non-conformance type transaction.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this part.  """  
      self.OurMtlBurUnitCost:int = obj["OurMtlBurUnitCost"]
      """   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPurPoint:str = obj["GlbPurPoint"]
      """  Global Purchase Point identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackSlip:str = obj["GlbPackSlip"]
      """  Global Packing Slip identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackLine:int = obj["GlbPackLine"]
      """  Global Packing Slip Line identifier.  Used in Consolidated Purchasing.  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.Volume:int = obj["Volume"]
      """  Container volume, frequently specified in cubic sq feet.  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Reporting currency value of this field  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Num related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number of the sales order line related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrigCountryNum:int = obj["OrigCountryNum"]
      """  Country Number of the Origin Country (defaults from Part Country of Origin).  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.LCDutyAmt:int = obj["LCDutyAmt"]
      """  Duty Amount portion of the landed cost for this receipt line.  """  
      self.LCIndCost:int = obj["LCIndCost"]
      """  Indirect Cost portion of the landed cost for this receipt line.  """  
      self.POTransValue:int = obj["POTransValue"]
      """  This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  """  
      self.ExtTransValue:int = obj["ExtTransValue"]
      """  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  """  
      self.Received:bool = obj["Received"]
      """  Flag to indicate that the receipt line has been received.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System (HS) goods classification code.  """  
      self.POType:str = obj["POType"]
      """  Identifier of associated PO ('Std', 'CMI', 'SMI')  """  
      self.AutoReceipt:bool = obj["AutoReceipt"]
      """  Flag representing whether or not this receipt was auto generated by the consumption process (GenSMIReceipt.p).  This is only pertinent for SMI type PO Receipts.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the shipment detail arrived. Defaults as current system date.  """  
      self.LCSpecLineDutyAmt:int = obj["LCSpecLineDutyAmt"]
      """  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  """  
      self.LCUpliftIndCost:int = obj["LCUpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.LCAmt:int = obj["LCAmt"]
      """  The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.LCMtlBurUnitCost:int = obj["LCMtlBurUnitCost"]
      """  Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  """  
      self.DocVendorUnitCost:int = obj["DocVendorUnitCost"]
      """  PO currency value of this field  """  
      self.Rpt1VendorUnitCost:int = obj["Rpt1VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2VendorUnitCost:int = obj["Rpt2VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3VendorUnitCost:int = obj["Rpt3VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its destination, that can be Inventory, Job Material, Job Subcontract, Sales Order.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.MangCustNum:int = obj["MangCustNum"]
      """  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  Originally defaults from PORel.MangCustNum.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegNumCnfg.  """  
      self.ICPackNum:int = obj["ICPackNum"]
      """  Relation between this RcvDtl and the ShipHead.PackNum where this Intercompany Shipment originated.  """  
      self.ShipRcv:str = obj["ShipRcv"]
      """  Shipment Received  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  Can be different from value on header.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  Can be different from value on header.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  Can be different from Header value.  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyOption:str = obj["QtyOption"]
      """  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  """  
      self.ConvOverride:bool = obj["ConvOverride"]
      """  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.SMITransNum:int = obj["SMITransNum"]
      """  Used to identify what has been consumed during an SMI Receipt for a particular transaction.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.Delivered:bool = obj["Delivered"]
      """  Delivered  """  
      self.DeliveredComments:str = obj["DeliveredComments"]
      """  DeliveredComments  """  
      self.InOurCost:int = obj["InOurCost"]
      """  Internal usage for inclusive taxes - Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.DocInUnitCost:int = obj["DocInUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.Rpt1InUnitCost:int = obj["Rpt1InUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitCost:int = obj["Rpt2InUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitCost:int = obj["Rpt3InUnitCost"]
      """  Reporting currency value of this field  """  
      self.InVendorUnitCost:int = obj["InVendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  """  
      self.DocInVendorUnitCost:int = obj["DocInVendorUnitCost"]
      """  PO currency value of this field  """  
      self.Rpt1InVendorUnitCost:int = obj["Rpt1InVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2InVendorUnitCost:int = obj["Rpt2InVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3InVendorUnitCost:int = obj["Rpt3InVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.SupplierUnInvcReceiptQty:int = obj["SupplierUnInvcReceiptQty"]
      """  Value that indicates the remaining quantity of the receipt that is waiting to be invoiced.  """  
      self.OurUnInvcReceiptQty:int = obj["OurUnInvcReceiptQty"]
      """  Value that indicates the un-invoiced quantity of the receipt.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  ** NOT USED TO BE DROPPED 10.2 ** The Tax Liability for this Receipt line  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Receipt line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Indicates if the Receipt line is Taxable  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this item is exempt from tax for this receipt line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the tax info.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a receipt line, if this is set to True the tax engine will not calculate any receipt detail line tax information  """  
      self.InAppliedLCVariance:int = obj["InAppliedLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  """  
      self.InAppliedRcptLCAmt:int = obj["InAppliedRcptLCAmt"]
      """  Internal usage for inclusive taxes - The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  """  
      self.InLCAmt:int = obj["InLCAmt"]
      """  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCDutyAmt:int = obj["InLCDutyAmt"]
      """  Internal usage for inclusive taxes - Duty Amount portion of the landed cost for this receipt line.  """  
      self.InLCIndCost:int = obj["InLCIndCost"]
      """  Internal usage for inclusive taxes - Indirect Cost portion of the landed cost for this receipt line.  """  
      self.InLCMtlBurUnitCost:int = obj["InLCMtlBurUnitCost"]
      """  Internal usage for inclusive taxes - Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  """  
      self.InLCSpecLineDutyAmt:int = obj["InLCSpecLineDutyAmt"]
      """  Internal usage for inclusive taxes - This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCUpliftIndCost:int = obj["InLCUpliftIndCost"]
      """  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InPOTransValue:int = obj["InPOTransValue"]
      """  Internal usage for inclusive taxes - This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  ProjProcessed  """  
      self.ExtNonRecoverableCost:int = obj["ExtNonRecoverableCost"]
      """  This will contain the non deductable tax portion for this Receipt line.  This will be calculated based on the Receipt Header or Receipt Line tax records depending on the Tax Liability type and Company Tax Configuration.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.AttributeBackoutRequired:bool = obj["AttributeBackoutRequired"]
      """  AttributeBackoutRequired  """  
      self.CNDeclarationBillLine:int = obj["CNDeclarationBillLine"]
      """  CNDeclarationBillLine  """  
      self.AllowLCUpdate:bool = obj["AllowLCUpdate"]
      """  Flag to indicate if landed cost info can be updated.  """  
      self.AsmPartDescription:str = obj["AsmPartDescription"]
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      """  Consolidated PO flag.  Used in Consolidated Purchasing.  """  
      self.ContainerExtCost:int = obj["ContainerExtCost"]
      """  This is the extended cost of the container detail item this RcvDtl entry is tied to.  """  
      self.ContainerLCAmt:int = obj["ContainerLCAmt"]
      """  Container Detail Landed Cost Amount  """  
      self.ContractOrder:bool = obj["ContractOrder"]
      self.CostPerFactor:int = obj["CostPerFactor"]
      """  Interger value of CostPerCode  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DisableInspection:bool = obj["DisableInspection"]
      """  Flag to set disable/enable the InspectionReq field.  """  
      self.DisplayUMField:str = obj["DisplayUMField"]
      """  Indicates whether the IUM or DUM field should be displayed/enabled  """  
      self.DocScrUnitCost:int = obj["DocScrUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.DocScrVendorUnitCost:int = obj["DocScrVendorUnitCost"]
      """  PO currency value of this field  """  
      self.DropShipment:bool = obj["DropShipment"]
      """  DropShipment  """  
      self.DueDate:str = obj["DueDate"]
      """  PORel.DueDate  """  
      self.EnableBin:bool = obj["EnableBin"]
      self.EnableDim:bool = obj["EnableDim"]
      """  Indicates whether to enable/disable the dimension fields  """  
      self.EnableInventoryAttributes:bool = obj["EnableInventoryAttributes"]
      """  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  """  
      self.EnableLot:bool = obj["EnableLot"]
      self.EnablePCID:bool = obj["EnablePCID"]
      """  Internal flag used for the row rules to control whether the PCID columns should be enabled or not.  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  Indicates whether to Enable the Serial Number button  """  
      self.EnableSupplierXRef:bool = obj["EnableSupplierXRef"]
      """  Use this field to enable\disable the Supplier Part XRef button  """  
      self.EnableTransValue:bool = obj["EnableTransValue"]
      """  Flag to indicate if PO Trans Value can be updated.  """  
      self.EnableUplift:bool = obj["EnableUplift"]
      """  Flag to indicate if UpliftPercent can be updated.  """  
      self.EnableWhse:bool = obj["EnableWhse"]
      self.ExtCost:int = obj["ExtCost"]
      """  Extended receipt detail cost.  """  
      self.HHReceiveToPCID:bool = obj["HHReceiveToPCID"]
      """  This is true when using the Receive To PCID option in HH PO Receipt.  """  
      self.InputOurQty:int = obj["InputOurQty"]
      """  OurQty not divided by dimension conversion factor for entry.  """  
      self.InspectionFlag:bool = obj["InspectionFlag"]
      """  Flag used to switch other Received To's to Pur-Ins  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Link to the IMRcvDtl table  """  
      self.JobIUM:str = obj["JobIUM"]
      self.JobPartNum:str = obj["JobPartNum"]
      self.JobRequiredQty:int = obj["JobRequiredQty"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.MangCustID:str = obj["MangCustID"]
      self.MangCustName:str = obj["MangCustName"]
      self.ManualLC:bool = obj["ManualLC"]
      """  Flag to indicate if LCIdCost can be manually updated.  """  
      self.MassReceipt:bool = obj["MassReceipt"]
      """  Indicates if created through Mass Receipts  """  
      self.OnTime:str = obj["OnTime"]
      self.OpenRelease:bool = obj["OpenRelease"]
      self.OrderQty:int = obj["OrderQty"]
      self.OurRemQty:int = obj["OurRemQty"]
      """  Our Remaining Quantity  """  
      self.PCIDOutboundContainer:bool = obj["PCIDOutboundContainer"]
      """  Linked to the outbound container flag taken from either the PkgControlStageHeader / PkgControlHeader.  """  
      self.PkgControlStatus:str = obj["PkgControlStatus"]
      """  Package Control Header Status  """  
      self.Plant:str = obj["Plant"]
      """  The Plant to which the warehouse belongs to  """  
      self.POComment:str = obj["POComment"]
      self.PODueDate:str = obj["PODueDate"]
      """  PO Line Due Date  """  
      self.POFactor:int = obj["POFactor"]
      self.POFactorDirection:str = obj["POFactorDirection"]
      self.POHold:bool = obj["POHold"]
      self.POIUM:str = obj["POIUM"]
      self.POPUM:str = obj["POPUM"]
      self.PORelArrivedQty:int = obj["PORelArrivedQty"]
      """  The total quantity that has arrived for this purchase order release.  """  
      self.PORelStatus:str = obj["PORelStatus"]
      """  Indicates the current status of the release. This field is maintained by the System automatically. The possible values are: Open (O), Arrived (A), Inspection (I), Received (R), Closed (C), Voided (V).  """  
      self.RcvdSMIQty:int = obj["RcvdSMIQty"]
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  PORel Received Qty for MassReceipts  """  
      self.RemainingSMIQty:int = obj["RemainingSMIQty"]
      self.Rpt1ScrUnitCost:int = obj["Rpt1ScrUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt1ScrVendorUnitCost:int = obj["Rpt1ScrVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ScrUnitCost:int = obj["Rpt2ScrUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ScrVendorUnitCost:int = obj["Rpt2ScrVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ScrUnitCost:int = obj["Rpt3ScrUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ScrVendorUnitCost:int = obj["Rpt3ScrVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.ScrOurUnitCost:int = obj["ScrOurUnitCost"]
      """  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.ScrVendorUnitCost:int = obj["ScrVendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine  """  
      self.SearchPONum:int = obj["SearchPONum"]
      self.Selected:bool = obj["Selected"]
      self.SetToLocation:bool = obj["SetToLocation"]
      """  This boolean is set by the user in Receipt Entry to initiate the SetToLocation logic for this line.  """  
      self.SkipMaterialQueueCreation:bool = obj["SkipMaterialQueueCreation"]
      """  When this flag is true, skip the Material Queue creation logic for the current RcvDtl line.  """  
      self.SMIComplete:bool = obj["SMIComplete"]
      self.SNStusChanged:bool = obj["SNStusChanged"]
      self.TagMtlSeq:int = obj["TagMtlSeq"]
      """  MtlSeq used in PrintTag option  """  
      self.TagOprSeq:int = obj["TagOprSeq"]
      """  Operation Sequence used in PrintTag  """  
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.ThisTranUOM:str = obj["ThisTranUOM"]
      self.TotalAmt:int = obj["TotalAmt"]
      """  Total amount.  This is the sum of all the other total fields.  """  
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total dedicated Tax amount.  """  
      self.TotDutiesAmt:int = obj["TotDutiesAmt"]
      """  Total duties amount.  This is the sum of RcvDtl.LCSpecLineDutyAmt + RcvDtl.LCDutyAmt  """  
      self.TotLineAmt:int = obj["TotLineAmt"]
      """  Receipt line amount using vendor unit cost.  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total tax amount.  This is the sum of RcvHeadTax.TaxAmt  """  
      self.TotWHTaxAmt:int = obj["TotWHTaxAmt"]
      """  Total WithHolding Tax amount  """  
      self.TranType:str = obj["TranType"]
      """   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  """  
      self.UsePurchaseCode:bool = obj["UsePurchaseCode"]
      self.VendorCurrSymbol:str = obj["VendorCurrSymbol"]
      self.VenRemQty:int = obj["VenRemQty"]
      self.AllowUpdSuppPrice:bool = obj["AllowUpdSuppPrice"]
      """  It is true, if RcvDtl.ReceipteType = 'P' and XbSyst.AllowUpdSuppPrice is true.  """  
      self.AttributeQtyMismatch:bool = obj["AttributeQtyMismatch"]
      """  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  """  
      self.PCIDStatusChanged:bool = obj["PCIDStatusChanged"]
      """  Indicates if the status of the PCID has changed since the receipt took place.  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      self.SerialNoAttributeSetID:int = obj["SerialNoAttributeSetID"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CommodityDescription:str = obj["CommodityDescription"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PackSlipInPrice:bool = obj["PackSlipInPrice"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.PONumConfirmed:bool = obj["PONumConfirmed"]
      self.PONumApprovalStatus:str = obj["PONumApprovalStatus"]
      self.PONumShipToConName:str = obj["PONumShipToConName"]
      self.PONumShipName:str = obj["PONumShipName"]
      self.PONumApprove:bool = obj["PONumApprove"]
      self.PurchCodePurchDesc:str = obj["PurchCodePurchDesc"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointName:str = obj["PurPointName"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvDtlTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  ReportableAmt  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created this record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date and time of the last change to this record  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
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
      self.CollectionType:int = obj["CollectionType"]
      """  CollectionType  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution date.  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date to determine the tax rate.  """  
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
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DocScrDedTaxAmt:int = obj["DocScrDedTaxAmt"]
      self.DocScrReportableAmt:int = obj["DocScrReportableAmt"]
      self.DocScrTaxableAmt:int = obj["DocScrTaxableAmt"]
      self.DocScrTaxAmt:int = obj["DocScrTaxAmt"]
      self.DocScrTaxAmtVar:int = obj["DocScrTaxAmtVar"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.DocScrFixedAmount:int = obj["DocScrFixedAmount"]
      """  Document Fixed Tax Amount  """  
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      """  Reporting currency value of this field  """  
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.RcvDtlPONum:int = obj["RcvDtlPONum"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvDutyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.DutySeq:int = obj["DutySeq"]
      """  Unique Number automatically assigned which is used along with VendorNum, PurPoint, PackSlip and PackLine to uniquely identify the Duty record within the Receipt Line.  """  
      self.TariffCode:str = obj["TariffCode"]
      """  Tariff Code must be for a Preference Scheme that is linked to the Country of Origin.  """  
      self.DutyAmt:int = obj["DutyAmt"]
      """   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount  """  
      self.CommentText:str = obj["CommentText"]
      """  Receipt Line Duty Comments  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InDutyAmt:int = obj["InDutyAmt"]
      """  Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.  """  
      self.AllowLCUpdate:bool = obj["AllowLCUpdate"]
      """  Flag to indicate if landed cost info can be updated.  """  
      self.ScrDutyAmt:int = obj["ScrDutyAmt"]
      """   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TariffDescription:str = obj["TariffDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt Date. Defaults as current system date.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Person that entered the transaction. It is set to the DCD-USERID that was logged on when the record was created . This is not maintainable by the user. This is could be used as a selection parameter for reporting and browsing.  """  
      self.SaveForInvoicing:bool = obj["SaveForInvoicing"]
      """  An internal flag that indicates this receipt document is to be saved for retrieval by A\P invoice entry. This is set based on the value stored in APSyst.SaveForInvoicing.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  An internal flag that indicates "ALL" the details items on this receipt document have been invoiced. This is set to "Yes" when there are no related RcvDtl records where RcvDtl.Invoiced = No. This flag along with the SaveForInvoicing flag are used to present a list of uninvoiced packing slips.  """  
      self.ReceiptComment:str = obj["ReceiptComment"]
      """  Contains comments about the overall Receipt.  """  
      self.ReceivePerson:str = obj["ReceivePerson"]
      """  Short name or initials of person who actually did the receiving. A totally optional field which can be used for internal reference.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  The system date when this record was created.  """  
      self.Plant:str = obj["Plant"]
      """  Site that received the goods.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order.  """  
      self.LCReference:str = obj["LCReference"]
      """  Reference field for Landed Costs  """  
      self.LCComment:str = obj["LCComment"]
      """  Comment field for Landed Costs  """  
      self.LandedCost:int = obj["LandedCost"]
      """  Total amount of landed cost spread amongst the lines.  This amount includes all duties and indirect costs of all lines.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.LCVariance:int = obj["LCVariance"]
      """  This field holds the variance amount for the landed costs.  """  
      self.ICLinked:bool = obj["ICLinked"]
      """  Indicates if linked to a inter-company shipment  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPurPoint:str = obj["GlbPurPoint"]
      """  Global Purchase Point identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackSlip:str = obj["GlbPackSlip"]
      """  Global Packing Slip identifier.  Used in Consolidated Purchasing.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost was disbursed among the container details.  Valid options are Volume (only for po releases tied to a container), Weight, Value and Manual.  """  
      self.AutoReceipt:bool = obj["AutoReceipt"]
      """  This is a flag representing whether or not this is a receipt that was auto generated.  It could only be true if it is associated with an SMI type PO.  """  
      self.AutoTranType:str = obj["AutoTranType"]
      """  Indicates the type of transaction that created this auto receipt.  This field will only be populated if AutoReceipt = true.  """  
      self.POType:str = obj["POType"]
      """  POType Identifier of the associated PO ('Std', 'CMI', or 'SMI')  """  
      self.AutoTranID:int = obj["AutoTranID"]
      """  The unique number of the PartTran record that was the source of this transaction.  This field will only be populated if AutoReceipt = true.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.SpecDutyAmt:int = obj["SpecDutyAmt"]
      """  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the receipt lines using the line tariffs as a factor.  """  
      self.AppliedLCAmt:int = obj["AppliedLCAmt"]
      """  The total Landed Cost Amount disbursed for this receipt.  """  
      self.LCDutyAmt:int = obj["LCDutyAmt"]
      """  The total Duty Amount of the entire receipt.  """  
      self.LCIndCost:int = obj["LCIndCost"]
      """  The total Indirect Cost Amount of the entire receipt.  """  
      self.ApplyToLC:bool = obj["ApplyToLC"]
      """  Flag to indicate if all of the receipt duties and indirect costs needs to be applied or disbursed.  """  
      self.Received:bool = obj["Received"]
      """  Flag to indicate if the entire receipt has been completely received.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the shipment arrived. Defaults as current system date.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount applied for this receipt.  """  
      self.LCUpliftIndCost:int = obj["LCUpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the receipt. The total LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and SpecDutyAmt.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  Default value for lines.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  Default value for lines.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  Default value for lines.  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  if Part.GrossWeightUOM is not known.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AddrList:str = obj["AddrList"]
      """  Address Information from Vendor or VendorPP  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.DispLandedCost:int = obj["DispLandedCost"]
      """  Display field used for container landed costs.  """  
      self.OrigLandedCost:int = obj["OrigLandedCost"]
      """  This field is used to hold the original total landed cost for containers for all plants.  """  
      self.POTypeDesc:str = obj["POTypeDesc"]
      self.AllowLCUpdate:bool = obj["AllowLCUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.AllowUplift:bool = obj["AllowUplift"]
      """  Flag to indicate if UpliftPercent should be enabled.  """  
      self.UpdateDtlRecs:bool = obj["UpdateDtlRecs"]
      """  Flag to indicate if details need to be refreshed after changing the UpliftPercent from header.  """  
      self.eshReceived:bool = obj["eshReceived"]
      """  Logical used to indicate if all details have been received.  """  
      self.PartialReceipt:bool = obj["PartialReceipt"]
      """  Logical indicating whether or not the receipt has been fully received.  If yes then the receipt has only been partially received.  """  
      self.LCMessage:str = obj["LCMessage"]
      """  Landed cost message used to inform the user on retrieval of data that the applied and landed costs do not equal.  """  
      self.UpdateDtlRcptDate:bool = obj["UpdateDtlRcptDate"]
      """  Flag to indicate if receipt details need to be refreshed after changing the Receipt Date from header.  """  
      self.UpdateDtlArvdDate:bool = obj["UpdateDtlArvdDate"]
      """  Flag to indicate if receipt details need to be refreshed after changing the Arrival Date from header.  """  
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointName:str = obj["PurPointName"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.vrPONumShipToConName:str = obj["vrPONumShipToConName"]
      self.vrPONumShipName:str = obj["vrPONumShipName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt Date. Defaults as current system date.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Person that entered the transaction. It is set to the DCD-USERID that was logged on when the record was created . This is not maintainable by the user. This is could be used as a selection parameter for reporting and browsing.  """  
      self.SaveForInvoicing:bool = obj["SaveForInvoicing"]
      """  An internal flag that indicates this receipt document is to be saved for retrieval by A\P invoice entry. This is set based on the value stored in APSyst.SaveForInvoicing.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  An internal flag that indicates "ALL" the details items on this receipt document have been invoiced. This is set to "Yes" when there are no related RcvDtl records where RcvDtl.Invoiced = No. This flag along with the SaveForInvoicing flag are used to present a list of uninvoiced packing slips.  """  
      self.ReceiptComment:str = obj["ReceiptComment"]
      """  Contains comments about the overall Receipt.  """  
      self.ReceivePerson:str = obj["ReceivePerson"]
      """  Short name or initials of person who actually did the receiving. A totally optional field which can be used for internal reference.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  The system date when this record was created.  """  
      self.Plant:str = obj["Plant"]
      """  Site that received the goods.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order.  """  
      self.LCReference:str = obj["LCReference"]
      """  Reference field for Landed Costs  """  
      self.LCComment:str = obj["LCComment"]
      """  Comment field for Landed Costs  """  
      self.LandedCost:int = obj["LandedCost"]
      """  Total amount of landed cost spread amongst the lines.  This amount includes all duties and indirect costs of all lines.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.LCVariance:int = obj["LCVariance"]
      """  This field holds the variance amount for the landed costs.  """  
      self.ICLinked:bool = obj["ICLinked"]
      """  Indicates if linked to a inter-company shipment  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPurPoint:str = obj["GlbPurPoint"]
      """  Global Purchase Point identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackSlip:str = obj["GlbPackSlip"]
      """  Global Packing Slip identifier.  Used in Consolidated Purchasing.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost was disbursed among the container details.  Valid options are Volume (only for po releases tied to a container), Weight, Value and Manual.  """  
      self.AutoReceipt:bool = obj["AutoReceipt"]
      """  This is a flag representing whether or not this is a receipt that was auto generated.  It could only be true if it is associated with an SMI type PO.  """  
      self.AutoTranType:str = obj["AutoTranType"]
      """  Indicates the type of transaction that created this auto receipt.  This field will only be populated if AutoReceipt = true.  """  
      self.POType:str = obj["POType"]
      """  POType Identifier of the associated PO ('Std', 'CMI', or 'SMI')  """  
      self.AutoTranID:int = obj["AutoTranID"]
      """  The unique number of the PartTran record that was the source of this transaction.  This field will only be populated if AutoReceipt = true.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.SpecDutyAmt:int = obj["SpecDutyAmt"]
      """  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the receipt lines using the line tariffs as a factor.  """  
      self.AppliedLCAmt:int = obj["AppliedLCAmt"]
      """  The total Landed Cost Amount disbursed for this receipt.  """  
      self.LCDutyAmt:int = obj["LCDutyAmt"]
      """  The total Duty Amount of the entire receipt.  """  
      self.LCIndCost:int = obj["LCIndCost"]
      """  The total Indirect Cost Amount of the entire receipt.  """  
      self.ApplyToLC:bool = obj["ApplyToLC"]
      """  Flag to indicate if all of the receipt duties and indirect costs needs to be applied or disbursed.  """  
      self.Received:bool = obj["Received"]
      """  Flag to indicate if the entire receipt has been completely received.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the shipment arrived. Defaults as current system date.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount applied for this receipt.  """  
      self.LCUpliftIndCost:int = obj["LCUpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the receipt. The total LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and SpecDutyAmt.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  Default value for lines.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  Default value for lines.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  Default value for lines.  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  if Part.GrossWeightUOM is not known.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Liability for this Receipt  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.HdrTaxNoUpdt:bool = obj["HdrTaxNoUpdt"]
      """  ** NOT USED TO BE DROPPED 10.2 ** This flag determines whether any manual taxes were created for a header miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code - FUTUREUSE  """  
      self.TaxesCalculated:bool = obj["TaxesCalculated"]
      """  The flag indicates that taxes have been calculated.  Once the flag is true is should never be changed back to false.  This will be set to true when any receipt line is marked as received, or when taxes have been calculated via the Calculate All Taxes menu option.  """  
      self.InAppliedLCAmt:int = obj["InAppliedLCAmt"]
      """  Internal usage for inclusive taxes - The total Landed Cost Amount disbursed for this receipt.  """  
      self.InAppliedLCVariance:int = obj["InAppliedLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  """  
      self.InAppliedRcptLCAmt:int = obj["InAppliedRcptLCAmt"]
      """  Internal usage for inclusive taxes - The total Landed Cost Amount applied for this receipt.  """  
      self.InLandedCost:int = obj["InLandedCost"]
      """  Internal usage for inclusive taxes - Total amount of landed cost spread amongst the lines.  This amount includes all duties and indirect costs of all lines.  """  
      self.InLCDutyAmt:int = obj["InLCDutyAmt"]
      """  Internal usage for inclusive taxes - The total Duty Amount of the entire receipt.  """  
      self.InLCIndCost:int = obj["InLCIndCost"]
      """  Internal usage for inclusive taxes - The total Indirect Cost Amount of the entire receipt.  """  
      self.InLCUpliftIndCost:int = obj["InLCUpliftIndCost"]
      """  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the receipt. The total LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and SpecDutyAmt.  """  
      self.InLCVariance:int = obj["InLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the variance amount for the landed costs.  """  
      self.InSpecDutyAmt:int = obj["InSpecDutyAmt"]
      """  Internal usage for inclusive taxes - This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the receipt lines using the line tariffs as a factor.  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      """  Declaration Bill  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  Bonded  """  
      self.APTaxRoundOption:int = obj["APTaxRoundOption"]
      """  APTaxRoundOption  """  
      self.AddrList:str = obj["AddrList"]
      """  Address Information from Vendor or VendorPP  """  
      self.PartialReceipt:bool = obj["PartialReceipt"]
      """  Logical indicating whether or not the receipt has been fully received.  If yes then the receipt has only been partially received.  """  
      self.POLine:int = obj["POLine"]
      self.PORel:int = obj["PORel"]
      self.POTypeDesc:str = obj["POTypeDesc"]
      self.ShipViaDesc:str = obj["ShipViaDesc"]
      self.TotalAmt:int = obj["TotalAmt"]
      """  Total amount.  This is the sum of all the other total fields.  """  
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total dedicated Tax amount.  """  
      self.TotDutiesAmt:int = obj["TotDutiesAmt"]
      """  Total duties amount.  This is the sum of RcvHead.SpecDutyAmt + RcvHead.LCDutyAmt  """  
      self.TotGrossWeight:int = obj["TotGrossWeight"]
      """  Total Gross Weight of all receipt lines  """  
      self.TotGrossWeightUOM:str = obj["TotGrossWeightUOM"]
      """  Qualifies the unit of measure of the Gross Weight field.  """  
      self.TotIndirectCostsAmt:int = obj["TotIndirectCostsAmt"]
      """  Total Indirect Costs amount.  This is a sum of all RcvMisc.ActualAmt.  """  
      self.TotLinesAmt:int = obj["TotLinesAmt"]
      """  Total amount for all receipt lines.  This is the sum of RcvDtl.POTransValue.  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total tax amount.  This is the sum of RcvHeadTax.TaxAmt  """  
      self.TotWeight:int = obj["TotWeight"]
      """  Total Weight of all receipt lines  """  
      self.TotWeightUOM:str = obj["TotWeightUOM"]
      """  Qualifies the unit of measure of the Weight field.  """  
      self.TotWHTaxAmt:int = obj["TotWHTaxAmt"]
      """  Total WithHolding Tax amount  """  
      self.UpdateDtlArvdDate:bool = obj["UpdateDtlArvdDate"]
      """  Flag to indicate if receipt details need to be refreshed after changing the Arrival Date from header.  """  
      self.UpdateDtlRcptDate:bool = obj["UpdateDtlRcptDate"]
      """  Flag to indicate if receipt details need to be refreshed after changing the Receipt Date from header.  """  
      self.UpdateDtlRecs:bool = obj["UpdateDtlRecs"]
      """  Flag to indicate if details need to be refreshed after changing the UpliftPercent from header.  """  
      self.AllowLCUpdate:bool = obj["AllowLCUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.AllowUplift:bool = obj["AllowUplift"]
      """  Flag to indicate if UpliftPercent should be enabled.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.DispLandedCost:int = obj["DispLandedCost"]
      """  Display field used for container landed costs.  """  
      self.eshReceived:bool = obj["eshReceived"]
      """  Logical used to indicate if all details have been received.  """  
      self.IntQueID:int = obj["IntQueID"]
      self.LCMessage:str = obj["LCMessage"]
      """  Landed cost message used to inform the user on retrieval of data that the applied and landed costs do not equal.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.OrigLandedCost:int = obj["OrigLandedCost"]
      """  This field is used to hold the original total landed cost for containers for all plants.  """  
      self.AddrListFormatted:str = obj["AddrListFormatted"]
      """  The formatted address Information from Vendor or VendorPP  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.vrPONumCNBonded:bool = obj["vrPONumCNBonded"]
      self.vrPONumShipToConName:str = obj["vrPONumShipToConName"]
      self.vrPONumShipName:str = obj["vrPONumShipName"]
      self.XbSystReceiptTaxCalculate:bool = obj["XbSystReceiptTaxCalculate"]
      self.XbSystAPTaxLnLevel:bool = obj["XbSystAPTaxLnLevel"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvHeadTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcReportableAmt.  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created this record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date and time of the last change to this record  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
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
      """  Date to determine the tax rate.  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
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
      self.TextCode:str = obj["TextCode"]
      """  TextCode  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.SummaryOnly:bool = obj["SummaryOnly"]
      """  flag to indicate if this record is used only to total detail records,  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.EnableSuperGRate:bool = obj["EnableSuperGRate"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      """  Display field for Rpt1ScrFixedAmount  """  
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      """  Display field for Rpt2FixedAmount  """  
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      """  Display field for Rpt3rFixedAmount  """  
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.ScrDocDedTaxAmt:int = obj["ScrDocDedTaxAmt"]
      self.ScrDocFixedAmount:int = obj["ScrDocFixedAmount"]
      """  Doc Fixed Amount  """  
      self.ScrDocReportableAmt:int = obj["ScrDocReportableAmt"]
      self.ScrDocTaxableAmt:int = obj["ScrDocTaxableAmt"]
      self.ScrDocTaxAmt:int = obj["ScrDocTaxAmt"]
      self.ScrDocTaxAmtVar:int = obj["ScrDocTaxAmtVar"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  FixedAmount  """  
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvMiscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.MiscSeq:int = obj["MiscSeq"]
      """  Unique Number automatically assigned within the Company/VendorNum/PurPoint/PackSlip to uniquely identify each Indirect Costs for this receipt.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Miscellaneous Charge ID that is flagged for Landed Cost  """  
      self.ExcludeFromLC:bool = obj["ExcludeFromLC"]
      """  Flag to indicate if the Indirect Cost is to be excluded from the Landed Cost calculation.  Disabled when IncTransValue is checked.  """  
      self.IncTransValue:bool = obj["IncTransValue"]
      """  Flag to indicate if the Indirect Cost is to be included in the Transaction Value (statistical value) which is used to calculate duties.  Disabled when the ExcludeFromLC is checked.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.ActualAmt:int = obj["ActualAmt"]
      """  Actual Miscellaneous Charge Amount.  """  
      self.DocActualAmt:int = obj["DocActualAmt"]
      """  Actual Miscellaneous Charge Amount in the currency specified.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.CommentText:str = obj["CommentText"]
      """  Receipt Indirect Cost Comments  """  
      self.Rpt1ActualAmt:int = obj["Rpt1ActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.Rpt2ActualAmt:int = obj["Rpt2ActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.Rpt3ActualAmt:int = obj["Rpt3ActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date that will be used to get the exchange rate if the indirect cost is not associated with an invoice miscellaneous charge.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvMsc record.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line from corresponding APInvMsc record.  """  
      self.MscNum:int = obj["MscNum"]
      """  The unique sequence number identifying the AP invoice miscellaneous charge.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.APInvVendorNum:int = obj["APInvVendorNum"]
      """  VendorNum duplicated from the corresponding APInvHed record.  Not directly maintainable by the operator.  """  
      self.PackLine:int = obj["PackLine"]
      """  Reference to RcvDtl.PackLine. An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Receipt Misc. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Indicates if the Indirect Cost is taxable  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  """  
      self.InActualAmt:int = obj["InActualAmt"]
      """  Actual Miscellaneous Charge Amount.  """  
      self.DocInActualAmt:int = obj["DocInActualAmt"]
      """  Actual Miscellaneous Charge Amount in the currency specified.  """  
      self.Rpt1InActualAmt:int = obj["Rpt1InActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.Rpt2InActualAmt:int = obj["Rpt2InActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.Rpt3InActualAmt:int = obj["Rpt3InActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this indirect cost.  """  
      self.RateLabel:str = obj["RateLabel"]
      """  Label for the exchange rate  """  
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total dedicated Tax amount.  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total tax amount  """  
      self.AllowLCUpdate:bool = obj["AllowLCUpdate"]
      """  Flag to indicate if landed cost info can be updated.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for currency "BASE"  """  
      self.ScrActualAmt:int = obj["ScrActualAmt"]
      """  Actual Miscellaneous Charge Amount - Screen value.  """  
      self.Rpt1ScrActualAmt:int = obj["Rpt1ScrActualAmt"]
      """  Reporting currency value of the Actual Amount - Screen value.  """  
      self.Rpt2ScrActualAmt:int = obj["Rpt2ScrActualAmt"]
      """  Reporting currency value of the Actual Amount - Screen value.  """  
      self.Rpt3ScrActualAmt:int = obj["Rpt3ScrActualAmt"]
      """  Reporting currency value of the Actual Amount - Screen value  """  
      self.DocScrActualAmt:int = obj["DocScrActualAmt"]
      """  Actual Miscellaneous Charge Amount in the currency specified - Screen value  """  
      self.BitFlag:int = obj["BitFlag"]
      self.APInvVendorName:str = obj["APInvVendorName"]
      self.APInvVendorVendorID:str = obj["APInvVendorVendorID"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.PurMiscLCDisburseMethod:str = obj["PurMiscLCDisburseMethod"]
      self.PurMiscLCCurrencyCode:str = obj["PurMiscLCCurrencyCode"]
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      self.PurMiscLCAmount:int = obj["PurMiscLCAmount"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.RcvHeadReceiptDate:str = obj["RcvHeadReceiptDate"]
      self.RcvHeadInPrice:bool = obj["RcvHeadInPrice"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.VendorName:str = obj["VendorName"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvMiscTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.MiscSeq:int = obj["MiscSeq"]
      """  Unique Number automatically assigned within the Company/VendorNum/PurPoint/PackSlip to uniquely identify each Indirect Costs for this receipt.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  ** NOT USED TO BE DROPPED 10.2 ** Miscellaneous Charge ID that is flagged for Landed Cost  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  ReportableAmt  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created this record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date and time of the last change to this record  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
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
      self.CollectionType:int = obj["CollectionType"]
      """  CollectionType  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution date.  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date to determine the tax rate.  """  
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
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DocScrDedTaxAmt:int = obj["DocScrDedTaxAmt"]
      self.DocScrReportableAmt:int = obj["DocScrReportableAmt"]
      self.DocScrTaxableAmt:int = obj["DocScrTaxableAmt"]
      self.DocScrTaxAmt:int = obj["DocScrTaxAmt"]
      self.DocScrTaxAmtVar:int = obj["DocScrTaxAmtVar"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.DocScrFixedAmount:int = obj["DocScrFixedAmount"]
      """  Document Fixed Tax Amount  """  
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      """  Reporting currency value of this field  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.RcvMiscCurrencyCode:str = obj["RcvMiscCurrencyCode"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat1:str = obj["SNFormat1"]
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SupplierXRefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.MfgID:str = obj["MfgID"]
      self.MfgName:str = obj["MfgName"]
      self.MfgNum:int = obj["MfgNum"]
      self.MfgPartNum:str = obj["MfgPartNum"]
      self.PartNum:str = obj["PartNum"]
      self.POReference:bool = obj["POReference"]
      self.Receipt:bool = obj["Receipt"]
      self.VendNum:int = obj["VendNum"]
      self.VendPartNum:str = obj["VendPartNum"]
      self.Invoice:bool = obj["Invoice"]
      self.RcvXRefNum:int = obj["RcvXRefNum"]
      """  RcvXRefNum  """  
      self.Inspected:bool = obj["Inspected"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AssignLegalNumber_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   checkforManualPrompt
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Packing Slip  """  
      self.checkforManualPrompt:bool = obj["checkforManualPrompt"]
      """  If true then Get Legal Number defaults and check if Generate Type is manual and set RequiresUserInput appropriately, otherwise just generate Legal Number  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class AssignLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.RequiresUserInput:bool = obj["RequiresUserInput"]
      pass

      """  output parameters  """  

class AutoSetToLocationToDflt_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class AutoSetToLocationToDflt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AutoSetToLocation_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class AutoSetToLocation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CNPreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class CNPreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CalculateReceiptTaxes_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   calledFromUI
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.calledFromUI:bool = obj["calledFromUI"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class CalculateReceiptTaxes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckCNCustomsDeclarationBillLine_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class CheckCNCustomsDeclarationBillLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckCompliance_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Purchase Point Number  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Slip Number  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class CheckCompliance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.compliant:bool = obj["compliant"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckContainersBeforeUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class CheckContainersBeforeUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.qMessageStr:str = obj["parameters"]
      self.qQuestion:str = obj["parameters"]
      self.sMessageStr:str = obj["parameters"]
      self.sQuestion:str = obj["parameters"]
      self.lMessageStr:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckDtlBeforeUpdate_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packLine
   packSlip
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      pass

class CheckDtlBeforeUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.qMessageStr:str = obj["parameters"]
      self.sMessageStr:str = obj["parameters"]
      self.lcMessageStr:str = obj["parameters"]
      self.pcMessageStr:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckDtlCompliance_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packLine
   packSlip
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      pass

class CheckDtlCompliance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.qMessageStr:str = obj["parameters"]
      self.pcMessageStr:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckDtlJobStatus_input:
   """ Required : 
   poNum
   poLine
   poRelNum
   jobNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      """  Purchase Order Number for Receipt  """  
      self.poLine:int = obj["poLine"]
      """  Purchase Order Line  """  
      self.poRelNum:int = obj["poRelNum"]
      """  Purchase Order Release  """  
      self.jobNum:str = obj["jobNum"]
      """  Job Number  """  
      pass

class CheckDtlJobStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.poQuestion:str = obj["parameters"]
      self.questionMsg:str = obj["parameters"]
      self.warnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckDtlLotInfo_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   lotNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.lotNum:str = obj["lotNum"]
      """  New Lot Number to validate  """  
      pass

class CheckDtlLotInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.questionMsg:str = obj["parameters"]
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckDtlSSN_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   receivedTo
   partNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Vendor Purchase Point ID  """  
      self.packSlip:str = obj["packSlip"]
      """  Packing Slip Number  """  
      self.packLine:int = obj["packLine"]
      """  Packing Slip Line  """  
      self.receivedTo:str = obj["receivedTo"]
      """  Receipt ReceivedTo field (proposed or current)  """  
      self.partNum:str = obj["partNum"]
      """  Proposed Receipt Part Number (proposed or current)  """  
      pass

class CheckDtlSSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      self.vWMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckDtlSeqChange_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   jobSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.jobSeq:int = obj["jobSeq"]
      """  The proposed JobSeq value  """  
      pass

class CheckDtlSeqChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckForDefaultRcvInfo_output:
   def __init__(self, obj):
      pass

class CheckHdrBeforeUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class CheckHdrBeforeUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opUpliftWarnMsg:str = obj["parameters"]
      self.opReceiptWarnMsg:str = obj["parameters"]
      self.opArriveWarnMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckIfAttributeQtyMismatch_input:
   """ Required : 
   sysRowID
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      pass

class CheckIfAttributeQtyMismatch_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity  """  
      pass

class CheckIssuedComplete_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   issuedComplete
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.issuedComplete:bool = obj["issuedComplete"]
      pass

class CheckIssuedComplete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckLCAmtBeforeUpdate_input:
   """ Required : 
   ipVendorNum
   ipPurPoint
   ipPackSlip
   ipPackLine
   ds
   """  
   def __init__(self, obj):
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  Receipt Vendor Number  """  
      self.ipPurPoint:str = obj["ipPurPoint"]
      """  Receipt Purchase Point  """  
      self.ipPackSlip:str = obj["ipPackSlip"]
      """  Receipt Packing Number  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  Receipt Line to check  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class CheckLCAmtBeforeUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckMassReceiptChangeWhseBin_input:
   """ Required : 
   contractID
   whse
   bin
   """  
   def __init__(self, obj):
      self.contractID:str = obj["contractID"]
      """  contractID  """  
      self.whse:str = obj["whse"]
      """  warehouse  """  
      self.bin:str = obj["bin"]
      """  bin  """  
      pass

class CheckMassReceiptChangeWhseBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckOnLeaveHead_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number of the Receipt  """  
      self.purPoint:str = obj["purPoint"]
      """  Purchase Point of the Receipt  """  
      self.packSlip:str = obj["packSlip"]
      """  Packing Slip number of the Receipt  """  
      pass

class CheckOnLeaveHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPOClosedInfo_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number of Receipt  """  
      self.purPoint:str = obj["purPoint"]
      """  Purchase Point of Receipt  """  
      self.packSlip:str = obj["packSlip"]
      """  Packing Slip number of Receipt  """  
      pass

class CheckPOClosedInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckReceivedComplete_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   receivedComplete
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.receivedComplete:bool = obj["receivedComplete"]
      pass

class CheckReceivedComplete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckShipmentReceived_input:
   """ Required : 
   packSlip
   poNum
   vendorNum
   """  
   def __init__(self, obj):
      self.packSlip:str = obj["packSlip"]
      """  The PackSlip number  """  
      self.poNum:int = obj["poNum"]
      """  The PO number  """  
      self.vendorNum:int = obj["vendorNum"]
      """  The Vendor number  """  
      pass

class CheckShipmentReceived_output:
   def __init__(self, obj):
      pass

class CheckSupplierPrice_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   suppPrice
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.suppPrice:int = obj["suppPrice"]
      """  new Supplier Price  """  
      pass

class CheckSupplierPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.warningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CommitRcvDtl_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class CommitRcvDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ContainerReceiptsBeforeUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class ContainerReceiptsBeforeUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lcMessage:str = obj["parameters"]
      self.qtyMessage:str = obj["parameters"]
      self.compliantMessage:str = obj["parameters"]
      self.legalRequiresUserInput:bool = obj["legalRequiresUserInput"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ContainerReceiptsUpdate_input:
   """ Required : 
   dsReceipt
   dsContainerTracking
   inContainerID
   ipArrivedDate
   inCreateNewPoRels
   """  
   def __init__(self, obj):
      self.dsReceipt:list[Erp_Tablesets_ReceiptTableset] = obj["dsReceipt"]
      self.dsContainerTracking:list[Erp_Tablesets_ContainerTrackingTableset] = obj["dsContainerTracking"]
      self.inContainerID:int = obj["inContainerID"]
      self.ipArrivedDate:str = obj["ipArrivedDate"]
      self.inCreateNewPoRels:str = obj["inCreateNewPoRels"]
      pass

class ContainerReceiptsUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dsReceipt:list[Erp_Tablesets_ReceiptTableset] = obj["dsReceipt"]
      self.dsContainerTracking:list[Erp_Tablesets_ContainerTrackingTableset] = obj["dsContainerTracking"]
      pass

      """  output parameters  """  

class CreateMassReceipts_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   intQueId
   poNum
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.intQueId:int = obj["intQueId"]
      """  Intercompany Queue ID for Intercompany Receipts  """  
      self.poNum:int = obj["poNum"]
      """  PO Number for Purchase Order Receipts  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class CreateMassReceipts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateMaterialQueueForPCID_input:
   """ Required : 
   pcid
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  The PCID to create MtlQueue record for  """  
      pass

class CreateMaterialQueueForPCID_output:
   def __init__(self, obj):
      pass

class CreatePartLot_input:
   """ Required : 
   partNum
   lotNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.lotNum:str = obj["lotNum"]
      pass

class CreatePartLot_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DisburseLandedCost_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      pass

class DisburseLandedCost_output:
   def __init__(self, obj):
      pass

class DisplayWarnMsg_input:
   """ Required : 
   PartTranType
   JobNum
   AsmSeq
   JobSeq
   """  
   def __init__(self, obj):
      self.PartTranType:str = obj["PartTranType"]
      self.JobNum:str = obj["JobNum"]
      self.AsmSeq:int = obj["AsmSeq"]
      self.JobSeq:int = obj["JobSeq"]
      pass

class DisplayWarnMsg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_ContainerDetailAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ContainerID:int = obj["ContainerID"]
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.ContainerShipQty:int = obj["ContainerShipQty"]
      """  The quantity of the PO Release that is shipped on this container.  """  
      self.ShipQtyUOm:str = obj["ShipQtyUOm"]
      """  UOM of Shipment Quantity.  """  
      self.Comment:str = obj["Comment"]
      """  Free form text describing the container detail.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order on this container.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number on this container  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order on this container.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.Volume:int = obj["Volume"]
      """  Amount of space consumed in the container by this detail line, often specified in cubic square feet.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.LCAmt:int = obj["LCAmt"]
      """  The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.Weight:int = obj["Weight"]
      """  Nett Weight  """  
      self.NetWeightUOM:str = obj["NetWeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost based on our unit of measure.  """  
      self.DocOurUnitCost:int = obj["DocOurUnitCost"]
      """  Unit cost based on our unit of measure in document currency.  """  
      self.Rpt1OurUnitCost:int = obj["Rpt1OurUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2OurUnitCost:int = obj["Rpt2OurUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3OurUnitCost:int = obj["Rpt3OurUnitCost"]
      """  Reporting currency value of this field  """  
      self.OrigCountryNum:int = obj["OrigCountryNum"]
      """  Country Number of the Origin Country from the PO?s Supplier Purchase Point.  """  
      self.ContainerLineRef:str = obj["ContainerLineRef"]
      """  Container shipment line reference or name.  """  
      self.ArrivedQty:int = obj["ArrivedQty"]
      """  Arrived Quantity as reported in the receipt line.  """  
      self.ArrivedQtyUOM:str = obj["ArrivedQtyUOM"]
      """  Unit of Measure of the Arrived Qty.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Received Quantity as reported in the receipt line.  """  
      self.ReceivedQtyUOM:str = obj["ReceivedQtyUOM"]
      """  Unit of Measure of the Received Qty  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  The current status of the container shipment.  Valid values are: Ordered, Shipped, Imported, Arrived and Received.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.LCDutyAmt:int = obj["LCDutyAmt"]
      """  The total Duty Amount portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.LCIndCost:int = obj["LCIndCost"]
      """  The total Indirect Cost portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.POTransValue:int = obj["POTransValue"]
      """  This is by default the PO release value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  """  
      self.ExtTransValue:int = obj["ExtTransValue"]
      """  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  """  
      self.ReceivedDate:str = obj["ReceivedDate"]
      """  The date the container shipment detail is received. Defaults as current system date.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System (HS) goods classification code.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the container shipment detail arrived. Defaults as current system date.  """  
      self.LCSpecLineDutyAmt:int = obj["LCSpecLineDutyAmt"]
      """  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount received for this container shipment line.  """  
      self.LCUpliftIndCost:int = obj["LCUpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  if Part.NetWeightUOM is not known.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Receipt line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Indicates if the Receipt line is Taxable  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this item is exempt from tax for this receipt line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the tax info.  """  
      self.InAppliedLCVariance:int = obj["InAppliedLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  """  
      self.InAppliedRcptLCAmt:int = obj["InAppliedRcptLCAmt"]
      """  Internal usage for inclusive taxes - The total Landed Cost Amount received for this container shipment line.  """  
      self.InExtTransValue:int = obj["InExtTransValue"]
      """  Internal usage for inclusive taxes - This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  """  
      self.InLCAmt:int = obj["InLCAmt"]
      """  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCDutyAmt:int = obj["InLCDutyAmt"]
      """  Internal usage for inclusive taxes - The total Duty Amount portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCIndCost:int = obj["InLCIndCost"]
      """  Internal usage for inclusive taxes - The total Indirect Cost portion of the landed cost for this container detail. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCSpecLineDutyAmt:int = obj["InLCSpecLineDutyAmt"]
      """  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this container detail.  This amount includes the duties and indirect costs per container shipment line.The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCUpliftIndCost:int = obj["InLCUpliftIndCost"]
      """  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the container shipment line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InPOTransValue:int = obj["InPOTransValue"]
      """  Internal usage for inclusive taxes -This is by default the PO release value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a receipt line, if this is set to True the tax engine will not calculate any receipt detail line tax information  """  
      self.BaseWeight:int = obj["BaseWeight"]
      self.BaseWeightUOM:str = obj["BaseWeightUOM"]
      self.ContainerShipped:bool = obj["ContainerShipped"]
      """  Logical used by row rules to determine whether or not the container detail line is read only.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.EnableTransValue:bool = obj["EnableTransValue"]
      """  Flag to indicate if PO Trans Value can be updated.  """  
      self.EnableUplift:bool = obj["EnableUplift"]
      """  Flag to indicate if UpliftPercent can be updated.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended container detail unit cost  """  
      self.IUM:str = obj["IUM"]
      self.ManualLC:bool = obj["ManualLC"]
      """  Flag to indicate if LCIdCost can be manually updated.  """  
      self.OpenPoRelease:bool = obj["OpenPoRelease"]
      """  Indicates if the PO release tied to this detail entry is open or closed.  """  
      self.PartNum:str = obj["PartNum"]
      self.PlantName:str = obj["PlantName"]
      self.PoLineDesc:str = obj["PoLineDesc"]
      self.PORelRcvdQty:int = obj["PORelRcvdQty"]
      """  Quantity already received on this PO Release  """  
      self.PORelRemQty:int = obj["PORelRemQty"]
      """  Remaining Qty  """  
      self.PUM:str = obj["PUM"]
      self.ShipDate:str = obj["ShipDate"]
      """  Container Detail Shipped Date  """  
      self.SupplierPartNum:str = obj["SupplierPartNum"]
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Liability for the associated purchase order.  """  
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      """  Full description of Tax Region.  """  
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.ThisTranUOM:str = obj["ThisTranUOM"]
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total dedicated Tax amount  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total tax amount.  This is the sum of ContainerDetailTax.TaxAmt.  """  
      self.UpdatedKeyRow:bool = obj["UpdatedKeyRow"]
      """  Logical indicates to the UI when a key field has been changed.  Set this to yes if this is the row you want the UI to find and display.  """  
      self.ValidPOInfoEntered:bool = obj["ValidPOInfoEntered"]
      """  Logical indicating that a valid po number, po line and po release has been entered and the user may not update the other container detail values.  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.BaseVolume:int = obj["BaseVolume"]
      self.BaseVolumeUOM:str = obj["BaseVolumeUOM"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains our revision. Default from the PartRev.RevisionNum field.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CommodityDescription:str = obj["CommodityDescription"]
      self.ContainerHeaderContainerDescription:str = obj["ContainerHeaderContainerDescription"]
      self.ContainerHeaderShipDate:str = obj["ContainerHeaderShipDate"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.POHeaderInPrice:bool = obj["POHeaderInPrice"]
      self.PORelBTOOrderNum:int = obj["PORelBTOOrderNum"]
      self.PORelBTOOrderLine:int = obj["PORelBTOOrderLine"]
      self.PORelRefCodeDesc:str = obj["PORelRefCodeDesc"]
      self.PORelPurchasingFactor:int = obj["PORelPurchasingFactor"]
      self.PORelXRelQty:int = obj["PORelXRelQty"]
      self.PORelOpenRelease:bool = obj["PORelOpenRelease"]
      self.PORelRelQty:int = obj["PORelRelQty"]
      self.PORelNeedByDate:str = obj["PORelNeedByDate"]
      self.PORelBTOOrderRelNum:int = obj["PORelBTOOrderRelNum"]
      self.PORelPromiseDt:str = obj["PORelPromiseDt"]
      self.PORelPurchasingFactorDirection:str = obj["PORelPurchasingFactorDirection"]
      self.PORelArrivedQty:int = obj["PORelArrivedQty"]
      self.PORelDueDate:str = obj["PORelDueDate"]
      self.PORelPlant:str = obj["PORelPlant"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerDetailTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  ReportableAmt  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created this record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date and time when the record was last changed.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
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
      self.CollectionType:int = obj["CollectionType"]
      """  CollectionType  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution date.  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date to determine the tax rate.  """  
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
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.EnableSuperGRate:str = obj["EnableSuperGRate"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.DocScrDedTaxAmt:int = obj["DocScrDedTaxAmt"]
      self.DocScrFixedAmount:int = obj["DocScrFixedAmount"]
      self.DocScrReportableAmt:int = obj["DocScrReportableAmt"]
      self.DocScrTaxableAmt:int = obj["DocScrTaxableAmt"]
      self.DocScrTaxAmt:int = obj["DocScrTaxAmt"]
      self.DocScrTaxAmtVar:int = obj["DocScrTaxAmtVar"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerDutyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order on this container.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number on this container  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order on this container.  """  
      self.DutySeq:int = obj["DutySeq"]
      """  Unique Number automatically assigned which is used along with ContainerID, PONum, POLine and PORelNum to uniquely identify the Duty record within the Container Shipment Line.  """  
      self.TariffCode:str = obj["TariffCode"]
      """  Tariff Code must be for a Preference Scheme that is linked to the Country of Origin.  """  
      self.DutyAmt:int = obj["DutyAmt"]
      """   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount  """  
      self.CommentText:str = obj["CommentText"]
      """  Container Duty Comments  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InDutyAmt:int = obj["InDutyAmt"]
      """  InDutyAmt  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.ScrDutyAmt:int = obj["ScrDutyAmt"]
      """   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount - Screen Value  """  
      self.BitFlag:int = obj["BitFlag"]
      self.POHeaderTaxRegionCode:str = obj["POHeaderTaxRegionCode"]
      self.POHeaderInPrice:bool = obj["POHeaderInPrice"]
      self.TariffDescription:str = obj["TariffDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerHeaderAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ContainerID:int = obj["ContainerID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  Date the container is to ship.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Logical indicating if the container has shipped.  """  
      self.ContainerClass:str = obj["ContainerClass"]
      """  Class of this container.  Must be a valid entry in the ContainerClass master file.  """  
      self.ContainerCost:int = obj["ContainerCost"]
      """  Total cost to ship this container.  This is defaulted to the value on the ContainerClass but can be overridden by the end user. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.ShippingDays:int = obj["ShippingDays"]
      """   Lead time it takes for this container to reach its destination.  This is a buffer amount used to offset the shipping date to identify when a shipment is due to arrive.  For example if the shipping days is 30 and the ship date of the container is January 1, the expected arrival date of the container is January 31.

This is intiially defaulted to the value on the ContainerClass but can be overridden by the end user.  """  
      self.ContainerComments:str = obj["ContainerComments"]
      """  Notes/comments about the container shipment.  """  
      self.ContainerDescription:str = obj["ContainerDescription"]
      """  Free form text that describes this particular container.  """  
      self.NewPoRelAtReceipt:bool = obj["NewPoRelAtReceipt"]
      """  Determines if a new PO release is created at receipt when the quantity received is less than the quantity shipped.  The new PO Rel quantity is the difference between the ship quantity and the receipt quantity.  """  
      self.Volume:int = obj["Volume"]
      """  Container volume, frequently specified in cubic sq feet.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default.
Having a Volume UOM will provides the ability to calculate total volume  """  
      self.CostPerVolume:int = obj["CostPerVolume"]
      """  Volume cost of the container.  This is calculated by dividing the container cost by the Volume.  """  
      self.ContainerReference:str = obj["ContainerReference"]
      """  The container reference is typically the shipping company's assigned container ID.  """  
      self.LCReference:str = obj["LCReference"]
      """  Reference information for landed cost.  """  
      self.LCComment:str = obj["LCComment"]
      """  Landed Cost Comments  """  
      self.LCVariance:int = obj["LCVariance"]
      """  This field holds the variance amount for the landed costs.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost (container cost) was disbursed among the container details.  Valid options are Volume (default), Weight, Value and Manual.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.CurrencyDate:str = obj["CurrencyDate"]
      """  Currency Date  """  
      self.DocContainerCost:int = obj["DocContainerCost"]
      """  Total cost to ship this container in the doc currency.  """  
      self.PORelShipOption:str = obj["PORelShipOption"]
      """  Valid values = "Short" and "Create".   At the time a container is shipped, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the shipping quantity and a new PO release is created for the difference between the original po release quantity and the ship quantity.  This is an optional field.  """  
      self.Rpt1ContainerCost:int = obj["Rpt1ContainerCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ContainerCost:int = obj["Rpt2ContainerCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ContainerCost:int = obj["Rpt3ContainerCost"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.LoadPortID:str = obj["LoadPortID"]
      """  Valid Loading Port ID where goods are loaded on the vessel.  """  
      self.DechargePortID:str = obj["DechargePortID"]
      """  Valid port location where goods are unloaded.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  """  
      self.FOB:str = obj["FOB"]
      """  Descriptive code assigned by user which uniquely identifies the fob record.  """  
      self.ContainerCount:int = obj["ContainerCount"]
      """  Number of Containers in this shipment.  """  
      self.PackageCount:int = obj["PackageCount"]
      """  Number of Packages in this shipment.  """  
      self.Weight:int = obj["Weight"]
      """  Total Weight of the shipment.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.ConNum:int = obj["ConNum"]
      """  Carrier (Supplier) Contact number.  Unique identifier for the contact record.  """  
      self.BOLading:str = obj["BOLading"]
      """  Bill of Lading Number  """  
      self.BOExchange:str = obj["BOExchange"]
      """  Bill of Exchange Number  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  The current status of the container shipment.  Valid values are: Ordered, Shipped, Imported, Arrived and Received.  """  
      self.PORelRcptOption:str = obj["PORelRcptOption"]
      """  Valid values = "Short" and "Create".   When the container arrives, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the arrived quantity and a new PO release is created for the difference between the original po release quantity and the arrived quantity.  This is an optional field.  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  """  
      self.Vessel:str = obj["Vessel"]
      """  Name of the vessel containing the shipment.  """  
      self.SpecDutyAmt:int = obj["SpecDutyAmt"]
      """  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the shipment lines using the line tariffs as a factor.  """  
      self.AppliedLCAmt:int = obj["AppliedLCAmt"]
      """  The total Landed Cost Amount disbursed or applied to this container shipment.  """  
      self.ContainerDutyAmt:int = obj["ContainerDutyAmt"]
      """  This is the total Duty Amount of all container shipment lines. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.ContainerIndCost:int = obj["ContainerIndCost"]
      """  This is the total Indirect Cost Amount of the container shipment.  The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.ApplyToLC:bool = obj["ApplyToLC"]
      """  Flag to indicate if all of the shipment duties and indirect costs needs to be applied or disbursed.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the container shipment arrived. Defaults as current system date.  """  
      self.ReceivedDate:str = obj["ReceivedDate"]
      """  The date the container shipment is received. Defaults as current system date.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount received for this container shipment.  """  
      self.UpliftIndCost:int = obj["UpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the container shipment. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.DueDate:str = obj["DueDate"]
      """  The date that the Container Shipment is due to arrive.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AdditionalShippingDays:int = obj["AdditionalShippingDays"]
      """  **NOT USED - REMOVE**  """  
      self.EstimatedArrivalDate:str = obj["EstimatedArrivalDate"]
      """  **NOT USED - Remove **  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Set from the earliest need by date set against the po releases.  """  
      self.PromiseDate:str = obj["PromiseDate"]
      """  Specifies the date on which the supplier has promised to deliver the container.  """  
      self.TaxesCalculated:bool = obj["TaxesCalculated"]
      """  Reflects whether taxes have been calculated  """  
      self.InAppliedLCAmt:int = obj["InAppliedLCAmt"]
      """  Internal usage for inclusive taxes -The total Landed Cost Amount disbursed or applied to this container shipment.  """  
      self.InAppliedLCVariance:int = obj["InAppliedLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  """  
      self.InAppliedRcptLCAmt:int = obj["InAppliedRcptLCAmt"]
      """  Internal usage for inclusive taxes - The total Landed Cost Amount received for this container shipment.  """  
      self.InContainerCost:int = obj["InContainerCost"]
      """  Internal usage for inclusive taxes - Total cost to ship this container.  This is defaulted to the value on the ContainerClass but can be overridden by the end user. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.InContainerDutyAmt:int = obj["InContainerDutyAmt"]
      """  Internal usage for inclusive taxes - This is the total Duty Amount of all container shipment lines. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.InContainerIndCost:int = obj["InContainerIndCost"]
      """  Internal usage for inclusive taxes - This is the total Indirect Cost Amount of the container shipment.  The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.InDocContainerCost:int = obj["InDocContainerCost"]
      """  Internal usage for inclusive taxes - Total cost to ship this container in the doc currency.  """  
      self.InLCAppliedAmt:int = obj["InLCAppliedAmt"]
      """  ** NOT USED TO BE DROPPED 10.2 **  """  
      self.InLCVariance:int = obj["InLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the variance amount for the landed costs.  """  
      self.InSpecDutyAmt:int = obj["InSpecDutyAmt"]
      """  Internal usage for inclusive taxes - This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the shipment lines using the line tariffs as a factor.  """  
      self.InUpliftIndCost:int = obj["InUpliftIndCost"]
      """  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the container shipment. The total ContainerCost is the sum of ContainerIndCost, ContainerDutyAmt, UpliftIndCost and SpecDutyAmt.  """  
      self.DisplayContainerID:str = obj["DisplayContainerID"]
      """  ContainerID in display format.  """  
      self.DispRcptStatus:str = obj["DispRcptStatus"]
      """  Display Receipt Status  """  
      self.DispShipStatus:str = obj["DispShipStatus"]
      """  Display Ship Status.  """  
      self.EnableCalcTaxes:bool = obj["EnableCalcTaxes"]
      """   Flag poplulated from XbSyst.ReceiptTaxCalculate 
Determines if taxes can be calculated at update or via action menu  """  
      self.EnableLCAfterRcpt:bool = obj["EnableLCAfterRcpt"]
      """  Flag to indicate if record can be updated after Receipt.  """  
      self.EnableSplitContainer:bool = obj["EnableSplitContainer"]
      """  Flag to indicate if container details can be split into another container shipment.  """  
      self.EnableTransferCost:bool = obj["EnableTransferCost"]
      """  Flag to indicate if indirect costs can be transferred into another container shipment.  """  
      self.EnableUplift:bool = obj["EnableUplift"]
      """  Flag to indicate if UpliftPercent should be enabled.  """  
      self.eshReceived:bool = obj["eshReceived"]
      """  Logical used to indicate if all po rels for the current plant have been received.  """  
      self.LCAccount:str = obj["LCAccount"]
      """  Landed Cost account for display  """  
      self.LCAccountDesc:str = obj["LCAccountDesc"]
      """  Account Description  """  
      self.LCAppliedAmt:int = obj["LCAppliedAmt"]
      """  Amount of Landed Cost applied  """  
      self.LCMessage:str = obj["LCMessage"]
      """  Landed cost message used to inform the user on retrieval of data that the applied and container costs do not equal.  """  
      self.PartialReceipt:bool = obj["PartialReceipt"]
      """  Logical indicating whether or not the container has been fully receipt.  If yes then the container has only been partially received.  """  
      self.ReceiveAll:bool = obj["ReceiveAll"]
      """  Flag to indicate that all container receipt details will be "received" automatically.  """  
      self.ResetPORelDates:bool = obj["ResetPORelDates"]
      """  Logical indicating whether or not on ship date change or shipping days change the po release due dates are to be upated.  """  
      self.SkipLandedCost:bool = obj["SkipLandedCost"]
      self.TestImportFields:bool = obj["TestImportFields"]
      """  Test Import Fields "ImportNumber" and "ImportedFromDesc" to see if the Receipt Line had already non empty values for these fields and the Lot is set for this Receipt Line.  """  
      self.TotalAmt:int = obj["TotalAmt"]
      """  Total amount.  This is the sum of all the other total fields.  """  
      self.TotalExtCost:int = obj["TotalExtCost"]
      """  Total shipment value  """  
      self.TotalWeight:int = obj["TotalWeight"]
      """  Total weight of the items shipped on the container detail.  """  
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total Deductable Tax Amount  """  
      self.TotDutiesAmt:int = obj["TotDutiesAmt"]
      """  Total duties amount.  """  
      self.TotIndirectCostsAmt:int = obj["TotIndirectCostsAmt"]
      """  Total Indirect Costs amount.  """  
      self.TotLinesAmt:int = obj["TotLinesAmt"]
      """  Total amount for all Container Lines  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax Amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total Tax amount.  """  
      self.TotWHTaxAmt:int = obj["TotWHTaxAmt"]
      """  Total WithHolding Tax Amount  """  
      self.UpdateDtlRecs:bool = obj["UpdateDtlRecs"]
      """  Flag to indicate if container details need to be refreshed after changing the UpliftPercent from header.  """  
      self.UpdIndCosts:bool = obj["UpdIndCosts"]
      self.AllowUpdate:bool = obj["AllowUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.EnableTaxAtLineLevel:bool = obj["EnableTaxAtLineLevel"]
      """   Flag poplulated from XbSyst.APTaxLnLevel.  
Determines if taxes are calculated at line level (true) or document level (false)  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.DisableApplyLandedCost:bool = obj["DisableApplyLandedCost"]
      """  Determine if the Apply Landed Cost button in Kinetic should be disabled.  """  
      self.OkToLeaveContainerHead:bool = obj["OkToLeaveContainerHead"]
      """  Flag to determine for Kinetic if use can leave the Container Header record/screen.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ContainerClassDescription:str = obj["ContainerClassDescription"]
      self.DechargePortDescription:str = obj["DechargePortDescription"]
      self.DechargePortPortID:str = obj["DechargePortPortID"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.LoadPortPortID:str = obj["LoadPortPortID"]
      self.LoadPortDescription:str = obj["LoadPortDescription"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.VendCntPhoneNum:str = obj["VendCntPhoneNum"]
      self.VendCntName:str = obj["VendCntName"]
      self.VendCntFaxNum:str = obj["VendCntFaxNum"]
      self.VendCntEmailAddress:str = obj["VendCntEmailAddress"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorState:str = obj["VendorState"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorName:str = obj["VendorName"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerHeaderTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcReportableAmt.  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created this record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date and time when the record was last changed.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
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
      """  Date to determine the tax rate.  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
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
      self.TextCode:str = obj["TextCode"]
      """  TextCode  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.SummaryOnly:bool = obj["SummaryOnly"]
      """  flag to indicate if this record is used only to total detail records,  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.EnableSuperGRate:bool = obj["EnableSuperGRate"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      """  Display field for Rpt1ScrFixedAmount  """  
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      """  Display field for Rpt2FixedAmount  """  
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      """  Display field for Rpt3rFixedAmount  """  
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.ScrDocDedTaxAmt:int = obj["ScrDocDedTaxAmt"]
      self.ScrDocFixedAmount:int = obj["ScrDocFixedAmount"]
      """  Doc Fixed Amount  """  
      self.ScrDocReportableAmt:int = obj["ScrDocReportableAmt"]
      self.ScrDocTaxableAmt:int = obj["ScrDocTaxableAmt"]
      self.ScrDocTaxAmt:int = obj["ScrDocTaxAmt"]
      self.ScrDocTaxAmtVar:int = obj["ScrDocTaxAmtVar"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  FixedAmount  """  
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerMiscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.MiscSeq:int = obj["MiscSeq"]
      """  Unique Number automatically assigned within the ContainerID to uniquely identify each Indirect Costs for this container shipment.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Miscellaneous Charge ID that is flagged for Landed Cost  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvMsc record.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line from corresponding APInvMsc record.  """  
      self.MscNum:int = obj["MscNum"]
      """  The unique sequence number identifying the AP invoice miscellaneous charge.  """  
      self.ExcludeFromLC:bool = obj["ExcludeFromLC"]
      """  Flag to indicate if the Indirect Cost is to be excluded from the Landed Cost calculation.  Disabled when IncTransValue is checked.  """  
      self.IncTransValue:bool = obj["IncTransValue"]
      """  Flag to indicate if the Indirect Cost is to be included in the Transaction Value (statistical value) which is used to calculate duties.  Disabled when the ExcludeFromLC is checked.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.EstimateAmt:int = obj["EstimateAmt"]
      """  Estimated Amount used in landed cost calculation if actual amount is not available.  """  
      self.DocEstimateAmt:int = obj["DocEstimateAmt"]
      """  Estimated Amount in currency specified.  """  
      self.ActualAmt:int = obj["ActualAmt"]
      """  Actual Amount coming from the posted AP invoice miscellaneous charge.  """  
      self.DocActualAmt:int = obj["DocActualAmt"]
      """  Actual Amount in currency specified.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.CommentText:str = obj["CommentText"]
      """  Container Indirect Cost Comments  """  
      self.Rpt1EstimateAmt:int = obj["Rpt1EstimateAmt"]
      """  Reporting currency value of the Estimated Amount.  """  
      self.Rpt2EstimateAmt:int = obj["Rpt2EstimateAmt"]
      """  Reporting currency value of the Estimated Amount.  """  
      self.Rpt3EstimateAmt:int = obj["Rpt3EstimateAmt"]
      """  Reporting currency value of the Estimated Amount.  """  
      self.Rpt1ActualAmt:int = obj["Rpt1ActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.Rpt2ActualAmt:int = obj["Rpt2ActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.Rpt3ActualAmt:int = obj["Rpt3ActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date that will be used to get the exchange rate if the indirect cost is not associated with an invoice miscellaneous charge.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DocHstEstimateAmt:int = obj["DocHstEstimateAmt"]
      """  Historical Doc Estimate Amount  """  
      self.HstEstimateAmt:int = obj["HstEstimateAmt"]
      """  Historical Estimate Amount  """  
      self.Rpt1HstEstimateAmt:int = obj["Rpt1HstEstimateAmt"]
      """  Historical Rpt1 Estimate Amount  """  
      self.Rpt2HstEstimateAmt:int = obj["Rpt2HstEstimateAmt"]
      """  Historical Rpt2 Estimate Amount  """  
      self.Rpt3HstEstimateAmt:int = obj["Rpt3HstEstimateAmt"]
      """  Historical Rpt3 Estimate Amount  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Indirect Cost. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Indicates if the Indirect Cost is Taxable  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Liability for this Receipt  """  
      self.InEstimateAmt:int = obj["InEstimateAmt"]
      """  Internal usage for inclusive taxes - Estimated Amount used in landed cost calculation if actual amount is not available.  """  
      self.DocInEstimateAmt:int = obj["DocInEstimateAmt"]
      """  Internal usage for inclusive taxes - Estimated Amount in currency specified.  """  
      self.Rpt1InEstimateAmt:int = obj["Rpt1InEstimateAmt"]
      """  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  """  
      self.Rpt2InEstimateAmt:int = obj["Rpt2InEstimateAmt"]
      """  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  """  
      self.Rpt3InEstimateAmt:int = obj["Rpt3InEstimateAmt"]
      """  Internal usage for inclusive taxes - Reporting currency value of the Estimated Amount.  """  
      self.InHstEstimateAmt:int = obj["InHstEstimateAmt"]
      """  Internal usage for inclusive taxes - Historical Estimate Amount  """  
      self.DocInHstEstimateAmt:int = obj["DocInHstEstimateAmt"]
      """  Internal usage for inclusive taxes - Historical Doc Estimate Amount  """  
      self.Rpt1InHstEstimateAmt:int = obj["Rpt1InHstEstimateAmt"]
      """  Internal usage for inclusive taxes - Historical Rpt1 Estimate Amount  """  
      self.Rpt2InHstEstimateAmt:int = obj["Rpt2InHstEstimateAmt"]
      """  Internal usage for inclusive taxes - Historical Rpt2 Estimate Amount  """  
      self.Rpt3InHstEstimateAmt:int = obj["Rpt3InHstEstimateAmt"]
      """  Internal usage for inclusive taxes - Historical Rpt3 Estimate Amount  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for currency "BASE"  """  
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total dedicated Tax amount.  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total tax amount  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this indirect cost.  """  
      self.RateLabel:str = obj["RateLabel"]
      """  Label for ExchangeRate  """  
      self.ScrEstimateAmt:int = obj["ScrEstimateAmt"]
      """  Estimated Amount used in landed cost calculation if actual amount is not available - Screen Value  """  
      self.Rpt1ScrEstimateAmt:int = obj["Rpt1ScrEstimateAmt"]
      """  Reporting currency value of the Estimated Amount - Screen Value  """  
      self.Rpt2ScrEstimateAmt:int = obj["Rpt2ScrEstimateAmt"]
      """  Reporting currency value of the Estimated Amount - Screen value  """  
      self.Rpt3ScrEstimateAmt:int = obj["Rpt3ScrEstimateAmt"]
      """  Reporting currency value of the Estimated Amount - Screen value  """  
      self.ScrHstEstimateAmt:int = obj["ScrHstEstimateAmt"]
      """  Historical Estimate Amount - Screen value  """  
      self.Rpt1ScrHstEstimateAmt:int = obj["Rpt1ScrHstEstimateAmt"]
      """  Historical Rpt1 Estimate Amount - Screen value  """  
      self.Rpt2ScrHstEstimateAmt:int = obj["Rpt2ScrHstEstimateAmt"]
      """  Historical Rpt2 Estimate Amount - Screen value  """  
      self.Rpt3ScrHstEstimateAmt:int = obj["Rpt3ScrHstEstimateAmt"]
      """  Historical Rpt3 Estimate Amount - Screen value  """  
      self.DocScrEstimateAmt:int = obj["DocScrEstimateAmt"]
      """  Estimated Amount in currency specified - Screen value  """  
      self.DocScrHstEstimateAmt:int = obj["DocScrHstEstimateAmt"]
      """  Estimated Amount used in landed cost calculation if actual amount is not available - Screen Value  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.PurMiscLCAmount:int = obj["PurMiscLCAmount"]
      self.PurMiscLCCurrencyCode:str = obj["PurMiscLCCurrencyCode"]
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      self.PurMiscLCDisburseMethod:str = obj["PurMiscLCDisburseMethod"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorName:str = obj["VendorName"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerMiscTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.MiscSeq:int = obj["MiscSeq"]
      """  Unique Number automatically assigned within the Company/VendorNum/PurPoint/PackSlip to uniquely identify each Indirect Costs for this receipt.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  ** NOT USED TO BE DROPPED 10.2 ** The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  ReportableAmt  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created this record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date and time when the record was last changed.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
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
      self.CollectionType:int = obj["CollectionType"]
      """  CollectionType  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution date.  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date to determine the tax rate.  """  
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
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DocScrDedTaxAmt:int = obj["DocScrDedTaxAmt"]
      self.DocScrReportableAmt:int = obj["DocScrReportableAmt"]
      self.DocScrTaxableAmt:int = obj["DocScrTaxableAmt"]
      self.DocScrTaxAmt:int = obj["DocScrTaxAmt"]
      self.DocScrTaxAmtVar:int = obj["DocScrTaxAmtVar"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      self.DocScrFixedAmount:int = obj["DocScrFixedAmount"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ContainerMiscApplyDate:str = obj["ContainerMiscApplyDate"]
      self.ContainerMiscInPrice:bool = obj["ContainerMiscInPrice"]
      self.ContainerMiscCurrencyCode:str = obj["ContainerMiscCurrencyCode"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContainerTrackingTableset:
   def __init__(self, obj):
      self.ContainerHeader:list[Erp_Tablesets_ContainerHeaderRow] = obj["ContainerHeader"]
      self.ContainerHeaderAttch:list[Erp_Tablesets_ContainerHeaderAttchRow] = obj["ContainerHeaderAttch"]
      self.ContainerDetail:list[Erp_Tablesets_ContainerDetailRow] = obj["ContainerDetail"]
      self.ContainerDetailAttch:list[Erp_Tablesets_ContainerDetailAttchRow] = obj["ContainerDetailAttch"]
      self.ContainerDetailTax:list[Erp_Tablesets_ContainerDetailTaxRow] = obj["ContainerDetailTax"]
      self.ContainerDuty:list[Erp_Tablesets_ContainerDutyRow] = obj["ContainerDuty"]
      self.ContainerHeaderTax:list[Erp_Tablesets_ContainerHeaderTaxRow] = obj["ContainerHeaderTax"]
      self.ContainerMisc:list[Erp_Tablesets_ContainerMiscRow] = obj["ContainerMisc"]
      self.ContainerMiscTax:list[Erp_Tablesets_ContainerMiscTaxRow] = obj["ContainerMiscTax"]
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

class Erp_Tablesets_MassReceiptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  """  
      self.PartNum:str = obj["PartNum"]
      """  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location of the warehouse which received the item. Only applicable for a receipt of Stock.  """  
      self.OurQty:int = obj["OurQty"]
      """  Receipt quantity in our unit of measure.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that received the item. Only applicable for receipt to Job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.VendorUnitCost:int = obj["VendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  """  
      self.ReceiptType:str = obj["ReceiptType"]
      """  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  """  
      self.ReceivedTo:str = obj["ReceivedTo"]
      """  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  """  
      self.ReceivedComplete:bool = obj["ReceivedComplete"]
      """   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.PUM:str = obj["PUM"]
      """  Vendor's selling Unit of Measure.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Vendor's Part Number. Defaulted from PODetail.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.OurMtlBurUnitCost:int = obj["OurMtlBurUnitCost"]
      """   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.LCAmt:int = obj["LCAmt"]
      """  The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RefDisplayAccount:str = obj["RefDisplayAccount"]
      self.DueDate:str = obj["DueDate"]
      self.TrackDims:bool = obj["TrackDims"]
      self.PrevRcvDtlRec:bool = obj["PrevRcvDtlRec"]
      self.TrackLots:bool = obj["TrackLots"]
      self.CostPerFactor:int = obj["CostPerFactor"]
      self.PConvFactor:int = obj["PConvFactor"]
      self.ReceivedQty:int = obj["ReceivedQty"]
      self.OurIQty:int = obj["OurIQty"]
      self.OrderQty:int = obj["OrderQty"]
      self.ErrorMsg:str = obj["ErrorMsg"]
      self.ExtCost:int = obj["ExtCost"]
      """  Extended Costs for Landed Costs  """  
      self.DisburseNum:int = obj["DisburseNum"]
      """  Used in Landed Costs  """  
      self.LCVariance:int = obj["LCVariance"]
      self.ExtMtlBurCost:int = obj["ExtMtlBurCost"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.BaseWeight:int = obj["BaseWeight"]
      """  Weight converted to the base UOM defined for the system UOM weight class.  """  
      self.BaseWeightUOM:str = obj["BaseWeightUOM"]
      """  The base UOM defined for the sytem UOM weight class.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MassReceiptTableset:
   def __init__(self, obj):
      self.MassReceipt:list[Erp_Tablesets_MassReceiptRow] = obj["MassReceipt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PendingRcvDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORel:int = obj["PORel"]
      self.PartNum:str = obj["PartNum"]
      self.LineDesc:str = obj["LineDesc"]
      self.OurQuantity:int = obj["OurQuantity"]
      self.UOM:str = obj["UOM"]
      self.JobNum:str = obj["JobNum"]
      self.Type:str = obj["Type"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvDtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
      self.PackLine:int = obj["PackLine"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvDtlAttrValueSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Indentifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Supplier master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Supplier purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Supplier Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      """  Unique identifier for this Attribute Value for this receipt detail.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  Dynamic Attribute Value Set ID for this receipt detail.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.OurQty:int = obj["OurQty"]
      """  Receipt quantity in our unit of measure for this attribute set.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether the Attribute Value was auto-generated by the system.  """  
      self.PUM:str = obj["PUM"]
      """  Supplier selling Unit of Measure.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the Supplier unit of measure.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.NumberOfPiecesUOM:str = obj["NumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  Indicates if the receipt is pending inspection.  Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  """  
      self.InspectionReq:bool = obj["InspectionReq"]
      """  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectedDate:str = obj["InspectedDate"]
      """  Date when item was inspected.  """  
      self.InspectedTime:int = obj["InspectedTime"]
      """  Time of day when inspection transaction was recorded.  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number on which this receipt detail was invoiced. This is updated from the A\P invoice entry process.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line on which this receipt detail was invoiced. Updated by the A\P invoice entry process.  """  
      self.PartNum:str = obj["PartNum"]
      """  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location of the warehouse which received the item. Only applicable for a receipt of Stock.  """  
      self.OurQty:int = obj["OurQty"]
      """  Receipt quantity in our unit of measure.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that received the item. Only applicable for receipt to Job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.TranReference:str = obj["TranReference"]
      """  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.VendorUnitCost:int = obj["VendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  """  
      self.ReceiptType:str = obj["ReceiptType"]
      """  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  """  
      self.ReceivedTo:str = obj["ReceivedTo"]
      """  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  """  
      self.ReceivedComplete:bool = obj["ReceivedComplete"]
      """   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.PUM:str = obj["PUM"]
      """  Vendor's selling Unit of Measure.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Vendor's Part Number. Defaulted from PODetail.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.NumLabels:int = obj["NumLabels"]
      """  Number of labels  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.InspectionReq:bool = obj["InspectionReq"]
      """  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """   Indicates if the receipt is pending inspection.
Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectedDate:str = obj["InspectedDate"]
      """  Date when item was inspected.  """  
      self.InspectedTime:int = obj["InspectedTime"]
      """   Time of day when inspection transaction was recorded.
(seconds since midnight format)  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt date. Mirror image of related RCVHead.ReceiptDate.  Maintained by the RcvHead/RcvDtl write triggers.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  DMRs use Reason type "D".  Only used if failing quantity from inspection.  """  
      self.TotCostVariance:int = obj["TotCostVariance"]
      """  Total Purchase Price Variance amount placed on a receipt in inspection when the variance is received.  Only set if the receipt is currently in inspection (not moved to DMR, job, or stock).  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.NonConformnce:bool = obj["NonConformnce"]
      """  Indicates if the transaction is a non-conformance type transaction.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this part.  """  
      self.OurMtlBurUnitCost:int = obj["OurMtlBurUnitCost"]
      """   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPurPoint:str = obj["GlbPurPoint"]
      """  Global Purchase Point identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackSlip:str = obj["GlbPackSlip"]
      """  Global Packing Slip identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackLine:int = obj["GlbPackLine"]
      """  Global Packing Slip Line identifier.  Used in Consolidated Purchasing.  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.Volume:int = obj["Volume"]
      """  Container volume, frequently specified in cubic sq feet.  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Reporting currency value of this field  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Num related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number of the sales order line related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrigCountryNum:int = obj["OrigCountryNum"]
      """  Country Number of the Origin Country (defaults from Part Country of Origin).  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.LCDutyAmt:int = obj["LCDutyAmt"]
      """  Duty Amount portion of the landed cost for this receipt line.  """  
      self.LCIndCost:int = obj["LCIndCost"]
      """  Indirect Cost portion of the landed cost for this receipt line.  """  
      self.POTransValue:int = obj["POTransValue"]
      """  This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  """  
      self.ExtTransValue:int = obj["ExtTransValue"]
      """  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  """  
      self.Received:bool = obj["Received"]
      """  Flag to indicate that the receipt line has been received.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System (HS) goods classification code.  """  
      self.POType:str = obj["POType"]
      """  Identifier of associated PO ('Std', 'CMI', 'SMI')  """  
      self.AutoReceipt:bool = obj["AutoReceipt"]
      """  Flag representing whether or not this receipt was auto generated by the consumption process (GenSMIReceipt.p).  This is only pertinent for SMI type PO Receipts.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the shipment detail arrived. Defaults as current system date.  """  
      self.LCSpecLineDutyAmt:int = obj["LCSpecLineDutyAmt"]
      """  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  """  
      self.LCUpliftIndCost:int = obj["LCUpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.LCAmt:int = obj["LCAmt"]
      """  The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.LCMtlBurUnitCost:int = obj["LCMtlBurUnitCost"]
      """  Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  """  
      self.DocVendorUnitCost:int = obj["DocVendorUnitCost"]
      """  PO currency value of this field  """  
      self.Rpt1VendorUnitCost:int = obj["Rpt1VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2VendorUnitCost:int = obj["Rpt2VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3VendorUnitCost:int = obj["Rpt3VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its destination, that can be Inventory, Job Material, Job Subcontract, Sales Order.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.MangCustNum:int = obj["MangCustNum"]
      """  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  Originally defaults from PORel.MangCustNum.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegNumCnfg.  """  
      self.ICPackNum:int = obj["ICPackNum"]
      """  Relation between this RcvDtl and the ShipHead.PackNum where this Intercompany Shipment originated.  """  
      self.ShipRcv:str = obj["ShipRcv"]
      """  Shipment Received  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  Can be different from value on header.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  Can be different from value on header.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  Can be different from Header value.  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyOption:str = obj["QtyOption"]
      """  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  """  
      self.ConvOverride:bool = obj["ConvOverride"]
      """  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.SMITransNum:int = obj["SMITransNum"]
      """  Used to identify what has been consumed during an SMI Receipt for a particular transaction.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.Delivered:bool = obj["Delivered"]
      """  Delivered  """  
      self.DeliveredComments:str = obj["DeliveredComments"]
      """  DeliveredComments  """  
      self.InOurCost:int = obj["InOurCost"]
      """  Internal usage for inclusive taxes - Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.DocInUnitCost:int = obj["DocInUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.Rpt1InUnitCost:int = obj["Rpt1InUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitCost:int = obj["Rpt2InUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitCost:int = obj["Rpt3InUnitCost"]
      """  Reporting currency value of this field  """  
      self.InVendorUnitCost:int = obj["InVendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  """  
      self.DocInVendorUnitCost:int = obj["DocInVendorUnitCost"]
      """  PO currency value of this field  """  
      self.Rpt1InVendorUnitCost:int = obj["Rpt1InVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2InVendorUnitCost:int = obj["Rpt2InVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3InVendorUnitCost:int = obj["Rpt3InVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.SupplierUnInvcReceiptQty:int = obj["SupplierUnInvcReceiptQty"]
      """  Value that indicates the remaining quantity of the receipt that is waiting to be invoiced.  """  
      self.OurUnInvcReceiptQty:int = obj["OurUnInvcReceiptQty"]
      """  Value that indicates the un-invoiced quantity of the receipt.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  ** NOT USED TO BE DROPPED 10.2 ** The Tax Liability for this Receipt line  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Receipt line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Indicates if the Receipt line is Taxable  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this item is exempt from tax for this receipt line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the tax info.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a receipt line, if this is set to True the tax engine will not calculate any receipt detail line tax information  """  
      self.InAppliedLCVariance:int = obj["InAppliedLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  """  
      self.InAppliedRcptLCAmt:int = obj["InAppliedRcptLCAmt"]
      """  Internal usage for inclusive taxes - The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  """  
      self.InLCAmt:int = obj["InLCAmt"]
      """  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCDutyAmt:int = obj["InLCDutyAmt"]
      """  Internal usage for inclusive taxes - Duty Amount portion of the landed cost for this receipt line.  """  
      self.InLCIndCost:int = obj["InLCIndCost"]
      """  Internal usage for inclusive taxes - Indirect Cost portion of the landed cost for this receipt line.  """  
      self.InLCMtlBurUnitCost:int = obj["InLCMtlBurUnitCost"]
      """  Internal usage for inclusive taxes - Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  """  
      self.InLCSpecLineDutyAmt:int = obj["InLCSpecLineDutyAmt"]
      """  Internal usage for inclusive taxes - This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCUpliftIndCost:int = obj["InLCUpliftIndCost"]
      """  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InPOTransValue:int = obj["InPOTransValue"]
      """  Internal usage for inclusive taxes - This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  ProjProcessed  """  
      self.ExtNonRecoverableCost:int = obj["ExtNonRecoverableCost"]
      """  This will contain the non deductable tax portion for this Receipt line.  This will be calculated based on the Receipt Header or Receipt Line tax records depending on the Tax Liability type and Company Tax Configuration.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.AttributeBackoutRequired:bool = obj["AttributeBackoutRequired"]
      """  AttributeBackoutRequired  """  
      self.CNDeclarationBillLine:int = obj["CNDeclarationBillLine"]
      """  CNDeclarationBillLine  """  
      self.AllowLCUpdate:bool = obj["AllowLCUpdate"]
      """  Flag to indicate if landed cost info can be updated.  """  
      self.AsmPartDescription:str = obj["AsmPartDescription"]
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      """  Consolidated PO flag.  Used in Consolidated Purchasing.  """  
      self.ContainerExtCost:int = obj["ContainerExtCost"]
      """  This is the extended cost of the container detail item this RcvDtl entry is tied to.  """  
      self.ContainerLCAmt:int = obj["ContainerLCAmt"]
      """  Container Detail Landed Cost Amount  """  
      self.ContractOrder:bool = obj["ContractOrder"]
      self.CostPerFactor:int = obj["CostPerFactor"]
      """  Interger value of CostPerCode  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DisableInspection:bool = obj["DisableInspection"]
      """  Flag to set disable/enable the InspectionReq field.  """  
      self.DisplayUMField:str = obj["DisplayUMField"]
      """  Indicates whether the IUM or DUM field should be displayed/enabled  """  
      self.DocScrUnitCost:int = obj["DocScrUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.DocScrVendorUnitCost:int = obj["DocScrVendorUnitCost"]
      """  PO currency value of this field  """  
      self.DropShipment:bool = obj["DropShipment"]
      """  DropShipment  """  
      self.DueDate:str = obj["DueDate"]
      """  PORel.DueDate  """  
      self.EnableBin:bool = obj["EnableBin"]
      self.EnableDim:bool = obj["EnableDim"]
      """  Indicates whether to enable/disable the dimension fields  """  
      self.EnableInventoryAttributes:bool = obj["EnableInventoryAttributes"]
      """  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  """  
      self.EnableLot:bool = obj["EnableLot"]
      self.EnablePCID:bool = obj["EnablePCID"]
      """  Internal flag used for the row rules to control whether the PCID columns should be enabled or not.  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  Indicates whether to Enable the Serial Number button  """  
      self.EnableSupplierXRef:bool = obj["EnableSupplierXRef"]
      """  Use this field to enable\disable the Supplier Part XRef button  """  
      self.EnableTransValue:bool = obj["EnableTransValue"]
      """  Flag to indicate if PO Trans Value can be updated.  """  
      self.EnableUplift:bool = obj["EnableUplift"]
      """  Flag to indicate if UpliftPercent can be updated.  """  
      self.EnableWhse:bool = obj["EnableWhse"]
      self.ExtCost:int = obj["ExtCost"]
      """  Extended receipt detail cost.  """  
      self.HHReceiveToPCID:bool = obj["HHReceiveToPCID"]
      """  This is true when using the Receive To PCID option in HH PO Receipt.  """  
      self.InputOurQty:int = obj["InputOurQty"]
      """  OurQty not divided by dimension conversion factor for entry.  """  
      self.InspectionFlag:bool = obj["InspectionFlag"]
      """  Flag used to switch other Received To's to Pur-Ins  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Link to the IMRcvDtl table  """  
      self.JobIUM:str = obj["JobIUM"]
      self.JobPartNum:str = obj["JobPartNum"]
      self.JobRequiredQty:int = obj["JobRequiredQty"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.MangCustID:str = obj["MangCustID"]
      self.MangCustName:str = obj["MangCustName"]
      self.ManualLC:bool = obj["ManualLC"]
      """  Flag to indicate if LCIdCost can be manually updated.  """  
      self.MassReceipt:bool = obj["MassReceipt"]
      """  Indicates if created through Mass Receipts  """  
      self.OnTime:str = obj["OnTime"]
      self.OpenRelease:bool = obj["OpenRelease"]
      self.OrderQty:int = obj["OrderQty"]
      self.OurRemQty:int = obj["OurRemQty"]
      """  Our Remaining Quantity  """  
      self.PCIDOutboundContainer:bool = obj["PCIDOutboundContainer"]
      """  Linked to the outbound container flag taken from either the PkgControlStageHeader / PkgControlHeader.  """  
      self.PkgControlStatus:str = obj["PkgControlStatus"]
      """  Package Control Header Status  """  
      self.Plant:str = obj["Plant"]
      """  The Plant to which the warehouse belongs to  """  
      self.POComment:str = obj["POComment"]
      self.PODueDate:str = obj["PODueDate"]
      """  PO Line Due Date  """  
      self.POFactor:int = obj["POFactor"]
      self.POFactorDirection:str = obj["POFactorDirection"]
      self.POHold:bool = obj["POHold"]
      self.POIUM:str = obj["POIUM"]
      self.POPUM:str = obj["POPUM"]
      self.PORelArrivedQty:int = obj["PORelArrivedQty"]
      """  The total quantity that has arrived for this purchase order release.  """  
      self.PORelStatus:str = obj["PORelStatus"]
      """  Indicates the current status of the release. This field is maintained by the System automatically. The possible values are: Open (O), Arrived (A), Inspection (I), Received (R), Closed (C), Voided (V).  """  
      self.RcvdSMIQty:int = obj["RcvdSMIQty"]
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  PORel Received Qty for MassReceipts  """  
      self.RemainingSMIQty:int = obj["RemainingSMIQty"]
      self.Rpt1ScrUnitCost:int = obj["Rpt1ScrUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt1ScrVendorUnitCost:int = obj["Rpt1ScrVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ScrUnitCost:int = obj["Rpt2ScrUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ScrVendorUnitCost:int = obj["Rpt2ScrVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ScrUnitCost:int = obj["Rpt3ScrUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ScrVendorUnitCost:int = obj["Rpt3ScrVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.ScrOurUnitCost:int = obj["ScrOurUnitCost"]
      """  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.ScrVendorUnitCost:int = obj["ScrVendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine  """  
      self.SearchPONum:int = obj["SearchPONum"]
      self.Selected:bool = obj["Selected"]
      self.SetToLocation:bool = obj["SetToLocation"]
      """  This boolean is set by the user in Receipt Entry to initiate the SetToLocation logic for this line.  """  
      self.SkipMaterialQueueCreation:bool = obj["SkipMaterialQueueCreation"]
      """  When this flag is true, skip the Material Queue creation logic for the current RcvDtl line.  """  
      self.SMIComplete:bool = obj["SMIComplete"]
      self.SNStusChanged:bool = obj["SNStusChanged"]
      self.TagMtlSeq:int = obj["TagMtlSeq"]
      """  MtlSeq used in PrintTag option  """  
      self.TagOprSeq:int = obj["TagOprSeq"]
      """  Operation Sequence used in PrintTag  """  
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.ThisTranUOM:str = obj["ThisTranUOM"]
      self.TotalAmt:int = obj["TotalAmt"]
      """  Total amount.  This is the sum of all the other total fields.  """  
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total dedicated Tax amount.  """  
      self.TotDutiesAmt:int = obj["TotDutiesAmt"]
      """  Total duties amount.  This is the sum of RcvDtl.LCSpecLineDutyAmt + RcvDtl.LCDutyAmt  """  
      self.TotLineAmt:int = obj["TotLineAmt"]
      """  Receipt line amount using vendor unit cost.  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total tax amount.  This is the sum of RcvHeadTax.TaxAmt  """  
      self.TotWHTaxAmt:int = obj["TotWHTaxAmt"]
      """  Total WithHolding Tax amount  """  
      self.TranType:str = obj["TranType"]
      """   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  """  
      self.UsePurchaseCode:bool = obj["UsePurchaseCode"]
      self.VendorCurrSymbol:str = obj["VendorCurrSymbol"]
      self.VenRemQty:int = obj["VenRemQty"]
      self.AllowUpdSuppPrice:bool = obj["AllowUpdSuppPrice"]
      """  It is true, if RcvDtl.ReceipteType = 'P' and XbSyst.AllowUpdSuppPrice is true.  """  
      self.AttributeQtyMismatch:bool = obj["AttributeQtyMismatch"]
      """  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  """  
      self.PCIDStatusChanged:bool = obj["PCIDStatusChanged"]
      """  Indicates if the status of the PCID has changed since the receipt took place.  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      self.SerialNoAttributeSetID:int = obj["SerialNoAttributeSetID"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CommodityDescription:str = obj["CommodityDescription"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PackSlipInPrice:bool = obj["PackSlipInPrice"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.PONumConfirmed:bool = obj["PONumConfirmed"]
      self.PONumApprovalStatus:str = obj["PONumApprovalStatus"]
      self.PONumShipToConName:str = obj["PONumShipToConName"]
      self.PONumShipName:str = obj["PONumShipName"]
      self.PONumApprove:bool = obj["PONumApprove"]
      self.PurchCodePurchDesc:str = obj["PurchCodePurchDesc"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointName:str = obj["PurPointName"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvDtlTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  ReportableAmt  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created this record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date and time of the last change to this record  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
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
      self.CollectionType:int = obj["CollectionType"]
      """  CollectionType  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution date.  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date to determine the tax rate.  """  
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
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DocScrDedTaxAmt:int = obj["DocScrDedTaxAmt"]
      self.DocScrReportableAmt:int = obj["DocScrReportableAmt"]
      self.DocScrTaxableAmt:int = obj["DocScrTaxableAmt"]
      self.DocScrTaxAmt:int = obj["DocScrTaxAmt"]
      self.DocScrTaxAmtVar:int = obj["DocScrTaxAmtVar"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.DocScrFixedAmount:int = obj["DocScrFixedAmount"]
      """  Document Fixed Tax Amount  """  
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      """  Reporting currency value of this field  """  
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.RcvDtlPONum:int = obj["RcvDtlPONum"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvDutyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.DutySeq:int = obj["DutySeq"]
      """  Unique Number automatically assigned which is used along with VendorNum, PurPoint, PackSlip and PackLine to uniquely identify the Duty record within the Receipt Line.  """  
      self.TariffCode:str = obj["TariffCode"]
      """  Tariff Code must be for a Preference Scheme that is linked to the Country of Origin.  """  
      self.DutyAmt:int = obj["DutyAmt"]
      """   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount  """  
      self.CommentText:str = obj["CommentText"]
      """  Receipt Line Duty Comments  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InDutyAmt:int = obj["InDutyAmt"]
      """  Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.  """  
      self.AllowLCUpdate:bool = obj["AllowLCUpdate"]
      """  Flag to indicate if landed cost info can be updated.  """  
      self.ScrDutyAmt:int = obj["ScrDutyAmt"]
      """   Duty Amount is calculated based on PO Release Value, Shipment Qty, Tariff Rate, Tariff Percent and Tariff Specific Amount.
Formula: (Total Shipment Qty * Tariff Rate) + (Total Shipment Value * Tariff Percent) + Specific Duty Amount  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TariffDescription:str = obj["TariffDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt Date. Defaults as current system date.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Person that entered the transaction. It is set to the DCD-USERID that was logged on when the record was created . This is not maintainable by the user. This is could be used as a selection parameter for reporting and browsing.  """  
      self.SaveForInvoicing:bool = obj["SaveForInvoicing"]
      """  An internal flag that indicates this receipt document is to be saved for retrieval by A\P invoice entry. This is set based on the value stored in APSyst.SaveForInvoicing.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  An internal flag that indicates "ALL" the details items on this receipt document have been invoiced. This is set to "Yes" when there are no related RcvDtl records where RcvDtl.Invoiced = No. This flag along with the SaveForInvoicing flag are used to present a list of uninvoiced packing slips.  """  
      self.ReceiptComment:str = obj["ReceiptComment"]
      """  Contains comments about the overall Receipt.  """  
      self.ReceivePerson:str = obj["ReceivePerson"]
      """  Short name or initials of person who actually did the receiving. A totally optional field which can be used for internal reference.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  The system date when this record was created.  """  
      self.Plant:str = obj["Plant"]
      """  Site that received the goods.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order.  """  
      self.LCReference:str = obj["LCReference"]
      """  Reference field for Landed Costs  """  
      self.LCComment:str = obj["LCComment"]
      """  Comment field for Landed Costs  """  
      self.LandedCost:int = obj["LandedCost"]
      """  Total amount of landed cost spread amongst the lines.  This amount includes all duties and indirect costs of all lines.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.LCVariance:int = obj["LCVariance"]
      """  This field holds the variance amount for the landed costs.  """  
      self.ICLinked:bool = obj["ICLinked"]
      """  Indicates if linked to a inter-company shipment  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPurPoint:str = obj["GlbPurPoint"]
      """  Global Purchase Point identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackSlip:str = obj["GlbPackSlip"]
      """  Global Packing Slip identifier.  Used in Consolidated Purchasing.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost was disbursed among the container details.  Valid options are Volume (only for po releases tied to a container), Weight, Value and Manual.  """  
      self.AutoReceipt:bool = obj["AutoReceipt"]
      """  This is a flag representing whether or not this is a receipt that was auto generated.  It could only be true if it is associated with an SMI type PO.  """  
      self.AutoTranType:str = obj["AutoTranType"]
      """  Indicates the type of transaction that created this auto receipt.  This field will only be populated if AutoReceipt = true.  """  
      self.POType:str = obj["POType"]
      """  POType Identifier of the associated PO ('Std', 'CMI', or 'SMI')  """  
      self.AutoTranID:int = obj["AutoTranID"]
      """  The unique number of the PartTran record that was the source of this transaction.  This field will only be populated if AutoReceipt = true.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.SpecDutyAmt:int = obj["SpecDutyAmt"]
      """  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the receipt lines using the line tariffs as a factor.  """  
      self.AppliedLCAmt:int = obj["AppliedLCAmt"]
      """  The total Landed Cost Amount disbursed for this receipt.  """  
      self.LCDutyAmt:int = obj["LCDutyAmt"]
      """  The total Duty Amount of the entire receipt.  """  
      self.LCIndCost:int = obj["LCIndCost"]
      """  The total Indirect Cost Amount of the entire receipt.  """  
      self.ApplyToLC:bool = obj["ApplyToLC"]
      """  Flag to indicate if all of the receipt duties and indirect costs needs to be applied or disbursed.  """  
      self.Received:bool = obj["Received"]
      """  Flag to indicate if the entire receipt has been completely received.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the shipment arrived. Defaults as current system date.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount applied for this receipt.  """  
      self.LCUpliftIndCost:int = obj["LCUpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the receipt. The total LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and SpecDutyAmt.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  Default value for lines.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  Default value for lines.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  Default value for lines.  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  if Part.GrossWeightUOM is not known.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AddrList:str = obj["AddrList"]
      """  Address Information from Vendor or VendorPP  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.DispLandedCost:int = obj["DispLandedCost"]
      """  Display field used for container landed costs.  """  
      self.OrigLandedCost:int = obj["OrigLandedCost"]
      """  This field is used to hold the original total landed cost for containers for all plants.  """  
      self.POTypeDesc:str = obj["POTypeDesc"]
      self.AllowLCUpdate:bool = obj["AllowLCUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.AllowUplift:bool = obj["AllowUplift"]
      """  Flag to indicate if UpliftPercent should be enabled.  """  
      self.UpdateDtlRecs:bool = obj["UpdateDtlRecs"]
      """  Flag to indicate if details need to be refreshed after changing the UpliftPercent from header.  """  
      self.eshReceived:bool = obj["eshReceived"]
      """  Logical used to indicate if all details have been received.  """  
      self.PartialReceipt:bool = obj["PartialReceipt"]
      """  Logical indicating whether or not the receipt has been fully received.  If yes then the receipt has only been partially received.  """  
      self.LCMessage:str = obj["LCMessage"]
      """  Landed cost message used to inform the user on retrieval of data that the applied and landed costs do not equal.  """  
      self.UpdateDtlRcptDate:bool = obj["UpdateDtlRcptDate"]
      """  Flag to indicate if receipt details need to be refreshed after changing the Receipt Date from header.  """  
      self.UpdateDtlArvdDate:bool = obj["UpdateDtlArvdDate"]
      """  Flag to indicate if receipt details need to be refreshed after changing the Arrival Date from header.  """  
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointName:str = obj["PurPointName"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.vrPONumShipToConName:str = obj["vrPONumShipToConName"]
      self.vrPONumShipName:str = obj["vrPONumShipName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvHeadListTableset:
   def __init__(self, obj):
      self.RcvHeadList:list[Erp_Tablesets_RcvHeadListRow] = obj["RcvHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RcvHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt Date. Defaults as current system date.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Person that entered the transaction. It is set to the DCD-USERID that was logged on when the record was created . This is not maintainable by the user. This is could be used as a selection parameter for reporting and browsing.  """  
      self.SaveForInvoicing:bool = obj["SaveForInvoicing"]
      """  An internal flag that indicates this receipt document is to be saved for retrieval by A\P invoice entry. This is set based on the value stored in APSyst.SaveForInvoicing.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  An internal flag that indicates "ALL" the details items on this receipt document have been invoiced. This is set to "Yes" when there are no related RcvDtl records where RcvDtl.Invoiced = No. This flag along with the SaveForInvoicing flag are used to present a list of uninvoiced packing slips.  """  
      self.ReceiptComment:str = obj["ReceiptComment"]
      """  Contains comments about the overall Receipt.  """  
      self.ReceivePerson:str = obj["ReceivePerson"]
      """  Short name or initials of person who actually did the receiving. A totally optional field which can be used for internal reference.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  The system date when this record was created.  """  
      self.Plant:str = obj["Plant"]
      """  Site that received the goods.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order.  """  
      self.LCReference:str = obj["LCReference"]
      """  Reference field for Landed Costs  """  
      self.LCComment:str = obj["LCComment"]
      """  Comment field for Landed Costs  """  
      self.LandedCost:int = obj["LandedCost"]
      """  Total amount of landed cost spread amongst the lines.  This amount includes all duties and indirect costs of all lines.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.LCVariance:int = obj["LCVariance"]
      """  This field holds the variance amount for the landed costs.  """  
      self.ICLinked:bool = obj["ICLinked"]
      """  Indicates if linked to a inter-company shipment  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPurPoint:str = obj["GlbPurPoint"]
      """  Global Purchase Point identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackSlip:str = obj["GlbPackSlip"]
      """  Global Packing Slip identifier.  Used in Consolidated Purchasing.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost was disbursed among the container details.  Valid options are Volume (only for po releases tied to a container), Weight, Value and Manual.  """  
      self.AutoReceipt:bool = obj["AutoReceipt"]
      """  This is a flag representing whether or not this is a receipt that was auto generated.  It could only be true if it is associated with an SMI type PO.  """  
      self.AutoTranType:str = obj["AutoTranType"]
      """  Indicates the type of transaction that created this auto receipt.  This field will only be populated if AutoReceipt = true.  """  
      self.POType:str = obj["POType"]
      """  POType Identifier of the associated PO ('Std', 'CMI', or 'SMI')  """  
      self.AutoTranID:int = obj["AutoTranID"]
      """  The unique number of the PartTran record that was the source of this transaction.  This field will only be populated if AutoReceipt = true.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.SpecDutyAmt:int = obj["SpecDutyAmt"]
      """  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the receipt lines using the line tariffs as a factor.  """  
      self.AppliedLCAmt:int = obj["AppliedLCAmt"]
      """  The total Landed Cost Amount disbursed for this receipt.  """  
      self.LCDutyAmt:int = obj["LCDutyAmt"]
      """  The total Duty Amount of the entire receipt.  """  
      self.LCIndCost:int = obj["LCIndCost"]
      """  The total Indirect Cost Amount of the entire receipt.  """  
      self.ApplyToLC:bool = obj["ApplyToLC"]
      """  Flag to indicate if all of the receipt duties and indirect costs needs to be applied or disbursed.  """  
      self.Received:bool = obj["Received"]
      """  Flag to indicate if the entire receipt has been completely received.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the shipment arrived. Defaults as current system date.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount applied for this receipt.  """  
      self.LCUpliftIndCost:int = obj["LCUpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the receipt. The total LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and SpecDutyAmt.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  Default value for lines.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  Default value for lines.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  Default value for lines.  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  if Part.GrossWeightUOM is not known.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Liability for this Receipt  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.HdrTaxNoUpdt:bool = obj["HdrTaxNoUpdt"]
      """  ** NOT USED TO BE DROPPED 10.2 ** This flag determines whether any manual taxes were created for a header miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code - FUTUREUSE  """  
      self.TaxesCalculated:bool = obj["TaxesCalculated"]
      """  The flag indicates that taxes have been calculated.  Once the flag is true is should never be changed back to false.  This will be set to true when any receipt line is marked as received, or when taxes have been calculated via the Calculate All Taxes menu option.  """  
      self.InAppliedLCAmt:int = obj["InAppliedLCAmt"]
      """  Internal usage for inclusive taxes - The total Landed Cost Amount disbursed for this receipt.  """  
      self.InAppliedLCVariance:int = obj["InAppliedLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  """  
      self.InAppliedRcptLCAmt:int = obj["InAppliedRcptLCAmt"]
      """  Internal usage for inclusive taxes - The total Landed Cost Amount applied for this receipt.  """  
      self.InLandedCost:int = obj["InLandedCost"]
      """  Internal usage for inclusive taxes - Total amount of landed cost spread amongst the lines.  This amount includes all duties and indirect costs of all lines.  """  
      self.InLCDutyAmt:int = obj["InLCDutyAmt"]
      """  Internal usage for inclusive taxes - The total Duty Amount of the entire receipt.  """  
      self.InLCIndCost:int = obj["InLCIndCost"]
      """  Internal usage for inclusive taxes - The total Indirect Cost Amount of the entire receipt.  """  
      self.InLCUpliftIndCost:int = obj["InLCUpliftIndCost"]
      """  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the receipt. The total LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and SpecDutyAmt.  """  
      self.InLCVariance:int = obj["InLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the variance amount for the landed costs.  """  
      self.InSpecDutyAmt:int = obj["InSpecDutyAmt"]
      """  Internal usage for inclusive taxes - This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the receipt lines using the line tariffs as a factor.  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      """  Declaration Bill  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  Bonded  """  
      self.APTaxRoundOption:int = obj["APTaxRoundOption"]
      """  APTaxRoundOption  """  
      self.AddrList:str = obj["AddrList"]
      """  Address Information from Vendor or VendorPP  """  
      self.PartialReceipt:bool = obj["PartialReceipt"]
      """  Logical indicating whether or not the receipt has been fully received.  If yes then the receipt has only been partially received.  """  
      self.POLine:int = obj["POLine"]
      self.PORel:int = obj["PORel"]
      self.POTypeDesc:str = obj["POTypeDesc"]
      self.ShipViaDesc:str = obj["ShipViaDesc"]
      self.TotalAmt:int = obj["TotalAmt"]
      """  Total amount.  This is the sum of all the other total fields.  """  
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total dedicated Tax amount.  """  
      self.TotDutiesAmt:int = obj["TotDutiesAmt"]
      """  Total duties amount.  This is the sum of RcvHead.SpecDutyAmt + RcvHead.LCDutyAmt  """  
      self.TotGrossWeight:int = obj["TotGrossWeight"]
      """  Total Gross Weight of all receipt lines  """  
      self.TotGrossWeightUOM:str = obj["TotGrossWeightUOM"]
      """  Qualifies the unit of measure of the Gross Weight field.  """  
      self.TotIndirectCostsAmt:int = obj["TotIndirectCostsAmt"]
      """  Total Indirect Costs amount.  This is a sum of all RcvMisc.ActualAmt.  """  
      self.TotLinesAmt:int = obj["TotLinesAmt"]
      """  Total amount for all receipt lines.  This is the sum of RcvDtl.POTransValue.  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total tax amount.  This is the sum of RcvHeadTax.TaxAmt  """  
      self.TotWeight:int = obj["TotWeight"]
      """  Total Weight of all receipt lines  """  
      self.TotWeightUOM:str = obj["TotWeightUOM"]
      """  Qualifies the unit of measure of the Weight field.  """  
      self.TotWHTaxAmt:int = obj["TotWHTaxAmt"]
      """  Total WithHolding Tax amount  """  
      self.UpdateDtlArvdDate:bool = obj["UpdateDtlArvdDate"]
      """  Flag to indicate if receipt details need to be refreshed after changing the Arrival Date from header.  """  
      self.UpdateDtlRcptDate:bool = obj["UpdateDtlRcptDate"]
      """  Flag to indicate if receipt details need to be refreshed after changing the Receipt Date from header.  """  
      self.UpdateDtlRecs:bool = obj["UpdateDtlRecs"]
      """  Flag to indicate if details need to be refreshed after changing the UpliftPercent from header.  """  
      self.AllowLCUpdate:bool = obj["AllowLCUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.AllowUplift:bool = obj["AllowUplift"]
      """  Flag to indicate if UpliftPercent should be enabled.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.DispLandedCost:int = obj["DispLandedCost"]
      """  Display field used for container landed costs.  """  
      self.eshReceived:bool = obj["eshReceived"]
      """  Logical used to indicate if all details have been received.  """  
      self.IntQueID:int = obj["IntQueID"]
      self.LCMessage:str = obj["LCMessage"]
      """  Landed cost message used to inform the user on retrieval of data that the applied and landed costs do not equal.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.OrigLandedCost:int = obj["OrigLandedCost"]
      """  This field is used to hold the original total landed cost for containers for all plants.  """  
      self.AddrListFormatted:str = obj["AddrListFormatted"]
      """  The formatted address Information from Vendor or VendorPP  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.vrPONumCNBonded:bool = obj["vrPONumCNBonded"]
      self.vrPONumShipToConName:str = obj["vrPONumShipToConName"]
      self.vrPONumShipName:str = obj["vrPONumShipName"]
      self.XbSystReceiptTaxCalculate:bool = obj["XbSystReceiptTaxCalculate"]
      self.XbSystAPTaxLnLevel:bool = obj["XbSystAPTaxLnLevel"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvHeadTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcReportableAmt.  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created this record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date and time of the last change to this record  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
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
      """  Date to determine the tax rate.  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
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
      self.TextCode:str = obj["TextCode"]
      """  TextCode  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.SummaryOnly:bool = obj["SummaryOnly"]
      """  flag to indicate if this record is used only to total detail records,  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.EnableSuperGRate:bool = obj["EnableSuperGRate"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      """  Display field for Rpt1ScrFixedAmount  """  
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      """  Display field for Rpt2FixedAmount  """  
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      """  Display field for Rpt3rFixedAmount  """  
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.ScrDocDedTaxAmt:int = obj["ScrDocDedTaxAmt"]
      self.ScrDocFixedAmount:int = obj["ScrDocFixedAmount"]
      """  Doc Fixed Amount  """  
      self.ScrDocReportableAmt:int = obj["ScrDocReportableAmt"]
      self.ScrDocTaxableAmt:int = obj["ScrDocTaxableAmt"]
      self.ScrDocTaxAmt:int = obj["ScrDocTaxAmt"]
      self.ScrDocTaxAmtVar:int = obj["ScrDocTaxAmtVar"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  FixedAmount  """  
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvMiscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.MiscSeq:int = obj["MiscSeq"]
      """  Unique Number automatically assigned within the Company/VendorNum/PurPoint/PackSlip to uniquely identify each Indirect Costs for this receipt.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Miscellaneous Charge ID that is flagged for Landed Cost  """  
      self.ExcludeFromLC:bool = obj["ExcludeFromLC"]
      """  Flag to indicate if the Indirect Cost is to be excluded from the Landed Cost calculation.  Disabled when IncTransValue is checked.  """  
      self.IncTransValue:bool = obj["IncTransValue"]
      """  Flag to indicate if the Indirect Cost is to be included in the Transaction Value (statistical value) which is used to calculate duties.  Disabled when the ExcludeFromLC is checked.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.ActualAmt:int = obj["ActualAmt"]
      """  Actual Miscellaneous Charge Amount.  """  
      self.DocActualAmt:int = obj["DocActualAmt"]
      """  Actual Miscellaneous Charge Amount in the currency specified.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.CommentText:str = obj["CommentText"]
      """  Receipt Indirect Cost Comments  """  
      self.Rpt1ActualAmt:int = obj["Rpt1ActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.Rpt2ActualAmt:int = obj["Rpt2ActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.Rpt3ActualAmt:int = obj["Rpt3ActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date that will be used to get the exchange rate if the indirect cost is not associated with an invoice miscellaneous charge.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvMsc record.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line from corresponding APInvMsc record.  """  
      self.MscNum:int = obj["MscNum"]
      """  The unique sequence number identifying the AP invoice miscellaneous charge.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.APInvVendorNum:int = obj["APInvVendorNum"]
      """  VendorNum duplicated from the corresponding APInvHed record.  Not directly maintainable by the operator.  """  
      self.PackLine:int = obj["PackLine"]
      """  Reference to RcvDtl.PackLine. An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Receipt Misc. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Indicates if the Indirect Cost is taxable  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  """  
      self.InActualAmt:int = obj["InActualAmt"]
      """  Actual Miscellaneous Charge Amount.  """  
      self.DocInActualAmt:int = obj["DocInActualAmt"]
      """  Actual Miscellaneous Charge Amount in the currency specified.  """  
      self.Rpt1InActualAmt:int = obj["Rpt1InActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.Rpt2InActualAmt:int = obj["Rpt2InActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.Rpt3InActualAmt:int = obj["Rpt3InActualAmt"]
      """  Reporting currency value of the Actual Amount.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this indirect cost.  """  
      self.RateLabel:str = obj["RateLabel"]
      """  Label for the exchange rate  """  
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total dedicated Tax amount.  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total tax amount  """  
      self.AllowLCUpdate:bool = obj["AllowLCUpdate"]
      """  Flag to indicate if landed cost info can be updated.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for currency "BASE"  """  
      self.ScrActualAmt:int = obj["ScrActualAmt"]
      """  Actual Miscellaneous Charge Amount - Screen value.  """  
      self.Rpt1ScrActualAmt:int = obj["Rpt1ScrActualAmt"]
      """  Reporting currency value of the Actual Amount - Screen value.  """  
      self.Rpt2ScrActualAmt:int = obj["Rpt2ScrActualAmt"]
      """  Reporting currency value of the Actual Amount - Screen value.  """  
      self.Rpt3ScrActualAmt:int = obj["Rpt3ScrActualAmt"]
      """  Reporting currency value of the Actual Amount - Screen value  """  
      self.DocScrActualAmt:int = obj["DocScrActualAmt"]
      """  Actual Miscellaneous Charge Amount in the currency specified - Screen value  """  
      self.BitFlag:int = obj["BitFlag"]
      self.APInvVendorName:str = obj["APInvVendorName"]
      self.APInvVendorVendorID:str = obj["APInvVendorVendorID"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.PurMiscLCDisburseMethod:str = obj["PurMiscLCDisburseMethod"]
      self.PurMiscLCCurrencyCode:str = obj["PurMiscLCCurrencyCode"]
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      self.PurMiscLCAmount:int = obj["PurMiscLCAmount"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.RcvHeadReceiptDate:str = obj["RcvHeadReceiptDate"]
      self.RcvHeadInPrice:bool = obj["RcvHeadInPrice"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.VendorName:str = obj["VendorName"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvMiscTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.MiscSeq:int = obj["MiscSeq"]
      """  Unique Number automatically assigned within the Company/VendorNum/PurPoint/PackSlip to uniquely identify each Indirect Costs for this receipt.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  ** NOT USED TO BE DROPPED 10.2 ** Miscellaneous Charge ID that is flagged for Landed Cost  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  ReportableAmt  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created this record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date and time of the last change to this record  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
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
      self.CollectionType:int = obj["CollectionType"]
      """  CollectionType  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution date.  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date to determine the tax rate.  """  
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
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Reporting currency value of this field  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DocScrDedTaxAmt:int = obj["DocScrDedTaxAmt"]
      self.DocScrReportableAmt:int = obj["DocScrReportableAmt"]
      self.DocScrTaxableAmt:int = obj["DocScrTaxableAmt"]
      self.DocScrTaxAmt:int = obj["DocScrTaxAmt"]
      self.DocScrTaxAmtVar:int = obj["DocScrTaxAmtVar"]
      self.Rpt1ScrDedTaxAmt:int = obj["Rpt1ScrDedTaxAmt"]
      self.Rpt1ScrReportableAmt:int = obj["Rpt1ScrReportableAmt"]
      self.Rpt1ScrTaxableAmt:int = obj["Rpt1ScrTaxableAmt"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTaxAmtVar:int = obj["Rpt1ScrTaxAmtVar"]
      self.Rpt2ScrDedTaxAmt:int = obj["Rpt2ScrDedTaxAmt"]
      self.Rpt2ScrReportableAmt:int = obj["Rpt2ScrReportableAmt"]
      self.Rpt2ScrTaxableAmt:int = obj["Rpt2ScrTaxableAmt"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTaxAmtVar:int = obj["Rpt2ScrTaxAmtVar"]
      self.Rpt3ScrDedTaxAmt:int = obj["Rpt3ScrDedTaxAmt"]
      self.Rpt3ScrReportableAmt:int = obj["Rpt3ScrReportableAmt"]
      self.Rpt3ScrTaxableAmt:int = obj["Rpt3ScrTaxableAmt"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTaxAmtVar:int = obj["Rpt3ScrTaxAmtVar"]
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.ScrReportableAmt:int = obj["ScrReportableAmt"]
      self.ScrTaxableAmt:int = obj["ScrTaxableAmt"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      self.ScrTaxAmtVar:int = obj["ScrTaxAmtVar"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.DocScrFixedAmount:int = obj["DocScrFixedAmount"]
      """  Document Fixed Tax Amount  """  
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      """  Reporting currency value of this field  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.RcvMiscCurrencyCode:str = obj["RcvMiscCurrencyCode"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReceiptTableset:
   def __init__(self, obj):
      self.RcvHead:list[Erp_Tablesets_RcvHeadRow] = obj["RcvHead"]
      self.RcvHeadAttch:list[Erp_Tablesets_RcvHeadAttchRow] = obj["RcvHeadAttch"]
      self.RcvHeadTax:list[Erp_Tablesets_RcvHeadTaxRow] = obj["RcvHeadTax"]
      self.RcvDtl:list[Erp_Tablesets_RcvDtlRow] = obj["RcvDtl"]
      self.RcvDtlAttch:list[Erp_Tablesets_RcvDtlAttchRow] = obj["RcvDtlAttch"]
      self.RcvDtlAttrValueSet:list[Erp_Tablesets_RcvDtlAttrValueSetRow] = obj["RcvDtlAttrValueSet"]
      self.RcvDtlTax:list[Erp_Tablesets_RcvDtlTaxRow] = obj["RcvDtlTax"]
      self.RcvDuty:list[Erp_Tablesets_RcvDutyRow] = obj["RcvDuty"]
      self.RcvMisc:list[Erp_Tablesets_RcvMiscRow] = obj["RcvMisc"]
      self.RcvMiscTax:list[Erp_Tablesets_RcvMiscTaxRow] = obj["RcvMiscTax"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.PendingRcvDtl:list[Erp_Tablesets_PendingRcvDtlRow] = obj["PendingRcvDtl"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.SupplierXRef:list[Erp_Tablesets_SupplierXRefRow] = obj["SupplierXRef"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsRow:
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The part number to which the serial numbers have been assigned.  """  
      self.quantity:int = obj["quantity"]
      """  The quantity of serial numbers that need to be selected.  """  
      self.whereClause:str = obj["whereClause"]
      """  whereClause for filtering available serial numbers  """  
      self.transType:str = obj["transType"]
      """  transType of this transaction  """  
      self.sourceRowID:str = obj["sourceRowID"]
      """  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  """  
      self.enableCreate:bool = obj["enableCreate"]
      """  Determines if serial numbers can be created.  """  
      self.enableSelect:bool = obj["enableSelect"]
      """  Determines if serial numbers can be selected.  """  
      self.enableRetrieve:bool = obj["enableRetrieve"]
      """  Determines if serial numbers can be retrieved.  """  
      self.allowVoided:bool = obj["allowVoided"]
      """  Specifies whether Voided serial numbers can be manually selected.  """  
      self.plant:str = obj["plant"]
      """  The Plant associated with this transaction  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      self.xrefPartType:str = obj["xrefPartType"]
      self.xrefCustNum:int = obj["xrefCustNum"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.attributeSetShortDescription:str = obj["attributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsTableset:
   def __init__(self, obj):
      self.SelectSerialNumbersParams:list[Erp_Tablesets_SelectSerialNumbersParamsRow] = obj["SelectSerialNumbersParams"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SupplierXRefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.MfgID:str = obj["MfgID"]
      self.MfgName:str = obj["MfgName"]
      self.MfgNum:int = obj["MfgNum"]
      self.MfgPartNum:str = obj["MfgPartNum"]
      self.PartNum:str = obj["PartNum"]
      self.POReference:bool = obj["POReference"]
      self.Receipt:bool = obj["Receipt"]
      self.VendNum:int = obj["VendNum"]
      self.VendPartNum:str = obj["VendPartNum"]
      self.Invoice:bool = obj["Invoice"]
      self.RcvXRefNum:int = obj["RcvXRefNum"]
      """  RcvXRefNum  """  
      self.Inspected:bool = obj["Inspected"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtReceiptTableset:
   def __init__(self, obj):
      self.RcvHead:list[Erp_Tablesets_RcvHeadRow] = obj["RcvHead"]
      self.RcvHeadAttch:list[Erp_Tablesets_RcvHeadAttchRow] = obj["RcvHeadAttch"]
      self.RcvHeadTax:list[Erp_Tablesets_RcvHeadTaxRow] = obj["RcvHeadTax"]
      self.RcvDtl:list[Erp_Tablesets_RcvDtlRow] = obj["RcvDtl"]
      self.RcvDtlAttch:list[Erp_Tablesets_RcvDtlAttchRow] = obj["RcvDtlAttch"]
      self.RcvDtlAttrValueSet:list[Erp_Tablesets_RcvDtlAttrValueSetRow] = obj["RcvDtlAttrValueSet"]
      self.RcvDtlTax:list[Erp_Tablesets_RcvDtlTaxRow] = obj["RcvDtlTax"]
      self.RcvDuty:list[Erp_Tablesets_RcvDutyRow] = obj["RcvDuty"]
      self.RcvMisc:list[Erp_Tablesets_RcvMiscRow] = obj["RcvMisc"]
      self.RcvMiscTax:list[Erp_Tablesets_RcvMiscTaxRow] = obj["RcvMiscTax"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.PendingRcvDtl:list[Erp_Tablesets_PendingRcvDtlRow] = obj["PendingRcvDtl"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.SupplierXRef:list[Erp_Tablesets_SupplierXRefRow] = obj["SupplierXRef"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExistsRcvHeadWithDifferentPO_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   poNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.poNum:int = obj["poNum"]
      pass

class ExistsRcvHeadWithDifferentPO_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ExistsRcvHead_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   poNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.poNum:int = obj["poNum"]
      """  PO Number  """  
      pass

class ExistsRcvHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warning:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listAvailTranDocTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReceiptTableset] = obj["returnObj"]
      pass

class GetByIdChkContainerID_input:
   """ Required : 
   piVendorNum
   pcPurPoint
   pcPackSlip
   piPONum
   """  
   def __init__(self, obj):
      self.piVendorNum:int = obj["piVendorNum"]
      """  The vendor for the selected PO.  """  
      self.pcPurPoint:str = obj["pcPurPoint"]
      """  The purchase point for the selected PO  """  
      self.pcPackSlip:str = obj["pcPackSlip"]
      """  The pack slip selected by the user  """  
      self.piPONum:int = obj["piPONum"]
      """  The PO number selected by the user  """  
      pass

class GetByIdChkContainerID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReceiptTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ReceiptTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ReceiptTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetContainerReceiptPartTranPKs_input:
   """ Required : 
   containerID
   """  
   def __init__(self, obj):
      self.containerID:int = obj["containerID"]
      """  The Container Landed Cost ID  """  
      pass

class GetContainerReceiptPartTranPKs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDtlAssemblyInfo_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      pass

class GetDtlAssemblyInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDtlJobInfo_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   jobNum
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.jobNum:str = obj["jobNum"]
      """  The new Job Number  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class GetDtlJobInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDtlLotInfo_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   lotNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.lotNum:str = obj["lotNum"]
      """  New Lot Number to validate  """  
      pass

class GetDtlLotInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.questionMsg:str = obj["parameters"]
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDtlPOInfo_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   poNum
   requiresUserInput
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.poNum:int = obj["poNum"]
      """  New PO Number  """  
      self.requiresUserInput:bool = obj["requiresUserInput"]
      """  Verifies if User Input is required  """  
      pass

class GetDtlPOInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.poStatusQstnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDtlPOLineInfo_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   poLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.poLine:int = obj["poLine"]
      """  New POLine Number  """  
      pass

class GetDtlPOLineInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.serialWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDtlPORelInfo_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   poRelNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.poRelNum:int = obj["poRelNum"]
      """  New PO Release Number  """  
      pass

class GetDtlPORelInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDtlPartInfo_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   partNum
   SysRowID
   rowType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.partNum:str = obj["partNum"]
      """  Proposed partNum value  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID of found row typically from multiple matches  """  
      self.rowType:str = obj["rowType"]
      """  FindPart match record  """  
      pass

class GetDtlPartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.partNum:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class GetDtlQtyInfo_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   inputOurQty
   inputIUM
   whichField
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.inputOurQty:int = obj["inputOurQty"]
      """  Proposed change to the Input qty field  """  
      self.inputIUM:str = obj["inputIUM"]
      """  Proposed change to the IUM field  """  
      self.whichField:str = obj["whichField"]
      """  Indicates either 'QTY' or 'UOM' field changed  """  
      pass

class GetDtlQtyInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.warnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDtlRcvdToInfo_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   rcvdTo
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.rcvdTo:str = obj["rcvdTo"]
      """  Proposed ReceivedTo value  """  
      pass

class GetDtlRcvdToInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.rcvdTo:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDtlSeqInfo_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   jobSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Packing slip number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.jobSeq:int = obj["jobSeq"]
      """  Proposed JobSeq change  """  
      pass

class GetDtlSeqInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.serialWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDtlVenQtyInfo_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   vendorQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Packing slip number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.vendorQty:int = obj["vendorQty"]
      """  Proposed VendorQty value  """  
      pass

class GetDtlVenQtyInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.warnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetExistingRcvHead_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      pass

class GetExistingRcvHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetListReceipts_input:
   """ Required : 
   whereClauseRcvDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRcvDtl:str = obj["whereClauseRcvDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListReceipts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReceiptTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_RcvHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetLotImportInfo_input:
   """ Required : 
   inPartNum
   inLotNum
   """  
   def __init__(self, obj):
      self.inPartNum:str = obj["inPartNum"]
      """  PartNum  """  
      self.inLotNum:str = obj["inLotNum"]
      """  LotNum  """  
      pass

class GetLotImportInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outImportNum:str = obj["parameters"]
      self.outImportedFromDesc:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetMtlQueueSeqValue_input:
   """ Required : 
   company
   pcid
   vendorNum
   purPoint
   packSlip
   packLine
   tranType
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.pcid:str = obj["pcid"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.packLine:int = obj["packLine"]
      self.tranType:str = obj["tranType"]
      pass

class GetMtlQueueSeqValue_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class GetNewRcvDtlAttch_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.packLine:int = obj["packLine"]
      pass

class GetNewRcvDtlAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRcvDtlAttrValueSet_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.packLine:int = obj["packLine"]
      pass

class GetNewRcvDtlAttrValueSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRcvDtlMisc_input:
   """ Required : 
   ds
   VendorNum
   PurPoint
   PackSlip
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PackSlip:str = obj["PackSlip"]
      pass

class GetNewRcvDtlMisc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRcvDtlTax_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.packLine:int = obj["packLine"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewRcvDtlTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRcvDtl_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      pass

class GetNewRcvDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRcvDuty_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.packLine:int = obj["packLine"]
      pass

class GetNewRcvDuty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRcvHeadAttch_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      pass

class GetNewRcvHeadAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRcvHeadTax_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewRcvHeadTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRcvHeadWithPONum_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   poNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.poNum:int = obj["poNum"]
      pass

class GetNewRcvHeadWithPONum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRcvHead_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      pass

class GetNewRcvHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRcvMiscTax_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   miscSeq
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.miscSeq:int = obj["miscSeq"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewRcvMiscTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRcvMisc_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      pass

class GetNewRcvMisc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPOInfo_input:
   """ Required : 
   ds
   poNum
   fromReceiptEntryNewRcpt
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.poNum:int = obj["poNum"]
      """  Proposed Purchase Order Number  """  
      self.fromReceiptEntryNewRcpt:bool = obj["fromReceiptEntryNewRcpt"]
      """  Flag to indicate this was called from the ReceiptEntry, non-tracker mode  """  
      pass

class GetPOInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["parameters"]
      self.purPoint:str = obj["parameters"]
      self.warnMsg:str = obj["parameters"]
      self.poStatusWarnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPartTranPKs_input:
   """ Required : 
   packSlip
   poNum
   vendorNum
   """  
   def __init__(self, obj):
      self.packSlip:str = obj["packSlip"]
      """  The PackSlip number  """  
      self.poNum:int = obj["poNum"]
      """  The PO number  """  
      self.vendorNum:int = obj["vendorNum"]
      """  The Vendor number  """  
      pass

class GetPartTranPKs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPartXRefInfo_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Proposed partNum value  """  
      pass

class GetPartXRefInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class GetPendingDtl_input:
   """ Required : 
   ds
   inPONum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.inPONum:int = obj["inPONum"]
      """  The PO number  """  
      pass

class GetPendingDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPurPointInfo_input:
   """ Required : 
   ds
   purPoint
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.purPoint:str = obj["purPoint"]
      """  Proposed Purchase Point value  """  
      pass

class GetPurPointInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.purPoint:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRcvDtlLCIndCost_input:
   """ Required : 
   company
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      pass

class GetRcvDtlLCIndCost_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class GetReceiptDetailsFromContainer_input:
   """ Required : 
   ds
   inContainerID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.inContainerID:int = obj["inContainerID"]
      """  Container ID to retrieve records for  """  
      pass

class GetReceiptDetailsFromContainer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetReceiptRelationshipMap_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   maxNumOfCards
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.maxNumOfCards:int = obj["maxNumOfCards"]
      pass

class GetReceiptRelationshipMap_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRowsForAPInvoice_input:
   """ Required : 
   whereClauseRcvHead
   whereClauseRcvHeadAttch
   whereClauseRcvHeadTax
   whereClauseRcvDtl
   whereClauseRcvDtlAttch
   whereClauseRcvDtlAttrValueSet
   whereClauseRcvDtlTax
   whereClauseRcvDuty
   whereClauseRcvMisc
   whereClauseRcvMiscTax
   whereClauseLegalNumGenOpts
   whereClausePendingRcvDtl
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   whereClauseSupplierXRef
   vendorNum
   invoiceNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRcvHead:str = obj["whereClauseRcvHead"]
      self.whereClauseRcvHeadAttch:str = obj["whereClauseRcvHeadAttch"]
      self.whereClauseRcvHeadTax:str = obj["whereClauseRcvHeadTax"]
      self.whereClauseRcvDtl:str = obj["whereClauseRcvDtl"]
      self.whereClauseRcvDtlAttch:str = obj["whereClauseRcvDtlAttch"]
      self.whereClauseRcvDtlAttrValueSet:str = obj["whereClauseRcvDtlAttrValueSet"]
      self.whereClauseRcvDtlTax:str = obj["whereClauseRcvDtlTax"]
      self.whereClauseRcvDuty:str = obj["whereClauseRcvDuty"]
      self.whereClauseRcvMisc:str = obj["whereClauseRcvMisc"]
      self.whereClauseRcvMiscTax:str = obj["whereClauseRcvMiscTax"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClausePendingRcvDtl:str = obj["whereClausePendingRcvDtl"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.whereClauseSupplierXRef:str = obj["whereClauseSupplierXRef"]
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForAPInvoice_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReceiptTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForPO_input:
   """ Required : 
   whereClauseRcvHead
   whereClauseRcvHeadAttch
   whereClauseRcvHeadTax
   whereClauseRcvDtl
   whereClauseRcvDtlAttch
   whereClauseRcvDtlAttrValueSet
   whereClauseRcvDtlTax
   whereClauseRcvDuty
   whereClauseRcvMisc
   whereClauseRcvMiscTax
   whereClauseLegalNumGenOpts
   whereClausePendingRcvDtl
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   whereClauseSupplierXRef
   poNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRcvHead:str = obj["whereClauseRcvHead"]
      self.whereClauseRcvHeadAttch:str = obj["whereClauseRcvHeadAttch"]
      self.whereClauseRcvHeadTax:str = obj["whereClauseRcvHeadTax"]
      self.whereClauseRcvDtl:str = obj["whereClauseRcvDtl"]
      self.whereClauseRcvDtlAttch:str = obj["whereClauseRcvDtlAttch"]
      self.whereClauseRcvDtlAttrValueSet:str = obj["whereClauseRcvDtlAttrValueSet"]
      self.whereClauseRcvDtlTax:str = obj["whereClauseRcvDtlTax"]
      self.whereClauseRcvDuty:str = obj["whereClauseRcvDuty"]
      self.whereClauseRcvMisc:str = obj["whereClauseRcvMisc"]
      self.whereClauseRcvMiscTax:str = obj["whereClauseRcvMiscTax"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClausePendingRcvDtl:str = obj["whereClausePendingRcvDtl"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.whereClauseSupplierXRef:str = obj["whereClauseSupplierXRef"]
      self.poNum:int = obj["poNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForPO_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReceiptTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForPayment_input:
   """ Required : 
   whereClauseRcvHead
   whereClauseRcvHeadAttch
   whereClauseRcvHeadTax
   whereClauseRcvDtl
   whereClauseRcvDtlAttch
   whereClauseRcvDtlAttrValueSet
   whereClauseRcvDtlTax
   whereClauseRcvDuty
   whereClauseRcvMisc
   whereClauseRcvMiscTax
   whereClauseLegalNumGenOpts
   whereClausePendingRcvDtl
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   whereClauseSupplierXRef
   headNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRcvHead:str = obj["whereClauseRcvHead"]
      self.whereClauseRcvHeadAttch:str = obj["whereClauseRcvHeadAttch"]
      self.whereClauseRcvHeadTax:str = obj["whereClauseRcvHeadTax"]
      self.whereClauseRcvDtl:str = obj["whereClauseRcvDtl"]
      self.whereClauseRcvDtlAttch:str = obj["whereClauseRcvDtlAttch"]
      self.whereClauseRcvDtlAttrValueSet:str = obj["whereClauseRcvDtlAttrValueSet"]
      self.whereClauseRcvDtlTax:str = obj["whereClauseRcvDtlTax"]
      self.whereClauseRcvDuty:str = obj["whereClauseRcvDuty"]
      self.whereClauseRcvMisc:str = obj["whereClauseRcvMisc"]
      self.whereClauseRcvMiscTax:str = obj["whereClauseRcvMiscTax"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClausePendingRcvDtl:str = obj["whereClausePendingRcvDtl"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.whereClauseSupplierXRef:str = obj["whereClauseSupplierXRef"]
      self.headNum:int = obj["headNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForPayment_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReceiptTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseRcvHead
   whereClauseRcvHeadAttch
   whereClauseRcvHeadTax
   whereClauseRcvDtl
   whereClauseRcvDtlAttch
   whereClauseRcvDtlAttrValueSet
   whereClauseRcvDtlTax
   whereClauseRcvDuty
   whereClauseRcvMisc
   whereClauseRcvMiscTax
   whereClauseLegalNumGenOpts
   whereClausePendingRcvDtl
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   whereClauseSupplierXRef
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRcvHead:str = obj["whereClauseRcvHead"]
      self.whereClauseRcvHeadAttch:str = obj["whereClauseRcvHeadAttch"]
      self.whereClauseRcvHeadTax:str = obj["whereClauseRcvHeadTax"]
      self.whereClauseRcvDtl:str = obj["whereClauseRcvDtl"]
      self.whereClauseRcvDtlAttch:str = obj["whereClauseRcvDtlAttch"]
      self.whereClauseRcvDtlAttrValueSet:str = obj["whereClauseRcvDtlAttrValueSet"]
      self.whereClauseRcvDtlTax:str = obj["whereClauseRcvDtlTax"]
      self.whereClauseRcvDuty:str = obj["whereClauseRcvDuty"]
      self.whereClauseRcvMisc:str = obj["whereClauseRcvMisc"]
      self.whereClauseRcvMiscTax:str = obj["whereClauseRcvMiscTax"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClausePendingRcvDtl:str = obj["whereClausePendingRcvDtl"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.whereClauseSupplierXRef:str = obj["whereClauseSupplierXRef"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReceiptTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSNStatus_input:
   """ Required : 
   isReceived
   receivedToVal
   """  
   def __init__(self, obj):
      self.isReceived:bool = obj["isReceived"]
      self.receivedToVal:str = obj["receivedToVal"]
      pass

class GetSNStatus_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ipPartNum
   ipAttributeSetID
   ipQuantity
   ipUOM
   ipVendNum
   ipVendPP
   ipPackSlip
   ipPackSlipLine
   ipJobNum
   ipAsmSeq
   ipSubOprSeq
   ipReceivedTo
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      self.ipQuantity:int = obj["ipQuantity"]
      self.ipUOM:str = obj["ipUOM"]
      self.ipVendNum:int = obj["ipVendNum"]
      self.ipVendPP:str = obj["ipVendPP"]
      self.ipPackSlip:str = obj["ipPackSlip"]
      self.ipPackSlipLine:int = obj["ipPackSlipLine"]
      self.ipJobNum:str = obj["ipJobNum"]
      self.ipAsmSeq:int = obj["ipAsmSeq"]
      self.ipSubOprSeq:int = obj["ipSubOprSeq"]
      self.ipReceivedTo:str = obj["ipReceivedTo"]
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

class GetVendorInfo_input:
   """ Required : 
   ds
   vendorID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorID:str = obj["vendorID"]
      """  Proposed Vendor ID value  """  
      pass

class GetVendorInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["parameters"]
      self.purPoint:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetWarningPOClosed_input:
   """ Required : 
   poNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      """  PO Number  """  
      pass

class GetWarningPOClosed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class HHCanEditPackSlip_input:
   """ Required : 
   piPONum
   pcPackSlip
   """  
   def __init__(self, obj):
      self.piPONum:int = obj["piPONum"]
      """  A valid PONumber  """  
      self.pcPackSlip:str = obj["pcPackSlip"]
      """  Packing slip to check if this one was received  """  
      pass

class HHCanEditPackSlip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pbIsEdit:bool = obj["pbIsEdit"]
      pass

      """  output parameters  """  

class HHOnChangeDtlPOLine_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   poLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.packLine:int = obj["packLine"]
      self.poLine:int = obj["poLine"]
      pass

class HHOnChangeDtlPOLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class HHOnChangeDtlPORelNum_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   poRelNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.packLine:int = obj["packLine"]
      self.poRelNum:int = obj["poRelNum"]
      pass

class HHOnChangeDtlPORelNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class HHOnChangeDtlPartNum_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   partNum
   sysRowID
   rowType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.packLine:int = obj["packLine"]
      self.partNum:str = obj["partNum"]
      self.sysRowID:str = obj["sysRowID"]
      self.rowType:str = obj["rowType"]
      pass

class HHOnChangeDtlPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.partNum:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class HHValRecDocReq_input:
   """ Required : 
   partNum
   lotNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number  """  
      self.lotNum:str = obj["lotNum"]
      """  Part Lot number  """  
      pass

class HHValRecDocReq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.infoMsg:str = obj["parameters"]
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

class ImportReceipt_input:
   """ Required : 
   intQueId
   checkForManualPrompt
   ds
   """  
   def __init__(self, obj):
      self.intQueId:int = obj["intQueId"]
      """  Unique key of IMRcvHead  """  
      self.checkForManualPrompt:bool = obj["checkForManualPrompt"]
      """  If true then Get Legal Number defaults and check if Generate Type is manual and set RequiresUserInput appropriately, otherwise just generate Legal Number  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class ImportReceipt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vendorNum:int = obj["parameters"]
      self.purPoint:str = obj["parameters"]
      self.packSlip:str = obj["parameters"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      self.legalNumMsg:str = obj["parameters"]
      self.closedPOWarningMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class InitializeLandedCost_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      pass

class InitializeLandedCost_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MassReceiptTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.lcComment:str = obj["parameters"]
      self.lcReference:str = obj["parameters"]
      pass

      """  output parameters  """  

class IsContainerReceived_input:
   """ Required : 
   inContainerID
   """  
   def __init__(self, obj):
      self.inContainerID:int = obj["inContainerID"]
      pass

class IsContainerReceived_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class LCChangeLCAmt_input:
   """ Required : 
   ds
   packSlip
   packLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MassReceiptTableset] = obj["ds"]
      self.packSlip:str = obj["packSlip"]
      """  Receipt Pack Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line Number  """  
      pass

class LCChangeLCAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MassReceiptsGeneratePCIDUpdate_input:
   """ Required : 
   PCIDSGenerated
   pkgControlOutboundContainer
   ds
   """  
   def __init__(self, obj):
      self.PCIDSGenerated:str = obj["PCIDSGenerated"]
      self.pkgControlOutboundContainer:bool = obj["pkgControlOutboundContainer"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class MassReceiptsGeneratePCIDUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeContainerHdrArrivedDate_input:
   """ Required : 
   ds
   ipCompany
   ipContainerID
   ipNewArrivedDate
   ipOldArrivedDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.ipCompany:str = obj["ipCompany"]
      """  Container Company  """  
      self.ipContainerID:int = obj["ipContainerID"]
      """  ContainerID  """  
      self.ipNewArrivedDate:str = obj["ipNewArrivedDate"]
      """  Proposed arrived date to be validated  """  
      self.ipOldArrivedDate:str = obj["ipOldArrivedDate"]
      """  Previous arrived date  """  
      pass

class OnChangeContainerHdrArrivedDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.opNeedsRecalc:bool = obj["opNeedsRecalc"]
      pass

      """  output parameters  """  

class OnChangeContainerImportFld_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeContainerImportFld_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlBinNum_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   newBinNum
   requiresUserInput
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.newBinNum:str = obj["newBinNum"]
      """  New BinNum code to check  """  
      self.requiresUserInput:bool = obj["requiresUserInput"]
      """  Set to True if question / warnings are to be returned  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeDtlBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.questionMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlCommodity_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   ipCommCode
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.ipCommCode:str = obj["ipCommCode"]
      """  Proposed Commodity Code to be validated  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeDtlCommodity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlCountryNum_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   ipCountryNum
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.ipCountryNum:int = obj["ipCountryNum"]
      """  Proposed Country of Origin to be validated  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeDtlCountryNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlLCIndCost_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   ipLCIndCost
   LCIndCostSum
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.ipLCIndCost:int = obj["ipLCIndCost"]
      """  Proposed LC Indirect Cose to be validated  """  
      self.LCIndCostSum:int = obj["LCIndCostSum"]
      """  Total amount of Indirect cost on all the lines  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeDtlLCIndCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlPCID_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   pcid
   requiresUserInput
   selectedSerialNumberCount
   serialNumber
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.pcid:str = obj["pcid"]
      """  PCID  """  
      self.requiresUserInput:bool = obj["requiresUserInput"]
      """  Set to True if question / warnings are to be returned  """  
      self.selectedSerialNumberCount:int = obj["selectedSerialNumberCount"]
      """  Count of selected serial numbers if tracked used for validation  """  
      self.serialNumber:str = obj["serialNumber"]
      """  First Serial Number if tracked used for validation  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeDtlPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.questionMsg:str = obj["parameters"]
      self.warnMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlPOSelected_input:
   """ Required : 
   ds
   poNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.poNum:int = obj["poNum"]
      pass

class OnChangeDtlPOSelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.poStatusQstnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeDtlReceiptTypeTranType_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   receiptType
   tranType
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.packLine:int = obj["packLine"]
      self.receiptType:str = obj["receiptType"]
      self.tranType:str = obj["tranType"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeDtlReceiptTypeTranType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlReceiptType_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   receiptType
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.receiptType:str = obj["receiptType"]
      """  Receipt Type  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeDtlReceiptType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlReceived_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   ipReceived
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.ipReceived:bool = obj["ipReceived"]
      """  Received flag  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeDtlReceived_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlSelectedSinglePO_input:
   """ Required : 
   poNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      pass

class OnChangeDtlSelectedSinglePO_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.poStatusQstnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeDtlSupplierPrice_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      pass

class OnChangeDtlSupplierPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlTaxCatID_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   taxCatID
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.taxCatID:str = obj["taxCatID"]
      """  Tax Category  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeDtlTaxCatID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlTaxExempt_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   taxExempt
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.taxExempt:str = obj["taxExempt"]
      """  Tax Exempt  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeDtlTaxExempt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlUpliftPercent_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   ipUpliftPercent
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.ipUpliftPercent:int = obj["ipUpliftPercent"]
      """  Proposed Uplift Percentage to be validated  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeDtlUpliftPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDtlWareHouseCode_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   newWareHouseCode
   requiresUserInput
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.newWareHouseCode:str = obj["newWareHouseCode"]
      """  New warehouse code to check  """  
      self.requiresUserInput:bool = obj["requiresUserInput"]
      """  Set to True if question / warnings are to be returned  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeDtlWareHouseCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.questionMsg:str = obj["parameters"]
      self.warnMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDutyTariffCode_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   dutySeq
   ipTariffCode
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.dutySeq:int = obj["dutySeq"]
      """  Receipt Duty Sequence  """  
      self.ipTariffCode:str = obj["ipTariffCode"]
      """  Proposed Tariff Code to be validated  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeDutyTariffCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeHdrReceived_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   ipReceived
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.ipReceived:bool = obj["ipReceived"]
      """  Received flag  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeHdrReceived_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeHdrTaxRegionCode_input:
   """ Required : 
   newTaxRegionCode
   ds
   """  
   def __init__(self, obj):
      self.newTaxRegionCode:str = obj["newTaxRegionCode"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeHdrTaxRegionCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeHeaderTaxFixedAmount_input:
   """ Required : 
   proposedFixedAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedFixedAmt:int = obj["proposedFixedAmt"]
      """  The proposed fixed amount  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeHeaderTaxFixedAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeHeaderTaxRateCodeMaster_input:
   """ Required : 
   proposedRateCode
   ds
   """  
   def __init__(self, obj):
      self.proposedRateCode:str = obj["proposedRateCode"]
      """  The proposed rate code  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeHeaderTaxRateCodeMaster_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeHeaderTaxRateCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeHeaderTaxRateCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeHeaderTaxReportableAmt_input:
   """ Required : 
   proposedReportableAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedReportableAmt:int = obj["proposedReportableAmt"]
      """  The proposed reportable amount  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeHeaderTaxReportableAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeHeaderTaxTaxAmt_input:
   """ Required : 
   proposedTaxAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxAmt:int = obj["proposedTaxAmt"]
      """  The proposed tax amount  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeHeaderTaxTaxAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeHeaderTaxTaxCode_input:
   """ Required : 
   proposedTaxCode
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxCode:str = obj["proposedTaxCode"]
      """  The proposed tax code  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeHeaderTaxTaxCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeHeaderTaxTaxDeductable_input:
   """ Required : 
   proposedTaxDeductable
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxDeductable:int = obj["proposedTaxDeductable"]
      """  The proposed tax deductable  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeHeaderTaxTaxDeductable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeHeaderTaxTaxPercent_input:
   """ Required : 
   proposedTaxPercent
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxPercent:int = obj["proposedTaxPercent"]
      """  The proposed tax percent  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeHeaderTaxTaxPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeHeaderTaxTaxableAmt_input:
   """ Required : 
   proposedTaxableAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxableAmt:int = obj["proposedTaxableAmt"]
      """  The proposed taxable amount  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeHeaderTaxTaxableAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeInspReq_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   packLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Packing slip number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line  """  
      pass

class OnChangeInspReq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscApplyDate_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   miscSeq
   ipApplyDate
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.miscSeq:int = obj["miscSeq"]
      """  Receipt Indirect Cost Sequence  """  
      self.ipApplyDate:str = obj["ipApplyDate"]
      """  Proposed Apply Date to be validated  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeMiscApplyDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscCharge_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   miscSeq
   ipChargeID
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.miscSeq:int = obj["miscSeq"]
      """  Receipt Indirect Cost Sequence  """  
      self.ipChargeID:str = obj["ipChargeID"]
      """  Proposed PurMisc ID to be validated  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeMiscCharge_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscCurrencyCode_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   miscSeq
   ipCurrCode
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.miscSeq:int = obj["miscSeq"]
      """  Receipt Indirect Cost Sequence  """  
      self.ipCurrCode:str = obj["ipCurrCode"]
      """  Proposed Currency Code to be validated  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeMiscCurrencyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscDocActualAmt_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   miscSeq
   ipDocActualAmt
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.miscSeq:int = obj["miscSeq"]
      """  Receipt Indirect Cost Sequence  """  
      self.ipDocActualAmt:int = obj["ipDocActualAmt"]
      """  Proposed Actual Amount in document currency  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeMiscDocActualAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscExchangeRate_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   miscSeq
   ipExchangeRate
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.miscSeq:int = obj["miscSeq"]
      """  Receipt Indirect Cost Sequence  """  
      self.ipExchangeRate:int = obj["ipExchangeRate"]
      """  Proposed Currency Exchange Rate to be validated  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeMiscExchangeRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscInvoiceLine_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   miscSeq
   ipInvLine
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.miscSeq:int = obj["miscSeq"]
      """  Receipt Indirect Cost Sequence  """  
      self.ipInvLine:int = obj["ipInvLine"]
      """  The AP Invoice Line to be validated  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeMiscInvoiceLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscInvoiceNum_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   miscSeq
   ipInvNum
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.miscSeq:int = obj["miscSeq"]
      """  Receipt Indirect Cost Sequence  """  
      self.ipInvNum:str = obj["ipInvNum"]
      """  The AP Invoice Number to be validated  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeMiscInvoiceNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscMscNum_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   miscSeq
   ipMscNum
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.miscSeq:int = obj["miscSeq"]
      """  Receipt Indirect Cost Sequence  """  
      self.ipMscNum:int = obj["ipMscNum"]
      """  The AP Invoice Line Miscellaneous Sequence Number to be validated  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeMiscMscNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscPercent_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   miscSeq
   ipPercent
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.miscSeq:int = obj["miscSeq"]
      """  Receipt Indirect Cost Sequence  """  
      self.ipPercent:int = obj["ipPercent"]
      """  Proposed Actual Amount in document currency  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeMiscPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscRateGrp_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   miscSeq
   ipRateGrpCode
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.miscSeq:int = obj["miscSeq"]
      """  Receipt Indirect Cost Sequence  """  
      self.ipRateGrpCode:str = obj["ipRateGrpCode"]
      """  Proposed Currency Rate Group Code to be validated  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeMiscRateGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscTaxCatID_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   miscSeq
   taxCatID
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.miscSeq:int = obj["miscSeq"]
      self.taxCatID:str = obj["taxCatID"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeMiscTaxCatID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscVendor_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   miscSeq
   vendID
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.miscSeq:int = obj["miscSeq"]
      """  Receipt Indirect Cost Sequence  """  
      self.vendID:str = obj["vendID"]
      """  Proposed vendor ID to be validated  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeMiscVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeReceiptDate_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   received
   partNum
   rcvDate
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.received:bool = obj["received"]
      """  If the POLine or the Pack Slip has been receipt or not  """  
      self.partNum:str = obj["partNum"]
      """  Set to True if question / warnings are to be returned  """  
      self.rcvDate:str = obj["rcvDate"]
      """  Receipt Date.  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeReceiptDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.wrnLines:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxDeductable_input:
   """ Required : 
   tableName
   proposedTaxDeductable
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name RcvMiscTax or RcvDtlTax  """  
      self.proposedTaxDeductable:int = obj["proposedTaxDeductable"]
      """  The proposed tax deductible  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeTaxDeductable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxFixedAmount_input:
   """ Required : 
   tableName
   proposedFixedAmt
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name RcvMiscTax or RcvDtlTax  """  
      self.proposedFixedAmt:int = obj["proposedFixedAmt"]
      """  The proposed reportable amount  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeTaxFixedAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxPercent_input:
   """ Required : 
   tableName
   proposedTaxPercent
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name RcvMiscTax or RcvDtlTax  """  
      self.proposedTaxPercent:int = obj["proposedTaxPercent"]
      """  The proposed tax percent  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeTaxPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxRateCode_input:
   """ Required : 
   tableName
   proposedRateCode
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name RcvMiscTax or RcvDtlTax  """  
      self.proposedRateCode:str = obj["proposedRateCode"]
      """  The proposed rate code  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeTaxRateCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxReportableAmt_input:
   """ Required : 
   tableName
   proposedReportableAmt
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name RcvMiscTax or RcvDtlTax  """  
      self.proposedReportableAmt:int = obj["proposedReportableAmt"]
      """  The proposed reportable amount  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeTaxReportableAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxTaxAmt_input:
   """ Required : 
   tableName
   proposedTaxAmt
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name RcvMiscTax or RcvDtlTax  """  
      self.proposedTaxAmt:int = obj["proposedTaxAmt"]
      """  The proposed tax amount  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeTaxTaxAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxTaxCode_input:
   """ Required : 
   tableName
   proposedTaxCode
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name RcvMiscTax or RcvDtlTax  """  
      self.proposedTaxCode:str = obj["proposedTaxCode"]
      """  The proposed tax code  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeTaxTaxCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxTaxableAmt_input:
   """ Required : 
   tableName
   proposedTaxableAmt
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name RcvMiscTax or RcvDtlTax  """  
      self.proposedTaxableAmt:int = obj["proposedTaxableAmt"]
      """  The proposed taxable amount  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangeTaxTaxableAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedDtlPOTransValue_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line to check  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangedDtlPOTransValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedHeaderTaxManual_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangedHeaderTaxManual_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedTaxManual_input:
   """ Required : 
   tableName
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name RcvMiscTax or RcvDtlTax  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class OnChangedTaxManual_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreReceiveContainer_input:
   """ Required : 
   inContainerID
   """  
   def __init__(self, obj):
      self.inContainerID:int = obj["inContainerID"]
      pass

class PreReceiveContainer_output:
   def __init__(self, obj):
      pass

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.RequiresUserInput:bool = obj["RequiresUserInput"]
      pass

      """  output parameters  """  

class ProcessIM_input:
   """ Required : 
   pintQueId
   curpackSlip
   ds
   """  
   def __init__(self, obj):
      self.pintQueId:int = obj["pintQueId"]
      """  A valid IntQueId  """  
      self.curpackSlip:str = obj["curpackSlip"]
      """  Packing slip number  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class ProcessIM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessLandedCosts_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      pass

class ProcessLandedCosts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReceiptTableset] = obj["returnObj"]
      pass

class RcvDtlNegInvCheck_input:
   """ Required : 
   company
   vendorNum
   purPoint
   packSlip
   packLine
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company  """  
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Num  """  
      self.purPoint:str = obj["purPoint"]
      """  Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Packing Slip Num  """  
      self.packLine:int = obj["packLine"]
      """  Packing Slip Line  """  
      pass

class RcvDtlNegInvCheck_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.negQtyAction:str = obj["parameters"]
      self.msg:str = obj["parameters"]
      pass

      """  output parameters  """  

class RcvHeadNegInvCheck_input:
   """ Required : 
   company
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company  """  
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Num  """  
      self.purPoint:str = obj["purPoint"]
      """  Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Packing Slip Num  """  
      pass

class RcvHeadNegInvCheck_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.negQtyAction:str = obj["parameters"]
      self.msg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ReceiveAllLines_input:
   """ Required : 
   ipReceived
   ds
   """  
   def __init__(self, obj):
      self.ipReceived:bool = obj["ipReceived"]
      """  Received flag  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class ReceiveAllLines_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ReceiveAll_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class ReceiveAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ReceiveContainerUpdateUsingArriveDate_input:
   """ Required : 
   ds
   inContainerID
   ipArrivedDate
   inCreateNewPoRels
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.inContainerID:int = obj["inContainerID"]
      self.ipArrivedDate:str = obj["ipArrivedDate"]
      """  Arrived Date  """  
      self.inCreateNewPoRels:str = obj["inCreateNewPoRels"]
      pass

class ReceiveContainerUpdateUsingArriveDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.outEshReceived:bool = obj["outEshReceived"]
      self.outPartialReceipt:bool = obj["outPartialReceipt"]
      self.outReceiveAll:bool = obj["outReceiveAll"]
      pass

      """  output parameters  """  

class ReceiveContainerUpdate_input:
   """ Required : 
   ds
   inContainerID
   inCreateNewPoRels
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.inContainerID:int = obj["inContainerID"]
      self.inCreateNewPoRels:str = obj["inCreateNewPoRels"]
      pass

class ReceiveContainerUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.outEshReceived:bool = obj["outEshReceived"]
      self.outPartialReceipt:bool = obj["outPartialReceipt"]
      self.outReceiveAll:bool = obj["outReceiveAll"]
      pass

      """  output parameters  """  

class ReceiveContainerUsingArrivedDate_input:
   """ Required : 
   ds
   inContainerID
   ipArrivedDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.inContainerID:int = obj["inContainerID"]
      self.ipArrivedDate:str = obj["ipArrivedDate"]
      pass

class ReceiveContainerUsingArrivedDate_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ContainerTrackingTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ReceiveContainer_input:
   """ Required : 
   ds
   inContainerID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      self.inContainerID:int = obj["inContainerID"]
      pass

class ReceiveContainer_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ContainerTrackingTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ResetLandedCostDisbursements_input:
   """ Required : 
   ipVendorNum
   ipPurPoint
   ipPackSlip
   ipDisburseMethod
   """  
   def __init__(self, obj):
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  Vendor Number to reset  """  
      self.ipPurPoint:str = obj["ipPurPoint"]
      """  Purchase Point to reset  """  
      self.ipPackSlip:str = obj["ipPackSlip"]
      """  Packing Slip Number to reset  """  
      self.ipDisburseMethod:str = obj["ipDisburseMethod"]
      """  Landed Cost Disbursment method  """  
      pass

class ResetLandedCostDisbursements_output:
   def __init__(self, obj):
      pass

class SetPrimaryBin_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Purchase Point Number  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Slip Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line number  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class SetPrimaryBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetToLocation_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Purchase Point Number  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Slip Number  """  
      self.packLine:int = obj["packLine"]
      """  Receipt Line number  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class SetToLocation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtReceiptTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtReceiptTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateMaster_input:
   """ Required : 
   RunChkLCAmtBeforeUpdate
   RunChkHdrBeforeUpdate
   ipVendorNum
   ipPurPoint
   ipPackSlip
   ipPackLine
   lRunChkDtl
   lRunChkDtlCompliance
   lRunCheckCompliance
   lRunPreUpdate
   lRunCreatePartLot
   partNum
   lotNum
   lOkToUpdate
   ds
   """  
   def __init__(self, obj):
      self.RunChkLCAmtBeforeUpdate:bool = obj["RunChkLCAmtBeforeUpdate"]
      """  bool to determine whether to run certain code segment  """  
      self.RunChkHdrBeforeUpdate:bool = obj["RunChkHdrBeforeUpdate"]
      """  bool to determine whether to run certain code segment  """  
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  current vendor number  """  
      self.ipPurPoint:str = obj["ipPurPoint"]
      """  current PurPoint  """  
      self.ipPackSlip:str = obj["ipPackSlip"]
      """  current packSlip  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  current packLine  """  
      self.lRunChkDtl:bool = obj["lRunChkDtl"]
      """  bool to determine whether to run certain code segment  """  
      self.lRunChkDtlCompliance:bool = obj["lRunChkDtlCompliance"]
      """  bool to determine whether to run certain code segment  """  
      self.lRunCheckCompliance:bool = obj["lRunCheckCompliance"]
      """  bool to determine whether to run certain code segment  """  
      self.lRunPreUpdate:bool = obj["lRunPreUpdate"]
      """  bool to determine whether to run certain code segment  """  
      self.lRunCreatePartLot:bool = obj["lRunCreatePartLot"]
      """  bool to determine whether to run certain code segment  """  
      self.partNum:str = obj["partNum"]
      """  current partNum  """  
      self.lotNum:str = obj["lotNum"]
      """  current lotNum  """  
      self.lOkToUpdate:bool = obj["lOkToUpdate"]
      """  bool to determine if the Update should be run in this process  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class UpdateMaster_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cLCAmtMessage:str = obj["parameters"]
      self.opUpliftWarnMsg:str = obj["parameters"]
      self.opReceiptWarnMsg:str = obj["parameters"]
      self.opArriveWarnMsg:str = obj["parameters"]
      self.qMessageStr:str = obj["parameters"]
      self.sMessageStr:str = obj["parameters"]
      self.lcMessageStr:str = obj["parameters"]
      self.pcMessageStr:str = obj["parameters"]
      self.qDtlComplianceMsgStr:str = obj["parameters"]
      self.lCompliant:bool = obj["lCompliant"]
      self.lRequiresUserInput:bool = obj["lRequiresUserInput"]
      self.lUpdateWasRun:bool = obj["lUpdateWasRun"]
      self.wrnLines:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateOurQtyFromAttributes_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class UpdateOurQtyFromAttributes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateMRPONum_input:
   """ Required : 
   poNum
   vendorNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      """  The PO Number to validate  """  
      self.vendorNum:int = obj["vendorNum"]
      """  The Receipt Header Vendor's Number  """  
      pass

class ValidateMRPONum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidatePONum_input:
   """ Required : 
   poNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      """  The PO Number to validate  """  
      pass

class ValidatePONum_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateReceiptRecords_input:
   """ Required : 
   tableName
   vendorNum
   purPoint
   packSlip
   packLine
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.packLine:int = obj["packLine"]
      pass

class ValidateReceiptRecords_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateSMIReceiptAttrPart_input:
   """ Required : 
   vendorNum
   purPoint
   poNum
   packSlip
   partNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Receipt Purchase Point  """  
      self.poNum:int = obj["poNum"]
      """  PO Number for Purchase Order Receipts  """  
      self.packSlip:str = obj["packSlip"]
      """  Receipt Packing Number  """  
      self.partNum:str = obj["partNum"]
      """  Receipt Part Number  """  
      pass

class ValidateSMIReceiptAttrPart_output:
   def __init__(self, obj):
      pass

class ValidateSN_input:
   """ Required : 
   ipPartNum
   ipAttributeSetID
   ipSerialNo
   ipVendorNum
   ipJobNum
   ipAsmSeq
   ipSubOprSeq
   ipPackSlip
   ipPackLine
   ipReceivedTo
   ipJobSeqType
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      self.ipSerialNo:str = obj["ipSerialNo"]
      self.ipVendorNum:int = obj["ipVendorNum"]
      self.ipJobNum:str = obj["ipJobNum"]
      self.ipAsmSeq:int = obj["ipAsmSeq"]
      self.ipSubOprSeq:int = obj["ipSubOprSeq"]
      self.ipPackSlip:str = obj["ipPackSlip"]
      self.ipPackLine:int = obj["ipPackLine"]
      self.ipReceivedTo:str = obj["ipReceivedTo"]
      self.ipJobSeqType:str = obj["ipJobSeqType"]
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class VoidLegalNumber_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   voidReason
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  Packing Slip  """  
      self.voidReason:str = obj["voidReason"]
      """  The void reason text  """  
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

class VoidLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class chkUnReceive_input:
   """ Required : 
   ipPONum
   ipPOLine
   ipPORelNum
   ipPackSlip
   ipPackLine
   """  
   def __init__(self, obj):
      self.ipPONum:int = obj["ipPONum"]
      self.ipPOLine:int = obj["ipPOLine"]
      self.ipPORelNum:int = obj["ipPORelNum"]
      self.ipPackSlip:str = obj["ipPackSlip"]
      self.ipPackLine:int = obj["ipPackLine"]
      pass

class chkUnReceive_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

