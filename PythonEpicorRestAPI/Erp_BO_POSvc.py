import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.POSvc
# Description: Purchase Order Entry
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_POes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get POes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes",headers=creds) as resp:
           return await resp.json()

async def post_POes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.POHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_POes_Company_PONum(Company, PONum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PO item
   Description: Calls GetByID to retrieve the PO item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PO
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_POes_Company_PONum(Company, PONum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PO for the service
   Description: Calls UpdateExt to update PO. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PO
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.POHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_POes_Company_PONum(Company, PONum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PO item
   Description: Call UpdateExt to delete PO item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PO
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")",headers=creds) as resp:
           return await resp.json()

async def get_POes_Company_PONum_PODetails(Company, PONum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PODetails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PODetails1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/PODetails",headers=creds) as resp:
           return await resp.json()

async def get_POes_Company_PONum_PODetails_Company_PONUM_POLine(Company, PONum, PONUM, POLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PODetail item
   Description: Calls GetByID to retrieve the PODetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetail1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/PODetails(" + Company + "," + PONUM + "," + POLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_POes_Company_PONum_POHeadMiscs(Company, PONum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get POHeadMiscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_POHeadMiscs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeadMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/POHeadMiscs",headers=creds) as resp:
           return await resp.json()

async def get_POes_Company_PONum_POHeadMiscs_Company_PONum_POLine_SeqNum(Company, PONum, POLine, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the POHeadMisc item
   Description: Calls GetByID to retrieve the POHeadMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POHeadMisc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeadMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/POHeadMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_POes_Company_PONum_POHeaderMiscTaxes(Company, PONum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get POHeaderMiscTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_POHeaderMiscTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeaderMiscTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/POHeaderMiscTaxes",headers=creds) as resp:
           return await resp.json()

async def get_POes_Company_PONum_POHeaderMiscTaxes_Company_PONum_SeqNum_TaxCode_RateCode_ECAcquisitionSeq(Company, PONum, SeqNum, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the POHeaderMiscTax item
   Description: Calls GetByID to retrieve the POHeaderMiscTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POHeaderMiscTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeaderMiscTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/POHeaderMiscTaxes(" + Company + "," + PONum + "," + SeqNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_POes_Company_PONum_POHeaderTaxes(Company, PONum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get POHeaderTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_POHeaderTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeaderTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/POHeaderTaxes",headers=creds) as resp:
           return await resp.json()

async def get_POes_Company_PONum_POHeaderTaxes_Company_PONum_TaxCode_RateCode_ECAcquisitionSeq(Company, PONum, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the POHeaderTax item
   Description: Calls GetByID to retrieve the POHeaderTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POHeaderTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeaderTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/POHeaderTaxes(" + Company + "," + PONum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_POes_Company_PONum_POHeaderAttches(Company, PONum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get POHeaderAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_POHeaderAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeaderAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/POHeaderAttches",headers=creds) as resp:
           return await resp.json()

async def get_POes_Company_PONum_POHeaderAttches_Company_PONum_DrawingSeq(Company, PONum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the POHeaderAttch item
   Description: Calls GetByID to retrieve the POHeaderAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POHeaderAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeaderAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/POHeaderAttches(" + Company + "," + PONum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PODetails(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PODetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PODetails
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails",headers=creds) as resp:
           return await resp.json()

async def post_PODetails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PODetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PODetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PODetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PODetails_Company_PONUM_POLine(Company, PONUM, POLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PODetail item
   Description: Calls GetByID to retrieve the PODetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PODetails_Company_PONUM_POLine(Company, PONUM, POLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PODetail for the service
   Description: Calls UpdateExt to update PODetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PODetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PODetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PODetails_Company_PONUM_POLine(Company, PONUM, POLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PODetail item
   Description: Call UpdateExt to delete PODetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PODetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_PODetails_Company_PONUM_POLine_PORels(Company, PONUM, POLine, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PORels items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PORels1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/PORels",headers=creds) as resp:
           return await resp.json()

async def get_PODetails_Company_PONUM_POLine_PORels_Company_PONum_POLine_PORelNum(Company, PONUM, POLine, PONum, PORelNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PORel item
   Description: Calls GetByID to retrieve the PORel item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORel1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PONum: Desc: PONum   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PODetails_Company_PONUM_POLine_PODetailInsps(Company, PONUM, POLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PODetailInsps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PODetailInsps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/PODetailInsps",headers=creds) as resp:
           return await resp.json()

async def get_PODetails_Company_PONUM_POLine_PODetailInsps_Company_PONUM_POLine_PlanSeq(Company, PONUM, POLine, PlanSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PODetailInsp item
   Description: Calls GetByID to retrieve the PODetailInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailInsp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/PODetailInsps(" + Company + "," + PONUM + "," + POLine + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PODetails_Company_PONUM_POLine_PODetailTaxes(Company, PONUM, POLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PODetailTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PODetailTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/PODetailTaxes",headers=creds) as resp:
           return await resp.json()

async def get_PODetails_Company_PONUM_POLine_PODetailTaxes_Company_PONum_POLine_TaxCode_RateCode_ECAcquisitionSeq(Company, PONUM, POLine, PONum, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PODetailTax item
   Description: Calls GetByID to retrieve the PODetailTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PONum: Desc: PONum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/PODetailTaxes(" + Company + "," + PONum + "," + POLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PODetails_Company_PONUM_POLine_POMiscs(Company, PONUM, POLine, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get POMiscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_POMiscs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/POMiscs",headers=creds) as resp:
           return await resp.json()

async def get_PODetails_Company_PONUM_POLine_POMiscs_Company_PONum_POLine_SeqNum(Company, PONUM, POLine, PONum, SeqNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the POMisc item
   Description: Calls GetByID to retrieve the POMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POMisc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PONum: Desc: PONum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/POMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PODetails_Company_PONUM_POLine_PODetailAttches(Company, PONUM, POLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PODetailAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PODetailAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/PODetailAttches",headers=creds) as resp:
           return await resp.json()

async def get_PODetails_Company_PONUM_POLine_PODetailAttches_Company_PONUM_POLine_DrawingSeq(Company, PONUM, POLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PODetailAttch item
   Description: Calls GetByID to retrieve the PODetailAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/PODetailAttches(" + Company + "," + PONUM + "," + POLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PORels(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PORels items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PORels
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels",headers=creds) as resp:
           return await resp.json()

async def post_PORels(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PORels
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PORelRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PORelRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PORels_Company_PONum_POLine_PORelNum(Company, PONum, POLine, PORelNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PORel item
   Description: Calls GetByID to retrieve the PORel item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORel
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PORels_Company_PONum_POLine_PORelNum(Company, PONum, POLine, PORelNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PORel for the service
   Description: Calls UpdateExt to update PORel. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PORel
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PORelRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PORels_Company_PONum_POLine_PORelNum(Company, PONum, POLine, PORelNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PORel item
   Description: Call UpdateExt to delete PORel item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PORel
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PORels_Company_PONum_POLine_PORelNum_PORelTGLCs(Company, PONum, POLine, PORelNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PORelTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PORelTGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")/PORelTGLCs",headers=creds) as resp:
           return await resp.json()

async def get_PORels_Company_PONum_POLine_PORelNum_PORelTGLCs_Company_PONum_POLine_PORelNum_BookID(Company, PONum, POLine, PORelNum, BookID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PORelTGLC item
   Description: Calls GetByID to retrieve the PORelTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORelTGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")/PORelTGLCs(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + BookID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PORels_Company_PONum_POLine_PORelNum_PORelTaxes(Company, PONum, POLine, PORelNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PORelTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PORelTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")/PORelTaxes",headers=creds) as resp:
           return await resp.json()

async def get_PORels_Company_PONum_POLine_PORelNum_PORelTaxes_Company_PONum_POLine_PORelNum_TaxCode_RateCode_ECAcquisitionSeq(Company, PONum, POLine, PORelNum, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PORelTax item
   Description: Calls GetByID to retrieve the PORelTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORelTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")/PORelTaxes(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PORels_Company_PONum_POLine_PORelNum_PORelAttches(Company, PONum, POLine, PORelNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PORelAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PORelAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")/PORelAttches",headers=creds) as resp:
           return await resp.json()

async def get_PORels_Company_PONum_POLine_PORelNum_PORelAttches_Company_PONum_POLine_PORelNum_DrawingSeq(Company, PONum, POLine, PORelNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PORelAttch item
   Description: Calls GetByID to retrieve the PORelAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORelAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")/PORelAttches(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PORelTGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PORelTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PORelTGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTGLCs",headers=creds) as resp:
           return await resp.json()

async def post_PORelTGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PORelTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PORelTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PORelTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PORelTGLCs_Company_PONum_POLine_PORelNum_BookID(Company, PONum, POLine, PORelNum, BookID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PORelTGLC item
   Description: Calls GetByID to retrieve the PORelTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORelTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTGLCs(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + BookID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PORelTGLCs_Company_PONum_POLine_PORelNum_BookID(Company, PONum, POLine, PORelNum, BookID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PORelTGLC for the service
   Description: Calls UpdateExt to update PORelTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PORelTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PORelTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTGLCs(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + BookID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PORelTGLCs_Company_PONum_POLine_PORelNum_BookID(Company, PONum, POLine, PORelNum, BookID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PORelTGLC item
   Description: Call UpdateExt to delete PORelTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PORelTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTGLCs(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + BookID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PORelTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PORelTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PORelTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTaxes",headers=creds) as resp:
           return await resp.json()

async def post_PORelTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PORelTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PORelTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PORelTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PORelTaxes_Company_PONum_POLine_PORelNum_TaxCode_RateCode_ECAcquisitionSeq(Company, PONum, POLine, PORelNum, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PORelTax item
   Description: Calls GetByID to retrieve the PORelTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORelTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTaxes(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PORelTaxes_Company_PONum_POLine_PORelNum_TaxCode_RateCode_ECAcquisitionSeq(Company, PONum, POLine, PORelNum, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PORelTax for the service
   Description: Calls UpdateExt to update PORelTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PORelTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PORelTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTaxes(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PORelTaxes_Company_PONum_POLine_PORelNum_TaxCode_RateCode_ECAcquisitionSeq(Company, PONum, POLine, PORelNum, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PORelTax item
   Description: Call UpdateExt to delete PORelTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PORelTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTaxes(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PORelAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PORelAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PORelAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelAttches",headers=creds) as resp:
           return await resp.json()

async def post_PORelAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PORelAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PORelAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PORelAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PORelAttches_Company_PONum_POLine_PORelNum_DrawingSeq(Company, PONum, POLine, PORelNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PORelAttch item
   Description: Calls GetByID to retrieve the PORelAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORelAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelAttches(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PORelAttches_Company_PONum_POLine_PORelNum_DrawingSeq(Company, PONum, POLine, PORelNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PORelAttch for the service
   Description: Calls UpdateExt to update PORelAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PORelAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PORelAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelAttches(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PORelAttches_Company_PONum_POLine_PORelNum_DrawingSeq(Company, PONum, POLine, PORelNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PORelAttch item
   Description: Call UpdateExt to delete PORelAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PORelAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelAttches(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PODetailInsps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PODetailInsps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PODetailInsps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailInsps",headers=creds) as resp:
           return await resp.json()

async def post_PODetailInsps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PODetailInsps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PODetailInspRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PODetailInspRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailInsps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PODetailInsps_Company_PONUM_POLine_PlanSeq(Company, PONUM, POLine, PlanSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PODetailInsp item
   Description: Calls GetByID to retrieve the PODetailInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailInsps(" + Company + "," + PONUM + "," + POLine + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PODetailInsps_Company_PONUM_POLine_PlanSeq(Company, PONUM, POLine, PlanSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PODetailInsp for the service
   Description: Calls UpdateExt to update PODetailInsp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PODetailInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PODetailInspRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailInsps(" + Company + "," + PONUM + "," + POLine + "," + PlanSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PODetailInsps_Company_PONUM_POLine_PlanSeq(Company, PONUM, POLine, PlanSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PODetailInsp item
   Description: Call UpdateExt to delete PODetailInsp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PODetailInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailInsps(" + Company + "," + PONUM + "," + POLine + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PODetailTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PODetailTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PODetailTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailTaxes",headers=creds) as resp:
           return await resp.json()

async def post_PODetailTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PODetailTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PODetailTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PODetailTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PODetailTaxes_Company_PONum_POLine_TaxCode_RateCode_ECAcquisitionSeq(Company, PONum, POLine, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PODetailTax item
   Description: Calls GetByID to retrieve the PODetailTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailTaxes(" + Company + "," + PONum + "," + POLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PODetailTaxes_Company_PONum_POLine_TaxCode_RateCode_ECAcquisitionSeq(Company, PONum, POLine, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PODetailTax for the service
   Description: Calls UpdateExt to update PODetailTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PODetailTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PODetailTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailTaxes(" + Company + "," + PONum + "," + POLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PODetailTaxes_Company_PONum_POLine_TaxCode_RateCode_ECAcquisitionSeq(Company, PONum, POLine, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PODetailTax item
   Description: Call UpdateExt to delete PODetailTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PODetailTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailTaxes(" + Company + "," + PONum + "," + POLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_POMiscs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get POMiscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POMiscs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POMiscs",headers=creds) as resp:
           return await resp.json()

async def post_POMiscs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POMiscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POMiscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.POMiscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POMiscs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_POMiscs_Company_PONum_POLine_SeqNum(Company, PONum, POLine, SeqNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the POMisc item
   Description: Calls GetByID to retrieve the POMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_POMiscs_Company_PONum_POLine_SeqNum(Company, PONum, POLine, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update POMisc for the service
   Description: Calls UpdateExt to update POMisc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.POMiscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_POMiscs_Company_PONum_POLine_SeqNum(Company, PONum, POLine, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete POMisc item
   Description: Call UpdateExt to delete POMisc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_POMiscs_Company_PONum_POLine_SeqNum_PODetailMiscTaxes(Company, PONum, POLine, SeqNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PODetailMiscTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PODetailMiscTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailMiscTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")/PODetailMiscTaxes",headers=creds) as resp:
           return await resp.json()

async def get_POMiscs_Company_PONum_POLine_SeqNum_PODetailMiscTaxes_Company_PONUM_POLine_SeqNum_TaxCode_RateCode_ECAcquisitionSeq(Company, PONum, POLine, SeqNum, PONUM, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PODetailMiscTax item
   Description: Calls GetByID to retrieve the PODetailMiscTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailMiscTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param PONUM: Desc: PONUM   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailMiscTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")/PODetailMiscTaxes(" + Company + "," + PONUM + "," + POLine + "," + SeqNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PODetailMiscTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PODetailMiscTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PODetailMiscTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailMiscTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailMiscTaxes",headers=creds) as resp:
           return await resp.json()

async def post_PODetailMiscTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PODetailMiscTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PODetailMiscTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PODetailMiscTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailMiscTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PODetailMiscTaxes_Company_PONUM_POLine_SeqNum_TaxCode_RateCode_ECAcquisitionSeq(Company, PONUM, POLine, SeqNum, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PODetailMiscTax item
   Description: Calls GetByID to retrieve the PODetailMiscTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailMiscTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailMiscTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailMiscTaxes(" + Company + "," + PONUM + "," + POLine + "," + SeqNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PODetailMiscTaxes_Company_PONUM_POLine_SeqNum_TaxCode_RateCode_ECAcquisitionSeq(Company, PONUM, POLine, SeqNum, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PODetailMiscTax for the service
   Description: Calls UpdateExt to update PODetailMiscTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PODetailMiscTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PODetailMiscTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailMiscTaxes(" + Company + "," + PONUM + "," + POLine + "," + SeqNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PODetailMiscTaxes_Company_PONUM_POLine_SeqNum_TaxCode_RateCode_ECAcquisitionSeq(Company, PONUM, POLine, SeqNum, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PODetailMiscTax item
   Description: Call UpdateExt to delete PODetailMiscTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PODetailMiscTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailMiscTaxes(" + Company + "," + PONUM + "," + POLine + "," + SeqNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PODetailAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PODetailAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PODetailAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailAttches",headers=creds) as resp:
           return await resp.json()

async def post_PODetailAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PODetailAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PODetailAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PODetailAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PODetailAttches_Company_PONUM_POLine_DrawingSeq(Company, PONUM, POLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PODetailAttch item
   Description: Calls GetByID to retrieve the PODetailAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailAttches(" + Company + "," + PONUM + "," + POLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PODetailAttches_Company_PONUM_POLine_DrawingSeq(Company, PONUM, POLine, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PODetailAttch for the service
   Description: Calls UpdateExt to update PODetailAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PODetailAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PODetailAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailAttches(" + Company + "," + PONUM + "," + POLine + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PODetailAttches_Company_PONUM_POLine_DrawingSeq(Company, PONUM, POLine, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PODetailAttch item
   Description: Call UpdateExt to delete PODetailAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PODetailAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailAttches(" + Company + "," + PONUM + "," + POLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_POHeadMiscs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get POHeadMiscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POHeadMiscs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeadMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeadMiscs",headers=creds) as resp:
           return await resp.json()

async def post_POHeadMiscs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POHeadMiscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POHeadMiscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.POHeadMiscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeadMiscs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_POHeadMiscs_Company_PONum_POLine_SeqNum(Company, PONum, POLine, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the POHeadMisc item
   Description: Calls GetByID to retrieve the POHeadMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POHeadMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeadMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeadMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_POHeadMiscs_Company_PONum_POLine_SeqNum(Company, PONum, POLine, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update POHeadMisc for the service
   Description: Calls UpdateExt to update POHeadMisc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POHeadMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.POHeadMiscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeadMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_POHeadMiscs_Company_PONum_POLine_SeqNum(Company, PONum, POLine, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete POHeadMisc item
   Description: Call UpdateExt to delete POHeadMisc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POHeadMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeadMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_POHeaderMiscTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get POHeaderMiscTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POHeaderMiscTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeaderMiscTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderMiscTaxes",headers=creds) as resp:
           return await resp.json()

async def post_POHeaderMiscTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POHeaderMiscTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POHeaderMiscTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.POHeaderMiscTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderMiscTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_POHeaderMiscTaxes_Company_PONum_SeqNum_TaxCode_RateCode_ECAcquisitionSeq(Company, PONum, SeqNum, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the POHeaderMiscTax item
   Description: Calls GetByID to retrieve the POHeaderMiscTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POHeaderMiscTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeaderMiscTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderMiscTaxes(" + Company + "," + PONum + "," + SeqNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_POHeaderMiscTaxes_Company_PONum_SeqNum_TaxCode_RateCode_ECAcquisitionSeq(Company, PONum, SeqNum, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update POHeaderMiscTax for the service
   Description: Calls UpdateExt to update POHeaderMiscTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POHeaderMiscTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.POHeaderMiscTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderMiscTaxes(" + Company + "," + PONum + "," + SeqNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_POHeaderMiscTaxes_Company_PONum_SeqNum_TaxCode_RateCode_ECAcquisitionSeq(Company, PONum, SeqNum, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete POHeaderMiscTax item
   Description: Call UpdateExt to delete POHeaderMiscTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POHeaderMiscTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderMiscTaxes(" + Company + "," + PONum + "," + SeqNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_POHeaderTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get POHeaderTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POHeaderTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeaderTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderTaxes",headers=creds) as resp:
           return await resp.json()

async def post_POHeaderTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POHeaderTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POHeaderTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.POHeaderTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_POHeaderTaxes_Company_PONum_TaxCode_RateCode_ECAcquisitionSeq(Company, PONum, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the POHeaderTax item
   Description: Calls GetByID to retrieve the POHeaderTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POHeaderTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeaderTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderTaxes(" + Company + "," + PONum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_POHeaderTaxes_Company_PONum_TaxCode_RateCode_ECAcquisitionSeq(Company, PONum, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update POHeaderTax for the service
   Description: Calls UpdateExt to update POHeaderTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POHeaderTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.POHeaderTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderTaxes(" + Company + "," + PONum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_POHeaderTaxes_Company_PONum_TaxCode_RateCode_ECAcquisitionSeq(Company, PONum, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete POHeaderTax item
   Description: Call UpdateExt to delete POHeaderTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POHeaderTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderTaxes(" + Company + "," + PONum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_POHeaderAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get POHeaderAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POHeaderAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeaderAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderAttches",headers=creds) as resp:
           return await resp.json()

async def post_POHeaderAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POHeaderAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POHeaderAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.POHeaderAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_POHeaderAttches_Company_PONum_DrawingSeq(Company, PONum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the POHeaderAttch item
   Description: Calls GetByID to retrieve the POHeaderAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POHeaderAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeaderAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderAttches(" + Company + "," + PONum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_POHeaderAttches_Company_PONum_DrawingSeq(Company, PONum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update POHeaderAttch for the service
   Description: Calls UpdateExt to update POHeaderAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POHeaderAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.POHeaderAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderAttches(" + Company + "," + PONum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_POHeaderAttches_Company_PONum_DrawingSeq(Company, PONum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete POHeaderAttch item
   Description: Call UpdateExt to delete POHeaderAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POHeaderAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderAttches(" + Company + "," + PONum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeaderListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePOHeader, whereClausePOHeaderAttch, whereClausePODetail, whereClausePODetailAttch, whereClausePORel, whereClausePORelAttch, whereClausePORelTax, whereClausePORelTGLC, whereClausePODetailInsp, whereClausePODetailTax, whereClausePOMisc, whereClausePODetailMiscTax, whereClausePOHeadMisc, whereClausePOHeaderMiscTax, whereClausePOHeaderTax, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePOHeader=" + whereClausePOHeader
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePOHeaderAttch=" + whereClausePOHeaderAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePODetail=" + whereClausePODetail
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePODetailAttch=" + whereClausePODetailAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePORel=" + whereClausePORel
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePORelAttch=" + whereClausePORelAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePORelTax=" + whereClausePORelTax
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePORelTGLC=" + whereClausePORelTGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePODetailInsp=" + whereClausePODetailInsp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePODetailTax=" + whereClausePODetailTax
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePOMisc=" + whereClausePOMisc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePODetailMiscTax=" + whereClausePODetailMiscTax
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePOHeadMisc=" + whereClausePOHeadMisc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePOHeaderMiscTax=" + whereClausePOHeaderMiscTax
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePOHeaderTax=" + whereClausePOHeaderTax
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(poNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "poNum=" + poNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaxFixedAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaxFixedAmount
   Description: Method to call when changing the fixed amount on the PORelTax table currently
   OperationID: ChangeTaxFixedAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxFixedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxFixedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaxReportableAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaxReportableAmt
   Description: Method to call when changing the reportable amount on either POHeaderMiscTax / PODetailMiscTax or PORelTax
reportable amounts based on the new reportable amount.
   OperationID: ChangeTaxReportableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxReportableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxReportableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaxTaxableAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaxTaxableAmt
   Description: Method to call when changing the taxable amount on either POHeaderMiscTax / PODetailMiscTax or PORelTax
taxable amounts based on the new taxable amount.
   OperationID: ChangeTaxTaxableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaxTaxAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaxTaxAmt
   Description: Method to call when changing the tax amount on a either a POHeaderMiscTax / PODetailMiscTax or a PORelTax row
tax amounts based on the new tax amount.
   OperationID: ChangeTaxTaxAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaxDeductable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaxDeductable
   Description: Method to call when changing the tax deductable on a Release line tax record.
   OperationID: ChangeTaxDeductable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxDeductable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxDeductable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaxTaxCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaxTaxCode
   Description: Method to call when changing the tax code on a the POHeaderMiscTax, PODetailMiscTax or PORelTax.  Validates the tax code and
updates PORelTax tax amounts based on the new tax code.
   OperationID: ChangeTaxTaxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaxRateCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaxRateCode
   Description: Method to call when changing the rate code on a tax record related to Release Tax Line.  Validates the rate and tax code
   OperationID: ChangeTaxRateCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaxPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaxPercent
   Description: Method to call when changing the tax percent on a tax release line record.  Updates PORelTax
tax amounts based on the new tax percent only when one tax record exists.
   OperationID: ChangeTaxPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeExpAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeExpAcct
   Description: This method sets the flag in PORelTGLC that indicates if the account
has been overridden from the default.
   OperationID: ChangeExpAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeExpAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeExpAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateAcctForGLControl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateAcctForGLControl
   Description: Validates an account has been entered for glcontrol of a PUR-UKN PORel record
   OperationID: ValidateAcctForGLControl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateAcctForGLControl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAcctForGLControl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateInspection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateInspection
   Description: Method to validate the Inspection control fields. (EQM)
   OperationID: ValidateInspection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateInspection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateInspection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidataPartToLinkToContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidataPartToLinkToContract
   Description: Validate Parts allowed for Planning Contracts.
   OperationID: ValidataPartToLinkToContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidataPartToLinkToContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidataPartToLinkToContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePOLinesTaxCategoryTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePOLinesTaxCategoryTypes
   Description: Method to validate that all Purchase Order lines have Tax Categories with the same Tax Category Type
   OperationID: ValidatePOLinesTaxCategoryTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePOLinesTaxCategoryTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePOLinesTaxCategoryTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPOHeader(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPOHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPOHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPOHeaderAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPOHeaderAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOHeaderAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPOHeaderAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOHeaderAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPODetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPODetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPODetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPODetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPODetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPODetailAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPODetailAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPODetailAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPODetailAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPODetailAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPORel(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPORel
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPORel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPORel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPORel_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPORelAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPORelAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPORelAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPORelAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPORelAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPORelTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPORelTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPORelTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPORelTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPORelTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPORelTGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPORelTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPORelTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPORelTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPORelTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPODetailInsp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPODetailInsp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPODetailInsp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPODetailInsp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPODetailInsp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPODetailTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPODetailTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPODetailTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPODetailTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPODetailTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPOMisc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPOMisc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOMisc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPOMisc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOMisc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPODetailMiscTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPODetailMiscTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPODetailMiscTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPODetailMiscTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPODetailMiscTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPOHeadMisc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPOHeadMisc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOHeadMisc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPOHeadMisc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOHeadMisc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPOHeaderMiscTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPOHeaderMiscTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOHeaderMiscTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPOHeaderMiscTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOHeaderMiscTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPOHeaderTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPOHeaderTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOHeaderTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPOHeaderTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOHeaderTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckForMRPAttributes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckForMRPAttributes
   Description: Check for potential warnings / confirmations before performing the PO update
   OperationID: CheckForMRPAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForMRPAttributes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForMRPAttributes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalcAutoPORelTGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalcAutoPORelTGLC
   Description: Auto Calculate PORelTGLC
   OperationID: CalcAutoPORelTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcAutoPORelTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcAutoPORelTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBeforeUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBeforeUpdate
   Description: Check for potential warnings / confirmations before performing the PO update
   OperationID: CheckBeforeUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckLOCWithMessages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckLOCWithMessages
   Description: Provides a way to call CheckLOC from MetaUI.
Checks outstanding amounts to limit on APLOC (if applicable)
This should be called before updating POHeader, PODetail,PORel, POMisc, or POHeadMisc
If limit is exceeded a string is returned asking the user if they want to override.
If Releases have distinct Due Date and LOC is marked as "Ship Complete", a string is returned asking the user if they want to continue.
   OperationID: CheckLOCWithMessages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckLOCWithMessages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckLOCWithMessages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckLOC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckLOC
   Description: Checks outstanding amounts to limit on APLOC (if applicable)
This should be called before updating POHeader, PODetail,PORel, POMisc, or POHeadMisc
If limit is exceeded a string is returned asking the user if they want to override.
If Releases have distinct Due Date and LOC is marked as "Ship Complete", a string is returned asking the user if they want to continue.
Not able to be used with MetaUI because of the output param array.
   OperationID: CheckLOC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckLOC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckLOC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPODetailCNBonded(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPODetailCNBonded
   Description: Purpose:  Check Bonded on line
Parameters:
<param name="sMessage">Warning</param><param name="ds"></param>
   OperationID: CheckPODetailCNBonded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPODetailCNBonded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPODetailCNBonded_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPONum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPONum
   Description: Method to call when entering proposed PO Number.  This method will return
two output variables.  One is a logical field to indicate if the PO number
entered is existing or not.  The other variable is for the error message
in case the proposed PO number is invalid.
Removed Return from the end of this procedure
   OperationID: CheckPONum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_chkPODatesChanges(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method chkPODatesChanges
   Description: SCR 142197 - New logic to let the user know which date fields chenged
Checks to see if certain fields changed on the order header or order line.  If they did,
a question is presented to the user asking if these changes should carry over
to the order lines and/or order releases.  This method returns the text of the message
to ask.  When adding a header it is not necessary to call this method because there
won't be any lines or releases to propogate the changes to.  The user can answer yes
or no, but processing doesn't stop based on the answer.  The answer should be stored
in the dataset in field OrderHed.UpdateDtlAndRelRecords.
   OperationID: chkPODatesChanges
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/chkPODatesChanges_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/chkPODatesChanges_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseOrder
   Description: Filters up available open orders/lines
   OperationID: CloseOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseOrderLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseOrderLine
   Description: Filters up available open lines
   OperationID: CloseOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseRelease(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseRelease
   Description: Run this method to close a release .
   OperationID: CloseRelease
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseRelease_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseRelease_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreDuplicatePO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreDuplicatePO
   Description: Checks attributes before duplicating a PO
   OperationID: PreDuplicatePO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreDuplicatePO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreDuplicatePO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DuplicatePO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicatePO
   Description: Duplicates PO
   OperationID: DuplicatePO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicatePO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicatePO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAPLOCDescription(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAPLOCDescription
   Description: This method should be invoked when it is required to set the APLOC Description changes.
   OperationID: GetAPLOCDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAPLOCDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPLOCDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Get Code Description List
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrencyBase(epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrencyBase
   Description: This method returns the Base CurrencyCode
   OperationID: GetCurrencyBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultBuyer(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultBuyer
   Description: Returns default buyer information for the current user.
   OperationID: GetDefaultBuyer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultBuyer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultGLAccountAllPOReleases(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultGLAccountAllPOReleases
   Description: Get Default GL Account for All the Releases.
<param name="pPONum">PO Number</param><param name="ds" type="Epicor.Mfg.BO.PODataSet">The Purchase Order data set </param>
   OperationID: GetDefaultGLAccountAllPOReleases
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultGLAccountAllPOReleases_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultGLAccountAllPOReleases_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDropShipPOHeaderList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDropShipPOHeaderList
   Description: Perform a GetList but only return POs that exist on a DropShipDtl
   OperationID: GetDropShipPOHeaderList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDropShipPOHeaderList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDropShipPOHeaderList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewConsolidatedPO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewConsolidatedPO
   Description: Method to call when adding a Consolidated PO
   OperationID: GetNewConsolidatedPO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsolidatedPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsolidatedPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewContractPO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContractPO
   Description: Method to call when adding a Consolidated PO
   OperationID: GetNewContractPO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContractPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContractPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGlbCompanyList(epicorHeaders = None):
   """  
   Summary: Invoke method GetGlbCompanyList
   Description: Returns a list of available companies to choose from for the
Global Company field.  Returns the list in code1`desc1~code2`desc2 format.
   OperationID: GetGlbCompanyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGlbCompanyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetPartSubList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartSubList
   Description: Public method to get the poapvmsg dataset.
   OperationID: GetPartSubList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartSubList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartSubList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPOReceipts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPOReceipts
   Description: Gets RcvDtl's and DropShipDtl's for a given PONum.
   OperationID: GetPOReceipts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPOReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPORelationshipMap(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPORelationshipMap
   Description: Returns a serialized json string to show a Relationship Map for PO
   OperationID: GetPORelationshipMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPORelationshipMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPORelationshipMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForAPInvoice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForAPInvoice
   Description: Invokes GetRows filtering on PO's for the specified Invoice
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForPayment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForPayment
   Description: Invokes GetRows filtering on PO's for the specified Payment
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForReceipt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForReceipt
   Description: Invokes GetRows filtering on PO's for the specified Pack slip
   OperationID: GetRowsForReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetShipToAddressForCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetShipToAddressForCompany
   Description: Gets the ShipTo Address for the current company
   OperationID: GetShipToAddressForCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipToAddressForCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipToAddressForCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetShipToAddressForCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetShipToAddressForCustomer
   Description: Gets the ShipTo Address for a customer
   OperationID: GetShipToAddressForCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipToAddressForCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipToAddressForCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetShipToAddressForSite(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetShipToAddressForSite
   Description: Gets the ShipTo Address for a Site
   OperationID: GetShipToAddressForSite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipToAddressForSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipToAddressForSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetShipToAddressForSupplier(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetShipToAddressForSupplier
   Description: Gets the ShipTo Address for a Supplier
   OperationID: GetShipToAddressForSupplier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipToAddressForSupplier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipToAddressForSupplier_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReopenOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReopenOrder
   Description: Reopens order
   OperationID: ReopenOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReopenOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReopenOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReopenOrderLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReopenOrderLine
   Description: Reopens order line
   OperationID: ReopenOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReopenOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReopenOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VerifyReopenRelease(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VerifyReopenRelease
   Description: Precheck before reopening an order release.
   OperationID: VerifyReopenRelease
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifyReopenRelease_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyReopenRelease_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReOpenRelease(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReOpenRelease
   Description: Run this method to reopen a release.
   OperationID: ReOpenRelease
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReOpenRelease_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReOpenRelease_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetReadyToCalc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetReadyToCalc
   Description: CALCULATE VANTAGE\TAX CONNECT TAX CALCULATIONS UI NEEDS TO CALL A SAVE BEFORE CALLING THIS PROCEDURE
<param name="poNum">poNum </param><param name="calledFromUI">calledFromUI</param><param name="ds">APInvoice dataset</param>
   OperationID: SetReadyToCalc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetReadyToCalc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetReadyToCalc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeContractUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeContractUOM
   Description: Call this method when the PODetail.ContractQtyUOM changes.
   OperationID: ChangeContractUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeContractUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeContractUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailAssemblySeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailAssemblySeq
   Description: Invoke when assembly on the detail sheet changes. It will validate the release and
zero out the JobSeq.
   OperationID: ChangeDetailAssemblySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailCalcOurQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailCalcOurQty
   Description: Run this method when our quantity on the detail changes.
   OperationID: ChangeDetailCalcOurQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailCalcOurQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailCalcOurQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailCostPerCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailCostPerCode
   Description: Run this method when the Cost Per factor on the detail changes.
   OperationID: ChangeDetailCostPerCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailCostPerCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailCostPerCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailCalcVendQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailCalcVendQty
   Description: Run this method when supplier quantity on the detail changes.
   OperationID: ChangeDetailCalcVendQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailCalcVendQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailCalcVendQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailCommodityCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailCommodityCode
   Description: Validate entered Commodity Code
   OperationID: ChangeDetailCommodityCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailCommodityCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailCommodityCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailIUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailIUM
   Description: Call this method when the IUM changes on the PODetail.
   OperationID: ChangeDetailIUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailIUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailIUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailJobNum
   Description: This method is used when the jobnumber on the detail screen changes .
   OperationID: ChangeDetailJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailJobSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailJobSeq
   Description: Invoke when Job/mtl sequence on the Detail sheet changes. I
   OperationID: ChangeDetailJobSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailJobSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailJobSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailMangCust(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailMangCust
   Description: Run this method when MangCustID on the detail changes.
   OperationID: ChangeDetailMangCust
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailMangCust_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailMangCust_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailMfgNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailMfgNum
   Description: Call this method when the MfgNum changes on the PODetail.
   OperationID: ChangeDetailMfgNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailMfgNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailMfgNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailMfgPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailMfgPartNum
   Description: Call this method when the MfgPartNum changes on the PODetail.
   OperationID: ChangeDetailMfgPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailMfgPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailMfgPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailOrderLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailOrderLine
   Description: Call this method when the OrderLine changes on the PODetail.
   OperationID: ChangeDetailOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailOrderNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailOrderNum
   Description: Call this method when the OrderNum changes on the PODetail.
   OperationID: ChangeDetailOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailOverridePriceList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailOverridePriceList
   Description: Run this method when the override pricelist is unchecked
   OperationID: ChangeDetailOverridePriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailOverridePriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailOverridePriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailPartClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailPartClass
   Description: Run this method when the Class ID on the detail screen changes .
   OperationID: ChangeDetailPartClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailPartClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailPartClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailPartNum
   Description: Run this method when the partnumber on the detail screen changes .
   OperationID: ChangeDetailPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailContractID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailContractID
   Description: Run this method when the Contract ID on the detail screen changes
   OperationID: ChangeDetailContractID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailContractID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailContractID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailPUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailPUM
   Description: Call this method when the PUM changes on the PODetail.
   OperationID: ChangeDetailPUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailPUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailPUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailRevisionNum
   Description: Change PO Detail Revision Number
   OperationID: ChangeDetailRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUOMConfirm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUOMConfirm
   Description: Confirm is attributes exit before changing UOM
   OperationID: ChangeUOMConfirm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUOMConfirm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUOMConfirm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailTaxCatID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailTaxCatID
   Description: Call this method when changing the Tax Category
   OperationID: ChangeDetailTaxCatID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailTaxCatID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailTaxCatID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailTranType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailTranType
   Description: Call this method when the TranType (LineType) changes on the PODetail.
It will update the price on the release
   OperationID: ChangeDetailTranType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailTranType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailTranType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangingDetailRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangingDetailRevisionNum
   Description: Change PO Detail Revision Number
   OperationID: ChangingDetailRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangingDetailRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangingDetailRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailVenPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailVenPartNum
   Description: Call this method when the VenPartNum changes on the PODetail.
   OperationID: ChangeDetailVenPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailVenPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailVenPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUnitPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUnitPrice
   Description: Calculates the UnitPrice or DocUnitPrice depending of the Currency Switch.
   OperationID: ChangeUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUnitPriceConfirmOverride(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUnitPriceConfirmOverride
   Description: Checks if the source of the unit price is from a supplier price list, if so
will prompt for confirmation of overriding if flag is set against purchase configuration.
   OperationID: ChangeUnitPriceConfirmOverride
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUnitPriceConfirmOverride_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUnitPriceConfirmOverride_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQtyOption(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQtyOption
   Description: This method is used when the QtyOption on the detail screen changes.
   OperationID: ChangeQtyOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQtyOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQtyOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBasePartAndConfigType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBasePartAndConfigType
   Description: Retrieve the based configured part and config type
   OperationID: GetBasePartAndConfigType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBasePartAndConfigType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBasePartAndConfigType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBasePartForConfig(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBasePartForConfig
   Description: This method will retrieve the base configured part number to be passed
to configuration entry
   OperationID: GetBasePartForConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBasePartForConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBasePartForConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPlantsForPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPlantsForPart
   Description: Gets Plant for appropriate Part
   OperationID: GetPlantsForPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPlantsForPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPlantsForPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PartStatusValidationMessages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartStatusValidationMessages
   Description: The method is to be run on leave of the PartNum, Revision fields before the
GetPartInfo or Update methods are run.  This returns all the questions that
need to be asked before a part can be changed.
   OperationID: PartStatusValidationMessages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartStatusValidationMessages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartStatusValidationMessages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetValidManufacturers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetValidManufacturers
   Description: Return the valid Manufacturers set to a specific part.
   OperationID: GetValidManufacturers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetValidManufacturers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetValidManufacturers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeApproveSwitch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeApproveSwitch
   Description: Invoke this method when the Approve switch on the summary screen changes.
   OperationID: ChangeApproveSwitch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeApproveSwitch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeApproveSwitch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedApproveSwitch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedApproveSwitch
   Description: Invoke this method when the Approve switch has changed to True and we need to invoke the 'Approval' logic and the Supplier minimum value tests.
   OperationID: ChangedApproveSwitch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedApproveSwitch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedApproveSwitch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeConfirmSwitch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeConfirmSwitch
   Description: Invoke this method when the Confirm switch on the summary screen changes.
   OperationID: ChangeConfirmSwitch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeConfirmSwitch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConfirmSwitch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCountry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCountry
   Description: Changes country
   OperationID: ChangeCountry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCurrencyCode
   Description: Run this method when the currency code changes on the poheader.
This method will pull in the exchange rate.
   OperationID: ChangeCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePOTaxRegionCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePOTaxRegionCode
   Description: Change Tax Region Code
   OperationID: ChangePOTaxRegionCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOTaxRegionCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOTaxRegionCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePOType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePOType
   Description: This method should be invoked when the newPOType changes.
   OperationID: ChangePOType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePrcConNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePrcConNum
   Description: This method should be invoked when the PrcConNum changes. This method will validate
the vendorCnt and pull in the new default information.
   OperationID: ChangePrcConNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePrcConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePrcConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePrcConNumByName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePrcConNumByName
   Description: This method should be invoked when the PrcConNum changes.This method will validate
the vendorCnt and pull in the new default information based on the contact's name.
   OperationID: ChangePrcConNumByName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePrcConNumByName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePrcConNumByName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePrcConNumByNameOrNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePrcConNumByNameOrNum
   Description: This method should be invoked when the PrcConNum changes.This method will validate
the vendorCnt and pull in the new default information based on the contact's num or name.
   OperationID: ChangePrcConNumByNameOrNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePrcConNumByNameOrNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePrcConNumByNameOrNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePurPoint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePurPoint
   Description: Invoke this method to change the purchase point on the POHeader. This method
will validate the PP and pull in default information.
   OperationID: ChangePurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendor
   Description: This method should be invoked when the vendor ID changes. This method will validate
the vendor and pull in the new default vendor information.
1. Validate Vendor ID / Vendor Num
2. check for inactive vendor
3. check Vendor for Approved flag
4. check item(s) for conficts with AprvVend
   OperationID: ChangeVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRateGrpCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRateGrpCode
   Description: Update Quote Detail information when the Part Number is changed.
   OperationID: CheckRateGrpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRateGrpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRateGrpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedHeaderTaxManual(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedHeaderTaxManual
   Description: Method to call when the Manual Tax Flag has Changed from True to False.  Updates POHeaderTax
tax amounts based on the new tax percent.
   OperationID: ChangedHeaderTaxManual
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedHeaderTaxManual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedHeaderTaxManual_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHeaderTaxFixedAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHeaderTaxFixedAmount
   Description: Method to call when changing the fixed amount on a tax record.  Updates POHeaderTax
tax amounts based on the new fixed amount.
   OperationID: ChangeHeaderTaxFixedAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxFixedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxFixedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHeaderTaxTaxPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHeaderTaxTaxPercent
   Description: Method to call when changing the tax percent on a tax record.  Updates POHeaderTax
tax amounts based on the new tax percent.
   OperationID: ChangeHeaderTaxTaxPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHeaderTaxRateCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHeaderTaxRateCode
   Description: Method to call when changing the tax percent on a tax record.  Updates POHeaderTax
tax amounts based on the new tax percent.
   OperationID: ChangeHeaderTaxRateCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHeaderTaxRateCodeMaster(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHeaderTaxRateCodeMaster
   Description: Method to call when changing the rate code on a tax record.  Validates the rate and tax code
   OperationID: ChangeHeaderTaxRateCodeMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxRateCodeMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxRateCodeMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHeaderTaxReportableAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHeaderTaxReportableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates POHeaderTax
tax amounts based on the new taxable amount.
   OperationID: ChangeHeaderTaxReportableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxReportableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxReportableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHeaderTaxTaxableAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHeaderTaxTaxableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates POHeaderTax
tax amounts based on the new taxable amount.
   OperationID: ChangeHeaderTaxTaxableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHeaderTaxTaxAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHeaderTaxTaxAmt
   Description: Method to call when changing the fixed tax amount on a tax record.  Updates POHeaderTax
tax amounts based on the new tax amount.
   OperationID: ChangeHeaderTaxTaxAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHeaderTaxTaxCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHeaderTaxTaxCode
   Description: Method to call when changing the tax code on a POHeader Tax record.  Validates the tax code and
updates POHeaderTax tax amounts based on the new tax code.
   OperationID: ChangeHeaderTaxTaxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHeaderTaxTaxDeductable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHeaderTaxTaxDeductable
   Description: Method to call when changing the tax deductable on a tax record.  Updates POHeaderTax
tax amounts based on the new tax percent.
   OperationID: ChangeHeaderTaxTaxDeductable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxTaxDeductable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxTaxDeductable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCurrencySwitch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCurrencySwitch
   Description: Run this method when the currency toggle changes on the POHeadeMisc.
It will update the currency symbol.
   OperationID: ChangeCurrencySwitch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurrencySwitch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencySwitch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePOHeadMiscAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePOHeadMiscAmt
   Description: Method to call when changing the miscellanous amount on a miscellaneous charge.
Updates the respective miscellanous charge table with default values based on the new amount.
   OperationID: ChangePOHeadMiscAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOHeadMiscAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOHeadMiscAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePOHeadMiscCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePOHeadMiscCode
   Description: Run this method when the misc code is changed on the POHeadMisc.
It will recalaculate amounts.
   OperationID: ChangePOHeadMiscCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOHeadMiscCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOHeadMiscCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePOHeadMiscPrcnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePOHeadMiscPrcnt
   Description: Run this method when the percentage changes on the POHeadMisc.
It will recalaculate doc and base amounts.
   OperationID: ChangePOHeadMiscPrcnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOHeadMiscPrcnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOHeadMiscPrcnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePOMiscAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePOMiscAmt
   Description: Method to call when changing the miscellanous amount on a miscellaneous charge.
Updates the respective miscellanous charge table with default values based on the new amount.
   OperationID: ChangePOMiscAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOMiscAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOMiscAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePOMiscCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePOMiscCode
   Description: Run this method when the misc code is changed on the POMisc.
It will recalaculate amounts.
   OperationID: ChangePOMiscCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOMiscCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOMiscCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePoMiscCurrSwitch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePoMiscCurrSwitch
   Description: Run this method when the currency toggle changes on the POMisc.
It will update the currency symbol and recalaculate doc and base amounts.
   OperationID: ChangePoMiscCurrSwitch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePoMiscCurrSwitch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePoMiscCurrSwitch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePOMiscPrcnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePOMiscPrcnt
   Description: Run this method when the percentage changes on the POMisc.
It will recalaculate doc and base amounts.
   OperationID: ChangePOMiscPrcnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOMiscPrcnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOMiscPrcnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelAssemblySeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelAssemblySeq
   Description: Invoke when assembly on the release sheet changes. It will validate the release and
zero out the JobSeq.
   OperationID: ChangeRelAssemblySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelGlbCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelGlbCompany
   Description: This method should be called when the GlbCompany field on a po release changes.
It will populate default values in PORel based on the new GlbCompany value.
   OperationID: ChangeRelGlbCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelGlbCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelGlbCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelGlbPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelGlbPlant
   Description: This method should be called when the GlbPlant field on a po release changes.
It will populate default values in PORel based on the new GlbPlant value.
   OperationID: ChangeRelGlbPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelGlbPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelGlbPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelGlbWarehouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelGlbWarehouse
   Description: This method should be called when the GlbWarehouse field on a po release changes.
It will populate default values in PORel based on the new GlbWarehouse value.
   OperationID: ChangeRelGlbWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelGlbWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelGlbWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelIUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelIUM
   Description: Call this method when the IUM changes on the PORel.
   OperationID: ChangeRelIUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelIUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelIUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelJobNum
   Description: /// Purpose: Invoke after the jobnumber has changed either on the release sheet .
///
   OperationID: ChangeRelJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelJobSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelJobSeq
   Description: Invoke when Job/mtl sequence on the release sheet changes. It will validate the release and
zero out the JobSeq.
   OperationID: ChangeRelJobSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelJobSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelJobSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelJobSeqWarning(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelJobSeqWarning
   Description: Gets specified material or operation record and changes the warning message.
   OperationID: ChangeRelJobSeqWarning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelJobSeqWarning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelJobSeqWarning_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBTOOrderLineWarning(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBTOOrderLineWarning
   Description: Check Order detail is valid and issue a error / warning accordingly.
   OperationID: ChangeBTOOrderLineWarning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBTOOrderLineWarning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBTOOrderLineWarning_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelMangCust(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelMangCust
   Description: Run this method when MangCustID on the release changes.
   OperationID: ChangeRelMangCust
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelMangCust_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelMangCust_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelOrderLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelOrderLine
   Description: Call this method when the OrderLine changes on the PORel.
   OperationID: ChangeRelOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelOrderNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelOrderNum
   Description: Call this method when the OrderNum changes on the PORel.
   OperationID: ChangeRelOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelOrderRelNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelOrderRelNum
   Description: Call this method when the OrderRelNum changes on the PORel.
   OperationID: ChangeRelOrderRelNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelOrderRelNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelOrderRelNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelOurQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelOurQty
   Description: This should be run after OurQty (PORel.XRelQty) changed on the PO release.
   OperationID: ChangeRelOurQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelOurQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelOurQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelPlant
   Description: Call this method when the Plant is changed on PORel.
   OperationID: ChangeRelPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelPUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelPUM
   Description: Call this method when the PUM changes on the PORel.
   OperationID: ChangeRelPUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelPUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelPUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelTaxExempt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelTaxExempt
   Description: Call this method when changing the Tax Exempt to toggle Taxable Flag
   OperationID: ChangeRelTaxExempt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelTaxExempt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelTaxExempt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelVendQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelVendQty
   Description: This should be run after VendorQty (PORel.RelQty) changed on the PO release.
   OperationID: ChangeRelVendQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelVendQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelVendQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePORelContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePORelContract
   Description: Call this method when the PORel.ContractID changes.
   OperationID: ChangePORelContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePORelContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePORelContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTranType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTranType
   Description: Call this method when the TranType (LineType) changes on the POREL.
ExpAccount will change
   OperationID: ChangeTranType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTranType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckComplianceFail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckComplianceFail
   Description: Check for every release of the PO if it is compliant.
   OperationID: CheckComplianceFail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckComplianceFail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckComplianceFail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckProjectID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckProjectID
   Description: Validate Projec ID value
   OperationID: CheckProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultGLAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultGLAccount
   Description: Get Default GL Account.
<param name="pPONum">PO Number</param><param name="pPOLine">PO Line number</param><param name="pPORelNum">PO Release number</param><param name="ds" type="Epicor.Mfg.BO.PODataSet">The Purchase Order data set </param>
   OperationID: GetDefaultGLAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultGLAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultGLAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedTaxManual(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedTaxManual
   Description: Method to call when changing the manual tax calculation value on a line tax record.  Updates PORelTax
tax amounts based on the new value of the flag back to system-calculated tax.
   OperationID: ChangedTaxManual
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedTaxManual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedTaxManual_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PODetailAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailInspRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PODetailInspRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailMiscTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PODetailMiscTaxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PODetailRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PODetailTaxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeadMiscRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_POHeadMiscRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_POHeaderAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_POHeaderListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderMiscTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_POHeaderMiscTaxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_POHeaderRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_POHeaderTaxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POMiscRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_POMiscRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PORelAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PORelRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelTGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PORelTGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PORelTaxRow] = obj["value"]
      pass

class Erp_Tablesets_PODetailAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PONUM:int = obj["PONUM"]
      self.POLine:int = obj["POLine"]
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

class Erp_Tablesets_PODetailInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PONUM:int = obj["PONUM"]
      """  Purchase order number that the detail line item is linked to.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.PlanSeq:int = obj["PlanSeq"]
      """  A sequence number that uniquely identifies the PartMtlInsp record within the Part material  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID.  Must be valid in the SpecHed table.  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PODetailMiscTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PONUM:int = obj["PONUM"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  ** NOT USED TO BE DROPPED 10.2 **  """  
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
      """  User ID of the user who created the record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date/ time that the record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date/ time that the record was last changed  """  
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
      self.Migrated:bool = obj["Migrated"]
      """  Indicates if this row was created as part of the migration process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Desc. Collection Type  """  
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
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PODetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if this line item is Open/Closed. This is not directly maintainable by the user. Normally it gets set to "Closed" as a result of the receiving process. When there are no longer any open PORel records then the PODetail record is closed. This can also be closed when the user Voids the Order or PODetail record.  """  
      self.VoidLine:bool = obj["VoidLine"]
      """   Indicates if the Line was voided. Voided line items are not maintainable, can't "unvoid".  This field is not directly maintainable.  Instead the void function will be performed via a "Void Line" button.  Which then presents a verification dialog box.
When an PODetail record is 'voided',  all current open  PORel records are also closed and voided.  If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoHeader is voided.  """  
      self.PONUM:int = obj["PONUM"]
      """  Purchase order number that the detail line item is linked to.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  (Our) Unit Of Measure.  """  
      self.UnitCost:int = obj["UnitCost"]
      """   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  The unit price in the vendors unit of measure and currency.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little misleading.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the OrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This insures that Order quantity and scheduled  quantities are always in sync.  """  
      self.XOrderQty:int = obj["XOrderQty"]
      """  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  This ensures that Order quantity and scheduled quantities are always in sync.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Taxable  """  
      self.PUM:str = obj["PUM"]
      """  Purchasing UOM  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal Part number for this item.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier Part Number  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail order line item. These will be printed on the purchase order.  Defaults from the related JobOper, JobMtl or Part file.  """  
      self.ClassID:str = obj["ClassID"]
      """  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.ClassID. The PartClass is used in determining a default G/L expense account.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required when this PO line item is received. Inspection may also be enforced if the related PartClass, Vendor, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is a duplicate of the field in POHeader and is maintained  in the write triggers of POHeader and PODetail.  """  
      self.AdvancePayBal:int = obj["AdvancePayBal"]
      """  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  """  
      self.DocAdvancePayBal:int = obj["DocAdvancePayBal"]
      """  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  """  
      self.Confirmed:bool = obj["Confirmed"]
      """  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  """  
      self.DateChgReq:bool = obj["DateChgReq"]
      """  Indicates this line has a pending date change  """  
      self.QtyChgReq:bool = obj["QtyChgReq"]
      """  Indicates this line has a pending qty change  """  
      self.PartNumChgReq:str = obj["PartNumChgReq"]
      """  Requested pending partnumber change  """  
      self.RevisionNumChgReq:str = obj["RevisionNumChgReq"]
      """  Requested pending revision change  """  
      self.ConfirmDate:str = obj["ConfirmDate"]
      """  Date Supplier Confirmed the PO  """  
      self.ConfirmVia:str = obj["ConfirmVia"]
      """  Can be "web" or "client"  """  
      self.PrcChgReq:int = obj["PrcChgReq"]
      """  Requested Price change.  SRM  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line created for this PO Line for the Inter-Company Trading.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order line.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.ContractActive:bool = obj["ContractActive"]
      """  Is this line active on the Contract Purchase Order?  """  
      self.ContractQty:int = obj["ContractQty"]
      """  Quantity for this Contract Purchase Order Line.  """  
      self.ContractUnitCost:int = obj["ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line.  """  
      self.ContractDocUnitCost:int = obj["ContractDocUnitCost"]
      """  Document Unit Price for this Contract Purchase Order Line.  """  
      self.Rpt1AdvancePayBal:int = obj["Rpt1AdvancePayBal"]
      """  Advanced Payments Balance in Rpt1 currency.  """  
      self.Rpt2AdvancePayBal:int = obj["Rpt2AdvancePayBal"]
      """  Advanced Payments Balance in Rpt2 currency.  """  
      self.Rpt3AdvancePayBal:int = obj["Rpt3AdvancePayBal"]
      """  Advanced Payments Balance in Rpt3 currency.  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt1 currency.  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt2 currency.  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt3 currency.  """  
      self.ContractQtyUOM:str = obj["ContractQtyUOM"]
      """  Unit Of Measure of the ContractQty.  """  
      self.Rpt1ContractUnitCost:int = obj["Rpt1ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt1 currency.  """  
      self.Rpt2ContractUnitCost:int = obj["Rpt2ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt2 currency.  """  
      self.Rpt3ContractUnitCost:int = obj["Rpt3ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt3 currency.  """  
      self.BaseQty:int = obj["BaseQty"]
      """  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PODeltail.XOrderQty to the PODetail.BaseUOM .  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """   Unit of Measure of the PODetail.BaseXOrderQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  """  
      self.BTOOrderNum:int = obj["BTOOrderNum"]
      """  Order Num related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderLine:int = obj["BTOOrderLine"]
      """  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  """  
      self.VendorPartOpts:str = obj["VendorPartOpts"]
      """   Vendor Part Print Options. Determines what is printed.
M = Main Part Reference (Default)
S = Secondary Part Reference
O = Only Part Reference
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  """  
      self.MfgPartOpts:str = obj["MfgPartOpts"]
      """   Mfg Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  """  
      self.SubPartOpts:str = obj["SubPartOpts"]
      """   Substitute Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
M = Main Part Reference
S = Secondary Part Reference  """  
      self.MfgNum:int = obj["MfgNum"]
      """  Manufacturer Unique ID  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  Manufacturer's Part Number.  """  
      self.SubPartNum:str = obj["SubPartNum"]
      """  Substitute Part Number  """  
      self.SubPartType:str = obj["SubPartType"]
      """   Substitute Part Type
O = Original
S = Substitute  """  
      self.ConfigUnitCost:int = obj["ConfigUnitCost"]
      """   Same as Unit cost except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitCost:int = obj["ConfigBaseUnitCost"]
      """  This is the base cost for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.ConvOverRide:bool = obj["ConvOverRide"]
      """  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.Direction:str = obj["Direction"]
      """  Direction  """  
      self.Per:str = obj["Per"]
      """  Per  """  
      self.MaintainPricingUnits:bool = obj["MaintainPricingUnits"]
      """  MaintainPricingUnits  """  
      self.OverrideConversion:bool = obj["OverrideConversion"]
      """  OverrideConversion  """  
      self.RowsManualFactor:bool = obj["RowsManualFactor"]
      """  RowsManualFactor  """  
      self.KeepRowsManualFactorTmp:bool = obj["KeepRowsManualFactorTmp"]
      """  KeepRowsManualFactorTmp  """  
      self.ShipToSupplierDate:str = obj["ShipToSupplierDate"]
      """  ShipToSupplierDate  """  
      self.Factor:int = obj["Factor"]
      """  Factor  """  
      self.PricingQty:int = obj["PricingQty"]
      """  PricingQty  """  
      self.PricingUnitPrice:int = obj["PricingUnitPrice"]
      """  PricingUnitPrice  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.DocPricingUnitPrice:int = obj["DocPricingUnitPrice"]
      """  DocPricingUnitPrice  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the supplier price list has been overriden which will in turn prevent the unit price from being updated when taking into account quantity / price breaks.  """  
      self.QtyOption:str = obj["QtyOption"]
      """  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  """  
      self.OrigComment:str = obj["OrigComment"]
      """  Contains old comments about the detail order line item. This field saves old comments about the detail line that are going to be replaced by new comments.  """  
      self.SmartString:str = obj["SmartString"]
      """  SmartString  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  SmartStringProcessed  """  
      self.DueDate:str = obj["DueDate"]
      """  Specifies the date by which you need to receive the part. If you set the Due Date before create releases, it will act as default value when adding new releases. If you're adding lines from:  - BTO or Drop Shipments, PODetail.DueDate will take the value from OrderRel.NeedByDate. - Job Material , PODetail.DueDate  will take the value from JobMtl.ReqDate. - Subcontract Operations, PODetail.DueDate  wil take the value from JobOper.DueDate  """  
      self.ContractID:str = obj["ContractID"]
      """  The identifier of the planning contract.  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  """  
      self.SelCurrPricingUnitPrice:int = obj["SelCurrPricingUnitPrice"]
      """  SelCurrPricingUnitPrice  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date and time that the record was last changed  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this PO line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True the tax engine will not calculate any miscellaneous charge tax information  """  
      self.InUnitCost:int = obj["InUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in base currency.  """  
      self.DocInUnitCost:int = obj["DocInUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in document currency.  """  
      self.Rpt1InUnitCost:int = obj["Rpt1InUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  """  
      self.Rpt2InUnitCost:int = obj["Rpt2InUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  """  
      self.Rpt3InUnitCost:int = obj["Rpt3InUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  """  
      self.InAdvancePayBal:int = obj["InAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in base currency.  """  
      self.DocInAdvancePayBal:int = obj["DocInAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in document currency.  """  
      self.Rpt1InAdvancePayBal:int = obj["Rpt1InAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in Rpt1 currency.  """  
      self.Rpt2InAdvancePayBal:int = obj["Rpt2InAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in Rpt2 currency.  """  
      self.Rpt3InAdvancePayBal:int = obj["Rpt3InAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in Rpt3 currency.  """  
      self.InContractUnitCost:int = obj["InContractUnitCost"]
      """  Contract unit cost inclusive of tax in base currency.  """  
      self.DocInContractUnitCost:int = obj["DocInContractUnitCost"]
      """  Contract unit cost inclusive of tax in document currency.  """  
      self.Rpt1InContractUnitCost:int = obj["Rpt1InContractUnitCost"]
      """  Contract unit cost inclusive of tax in Rpt1 currency.  """  
      self.Rpt2InContractUnitCost:int = obj["Rpt2InContractUnitCost"]
      """  Contract unit cost inclusive of tax in Rpt2 currency.  """  
      self.Rpt3InContractUnitCost:int = obj["Rpt3InContractUnitCost"]
      """  Contract unit cost inclusive of tax in Rpt3 currency.  """  
      self.DocExtCost:int = obj["DocExtCost"]
      """  Extended cost of the PO Line in document currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.DocUnitCost.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended cost of the PO Line in base currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.UnitCost.  """  
      self.Rpt1ExtCost:int = obj["Rpt1ExtCost"]
      """  Extended cost of the PO Line in Rpt1 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt1UnitCost.  """  
      self.Rpt2ExtCost:int = obj["Rpt2ExtCost"]
      """  Extended cost of the PO Line in Rpt2 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt2UnitCost.  """  
      self.Rpt3ExtCost:int = obj["Rpt3ExtCost"]
      """  Extended cost of the PO Line in Rpt3 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt3UnitCost.  """  
      self.DocMiscCost:int = obj["DocMiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in document currency.  This is the sum of POMisc.DocMiscAmt for all line charges.  """  
      self.MiscCost:int = obj["MiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in base currency.  This is the sum of POMisc.MiscAmt for all line charges.  """  
      self.Rpt1MiscCost:int = obj["Rpt1MiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in Rpt1 currency.  This is the sum of POMisc.Rpt1MiscAmt for all line charges.  """  
      self.Rpt2MiscCost:int = obj["Rpt2MiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in Rpt2 currency.  This is the sum of POMisc.Rpt2MiscAmt for all line charges.  """  
      self.Rpt3MiscCost:int = obj["Rpt3MiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in Rpt3 currency.  This is the sum of POMisc.Rpt3MiscAmt for all line charges.  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Total Tax amount for this PO Line in base currency,  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """  Total Tax amount for this PO Line in document currency.  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """  Total Tax amount for this PO Line in Rpt1 currency,  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """  Total Tax amount for this PO Line in Rpt2 currency,  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """  Total Tax amount for this PO Line in Rpt3 currency,  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in base currency.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in document currency.  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  """  
      self.TotalDedTax:int = obj["TotalDedTax"]
      """  Total deductable tax amount for this PO Line in base currency.  """  
      self.DocTotalDedTax:int = obj["DocTotalDedTax"]
      """  Total deductable tax amount for this PO Line in document currency.  """  
      self.Rpt1TotalDedTax:int = obj["Rpt1TotalDedTax"]
      """  Total deductable tax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt2TotalDedTax:int = obj["Rpt2TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt3TotalDedTax:int = obj["Rpt3TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt3 currency.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  CommodityCode  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  CNBonded  """  
      self.EDIAckCode:str = obj["EDIAckCode"]
      """  Acknowledge code received from EDI  """  
      self.EDIAckComment:str = obj["EDIAckComment"]
      """  Additional comments to send with Acknowledge  """  
      self.AskRefCode:bool = obj["AskRefCode"]
      """  The flag to indicate if the user is supposed to be asked to enter a Reference code before saving a new PoDetail record .  """  
      self.CalcAssemblySeq:int = obj["CalcAssemblySeq"]
      self.CalcDocTotalCost:int = obj["CalcDocTotalCost"]
      self.CalcDueDate:str = obj["CalcDueDate"]
      self.CalcJobNum:str = obj["CalcJobNum"]
      self.CalcJobSeq:int = obj["CalcJobSeq"]
      self.CalcJobSeqType:str = obj["CalcJobSeqType"]
      self.calcLeadTime:int = obj["calcLeadTime"]
      self.CalcMangCustID:str = obj["CalcMangCustID"]
      self.CalcMangCustName:str = obj["CalcMangCustName"]
      self.CalcMangCustNum:int = obj["CalcMangCustNum"]
      self.CalcMfg:str = obj["CalcMfg"]
      self.CalcMfgPart:str = obj["CalcMfgPart"]
      self.calcMinOrderQty:int = obj["calcMinOrderQty"]
      self.CalcOurQty:int = obj["CalcOurQty"]
      self.calcPartPUM:str = obj["calcPartPUM"]
      self.CalcPurchasingFactor:int = obj["CalcPurchasingFactor"]
      """  purchasing factor  """  
      self.CalcPurchasingFactorDirection:str = obj["CalcPurchasingFactorDirection"]
      self.CalcTotalCost:int = obj["CalcTotalCost"]
      self.CalcTranType:str = obj["CalcTranType"]
      self.CalcVendQty:int = obj["CalcVendQty"]
      self.Configured:str = obj["Configured"]
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      self.ContractOrder:bool = obj["ContractOrder"]
      self.CostPerCodeContract:str = obj["CostPerCodeContract"]
      """  Indicates the costing per quantity (When Contract PO). It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.CPFactor:int = obj["CPFactor"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DelPoSug:bool = obj["DelPoSug"]
      self.DisablePartRevBtn:bool = obj["DisablePartRevBtn"]
      self.DispAcctDescription:str = obj["DispAcctDescription"]
      """  Display Account Description.  """  
      self.DispExpAccount:str = obj["DispExpAccount"]
      """  A character string made up of Div, Dept, Chart and Segment values and their related separators concatenated into the full GL account number.  """  
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      self.DocScrUnitCost:int = obj["DocScrUnitCost"]
      self.EnableRcvInspectionReq:bool = obj["EnableRcvInspectionReq"]
      """  False if vendor or class requires inspection, otherwise true.  """  
      self.ExpChart:str = obj["ExpChart"]
      """  The Chart ID component of the default G/L account.  """  
      self.ExpDivision:str = obj["ExpDivision"]
      """  The Division Component of the default expence G/L account.  """  
      self.ExpGLDept:str = obj["ExpGLDept"]
      """  The Department component of the default G/L account.  """  
      self.FromPOSugChg:bool = obj["FromPOSugChg"]
      self.LinkedSOConfig:bool = obj["LinkedSOConfig"]
      self.MultiRel:bool = obj["MultiRel"]
      self.NonMasterPart:bool = obj["NonMasterPart"]
      self.OpCode:str = obj["OpCode"]
      self.PartQtyBearing:bool = obj["PartQtyBearing"]
      self.POHeaderApprove:bool = obj["POHeaderApprove"]
      self.PORelOneOpenRelease:bool = obj["PORelOneOpenRelease"]
      """  True if there is only one release and it's open.  """  
      self.PriceBrkBTNSensitive:bool = obj["PriceBrkBTNSensitive"]
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  Reference Code Description  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Reference Code Status  """  
      self.ReferenceCode:str = obj["ReferenceCode"]
      """  Link to the related code in GlRefCod.RefCode  """  
      self.Rpt1CalcTotalCost:int = obj["Rpt1CalcTotalCost"]
      self.Rpt1ScrUnitCost:int = obj["Rpt1ScrUnitCost"]
      self.Rpt2CalcTotalCost:int = obj["Rpt2CalcTotalCost"]
      self.Rpt2ScrUnitCost:int = obj["Rpt2ScrUnitCost"]
      self.Rpt3CalcTotalCost:int = obj["Rpt3CalcTotalCost"]
      self.Rpt3ScrUnitCost:int = obj["Rpt3ScrUnitCost"]
      self.ScrUnitCost:int = obj["ScrUnitCost"]
      """   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  """  
      self.SetCheveron:bool = obj["SetCheveron"]
      self.SubAvail:bool = obj["SubAvail"]
      self.UpdateRelRecords:bool = obj["UpdateRelRecords"]
      self.UpdateRelTaxable:bool = obj["UpdateRelTaxable"]
      """  Update PO Release Taxable Flag on Change of PO Detail Taxable Flag  """  
      self.VendPurPoint:str = obj["VendPurPoint"]
      """  Purchase Point used in the Supplier Tracker.  """  
      self.AllowPORecon:bool = obj["AllowPORecon"]
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      """  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  """  
      self.AttributeQtyMismatch:bool = obj["AttributeQtyMismatch"]
      """  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  """  
      self.CalcJobMtlSeq:int = obj["CalcJobMtlSeq"]
      self.CalcJobOprSeq:int = obj["CalcJobOprSeq"]
      self.HasBuyToOrderRelease:bool = obj["HasBuyToOrderRelease"]
      """  Flag to indicate the current PO Line has at least one Buy To Order Release  """  
      self.LineAmtCalcd:bool = obj["LineAmtCalcd"]
      """  The flag to indicate if PO  doc/base/rpt line amounts are recalculated  whne entered and no need to recalculate on save.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClassInactive:bool = obj["ClassInactive"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.GlPurchPurchDesc:str = obj["GlPurchPurchDesc"]
      self.MfgNumMfgID:str = obj["MfgNumMfgID"]
      self.MfgNumName:str = obj["MfgNumName"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PONUMCurrencyCode:str = obj["PONUMCurrencyCode"]
      self.PONUMOrderDate:str = obj["PONUMOrderDate"]
      self.PONUMInPrice:bool = obj["PONUMInPrice"]
      self.PONUMShipName:str = obj["PONUMShipName"]
      self.PONUMShipToConName:str = obj["PONUMShipToConName"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.DeliveryInstructions_c:str = obj["DeliveryInstructions_c"]
      pass

class Erp_Tablesets_PODetailTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of PODetail record  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  Reportable Amount  """  
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
      """  User ID of the user who created the record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date / time that the record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date/ time that the record was last changed  """  
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
      """  ResolutionNum  """  
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
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
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
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POHeadMiscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that this miscellaneous record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when they requested miscellaneous maintenance.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. This will be printed on the PO. The default is provided by PurMisc.Description, but it is overridable by the user. This can't be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The Customer Currency amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Sets the miscellaneous line as being taxable. This is used to pass along to invoice processing.  """  
      self.InvoicedAmt:int = obj["InvoicedAmt"]
      """  Amount invoiced against this POMisc record. This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  """  
      self.DocInvoicedAmt:int = obj["DocInvoicedAmt"]
      """  Amount invoiced against this POMisc record(Customer Currency). This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line created for this PO Line for the Inter-Company Trading.  """  
      self.OrderSeqNum:int = obj["OrderSeqNum"]
      """  Order Misc Seq Num created for this PO Misc Seq Num for the Inter-Company Trading.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order misc charge.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.Rpt1InvoicedAmt:int = obj["Rpt1InvoicedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoicedAmt:int = obj["Rpt2InvoicedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoicedAmt:int = obj["Rpt3InvoicedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InMiscAmt:int = obj["InMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.DocInMiscAmt:int = obj["DocInMiscAmt"]
      """  The Customer Currency amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.Rpt1InMiscAmt:int = obj["Rpt1InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InMiscAmt:int = obj["Rpt2InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InMiscAmt:int = obj["Rpt3InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.InInvoiceAmt:int = obj["InInvoiceAmt"]
      """  Amount invoiced against this POMisc record. This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  """  
      self.DocInInvoiceAmt:int = obj["DocInInvoiceAmt"]
      """  Amount invoiced against this POMisc record(Customer Currency). This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  """  
      self.Rpt1InInvoiceAmt:int = obj["Rpt1InInvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InInvoiceAmt:int = obj["Rpt2InInvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InInvoiceAmt:int = obj["Rpt3InInvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True the tax engine will not calculate any miscellaneous charge tax information  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrencySymbol:str = obj["CurrencySymbol"]
      self.DocCurrencySymbol:str = obj["DocCurrencySymbol"]
      self.POHeaderApprove:bool = obj["POHeaderApprove"]
      self.Rpt1ScrMiscAmt:int = obj["Rpt1ScrMiscAmt"]
      self.Rpt2ScrMiscAmt:int = obj["Rpt2ScrMiscAmt"]
      self.Rpt3ScrMiscAmt:int = obj["Rpt3ScrMiscAmt"]
      self.ScrDocMiscAmt:int = obj["ScrDocMiscAmt"]
      self.ScrMiscAmt:int = obj["ScrMiscAmt"]
      self.TaxIDDescription:str = obj["TaxIDDescription"]
      """  Description of Tax ID  """  
      self.DocTotalDedTax:int = obj["DocTotalDedTax"]
      """  Total deductable tax amount for this PO Line in document currency.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in document currency.  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """  Total Tax amount for this PO Line in document currency.  """  
      self.Rpt1TotalDedTax:int = obj["Rpt1TotalDedTax"]
      """  Total deductable tax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """  Total Tax amount for this PO Line in Rpt1 currency,  """  
      self.Rpt2TotalDedTax:int = obj["Rpt2TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """  Total Tax amount for this PO Line in Rpt2 currency,  """  
      self.Rpt3TotalDedTax:int = obj["Rpt3TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt3 currency.  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """  Total Tax amount for this PO Line in Rpt3 currency,  """  
      self.TotalDedTax:int = obj["TotalDedTax"]
      """  Total deductable tax amount for this PO Line in base currency.  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in base currency.  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Total Tax amount for this PO Line in base currency,  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeTaxCatID:str = obj["MiscCodeTaxCatID"]
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.PONumInPrice:bool = obj["PONumInPrice"]
      self.PONumShipToConName:str = obj["PONumShipToConName"]
      self.PONumShipName:str = obj["PONumShipName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POHeaderAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PONum:int = obj["PONum"]
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

class Erp_Tablesets_POHeaderListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if the order is open or closed. This is set automatically when all the PODetail records have been closed or can be set if the user Voids the Order. This field is not directly maintainable.  """  
      self.VoidOrder:bool = obj["VoidOrder"]
      """  Indicates if the entire remaining Purchase Order is Voided. When an order is voided the POHeader.OpenOrder is set to No and all remaining PODetail and PORel records for the related order are closed and voided.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Order Date for this purchase order. Initially defaults as "today", then defaults as last date entered in this session.  """  
      self.FOB:str = obj["FOB"]
      """  Incoterms  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Ship Via Code  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms  """  
      self.ShipName:str = obj["ShipName"]
      """  defaults from the company file.  """  
      self.ShipAddress1:str = obj["ShipAddress1"]
      """  First adress line  """  
      self.ShipAddress2:str = obj["ShipAddress2"]
      """  Second address line  """  
      self.ShipAddress3:str = obj["ShipAddress3"]
      """  Third address line  """  
      self.ShipCity:str = obj["ShipCity"]
      """  City portion of the address  """  
      self.ShipState:str = obj["ShipState"]
      """  Statee portion of the address  """  
      self.ShipCountry:str = obj["ShipCountry"]
      """  Country is used as part of the Ship to  address. It can be left blank.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID that links to the Purchasing Agent master file.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  """  
      self.ShipToConName:str = obj["ShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.ReadyToPrint:bool = obj["ReadyToPrint"]
      """  Indicates if the PO can be printed. Print functions are not available if this is = No.  """  
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorName:str = obj["VendorName"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  System date that the PO was approved.  This only pertains to PO which exceeded the buyers limit and have been approved.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  The BuyerID  that approved the PO. (See ApprovedDate for related info)  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.Approve:bool = obj["Approve"]
      """   Inidicates if the PO is "ready" to be approved.  This is checked  when all the information is complete and is ready to be processed. When checked the system will test if PO has exceeded the buyers or system purchasing limit.  (See ApprovalStatus for related info)
When Approve = yes the PO cannot be maintained.  """  
      self.ApprovalStatus:str = obj["ApprovalStatus"]
      """   Indicates the approval status of the PO.
Valid values are; U - Unsubmitted for Approval,  P - Pending Approval, A - Approved, R - Rejected.  Before a PO can be printed it must be approved.  A PO is consider  approved if it doesn't exceed the buyers limit or it has been approved by the approver.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.POType:str = obj["POType"]
      """  PO Type Identifier ('STD' - standard PO, 'CMI' - Customer managed inventory PO, or 'SMI' - Supplier managed inventory PO)  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POHeaderMiscTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number  """  
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
      """  User ID o fthe user who created the record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date / time that the record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date/ time that the record was last changed  """  
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
      self.Migrated:bool = obj["Migrated"]
      """  Indicates if this row was created as part of the migration process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
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
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if the order is open or closed. This is set automatically when all the PODetail records have been closed or can be set if the user Voids the Order. This field is not directly maintainable.  """  
      self.VoidOrder:bool = obj["VoidOrder"]
      """  Indicates if the entire remaining Purchase Order is Voided. When an order is voided the POHeader.OpenOrder is set to No and all remaining PODetail and PORel records for the related order are closed and voided.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Order Date for this purchase order. Initially defaults as "today", then defaults as last date entered in this session.  """  
      self.FOB:str = obj["FOB"]
      """  Incoterms  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Ship Via Code  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms  """  
      self.ShipName:str = obj["ShipName"]
      """  defaults from the company file.  """  
      self.ShipAddress1:str = obj["ShipAddress1"]
      """  First adress line  """  
      self.ShipAddress2:str = obj["ShipAddress2"]
      """  Second address line  """  
      self.ShipAddress3:str = obj["ShipAddress3"]
      """  Third address line  """  
      self.ShipCity:str = obj["ShipCity"]
      """  City portion of the address  """  
      self.ShipState:str = obj["ShipState"]
      """  Statee portion of the address  """  
      self.ShipZIP:str = obj["ShipZIP"]
      """  Postal code or Zip code portion of the address  """  
      self.ShipCountry:str = obj["ShipCountry"]
      """  Country is used as part of the Ship to  address. It can be left blank.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID that links to the Purchasing Agent master file.  """  
      self.FreightPP:bool = obj["FreightPP"]
      """  The freight charge is to be paid by the vendor.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the VendCnt  table. Use the Vendor.PRIMPCON as the default. or the VendorPP.PrimPCon if a vendor purchase point is referenced.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about over all  purchase order. These will be printed on the purchase order.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  """  
      self.ShipToConName:str = obj["ShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.ReadyToPrint:bool = obj["ReadyToPrint"]
      """  Indicates if the PO can be printed. Print functions are not available if this is = No.  """  
      self.PrintAs:str = obj["PrintAs"]
      """  N = New, C = Change Order  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.ShipCountryNum:int = obj["ShipCountryNum"]
      """  Country part of address. This field is in sync with the Country field. Must be a valid entry in the Country table.  """  
      self.LogChanges:bool = obj["LogChanges"]
      """  This field indicates if the system should generate purchase order booking records. Booking tables are used to track changes to POheader.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  System date that the PO was approved.  This only pertains to PO which exceeded the buyers limit and have been approved.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  The BuyerID  that approved the PO. (See ApprovedDate for related info)  """  
      self.Approve:bool = obj["Approve"]
      """   Inidicates if the PO is "ready" to be approved.  This is checked  when all the information is complete and is ready to be processed. When checked the system will test if PO has exceeded the buyers or system purchasing limit.  (See ApprovalStatus for related info)
When Approve = yes the PO cannot be maintained.  """  
      self.ApprovalStatus:str = obj["ApprovalStatus"]
      """   Indicates the approval status of the PO.
Valid values are; U - Unsubmitted for Approval,  P - Pending Approval, A - Approved, R - Rejected.  Before a PO can be printed it must be approved.  A PO is consider  approved if it doesn't exceed the buyers limit or it has been approved by the approver.  """  
      self.ApprovedAmount:int = obj["ApprovedAmount"]
      """   An internally used field that represents the total amount of the PO (in base currency) captured the last time the po was approved/rejected.  Note: this only pertains to PO that required approval in the first place otherwise it's zero.  The limit checking process will compare PO amounts to the greater of the buyers limit or this amount. Basically, if the PO was already approved once for a specific amount then it should not require subsequent approval until that amount is exceeded.
Note: This also contains the PO amount if it was rejected. In this case, the PO remains as rejected until they reduce the PO amount.  """  
      self.PostToWeb:bool = obj["PostToWeb"]
      """  Indicates the Supplier will respond via Suppliers workbench  """  
      self.PostDate:str = obj["PostDate"]
      """  Date Buyer posted the PO  """  
      self.VendorRefNum:str = obj["VendorRefNum"]
      """  Vendor reference number.  """  
      self.ConfirmReq:bool = obj["ConfirmReq"]
      """  Indicated this PO requires a confirmation.  This would default yes for any Web Vendor  """  
      self.Confirmed:bool = obj["Confirmed"]
      """  Indicated Supplier Confirmed the PO  """  
      self.ConfirmVia:str = obj["ConfirmVia"]
      """   Indicates if the Supplier has confirmed that they intend to fill the Order, and that it will be done through Supplier Connect("web"), 
phoned in a confirmation and clicked on the Confirmed checkbox in Epicor ("client"), or they clicked on the "Reject" checkbox in Supplier Connect("rejected").  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.XRefPONum:str = obj["XRefPONum"]
      """  Cross reference PO number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      """  Consolidated PO flag.  Used in Consolidated Purchasing.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.ContractOrder:bool = obj["ContractOrder"]
      """  Is this Purchase Order a Contract Purchase Order?  """  
      self.ContractStartDate:str = obj["ContractStartDate"]
      """  The date the Contract Purchase Order is active.  """  
      self.ContractEndDate:str = obj["ContractEndDate"]
      """  The date the Contract Purchase Order expires.  """  
      self.PrintHeaderAddress:bool = obj["PrintHeaderAddress"]
      """  Print Header Address flag  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.POType:str = obj["POType"]
      """  PO Type Identifier ('STD' - standard PO, 'CMI' - Customer managed inventory PO, or 'SMI' - Supplier managed inventory PO)  """  
      self.APLOCID:str = obj["APLOCID"]
      """  Letter of Credit ID.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document for the record.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.ICPOLocked:bool = obj["ICPOLocked"]
      """  ICPOLocked  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DueDate:str = obj["DueDate"]
      """  Specifies the date by which you need to receive the whole Purchase Order. If you set the Due Date before create lines and releases, it will act as a default value when adding new lines/releases.  """  
      self.PromiseDate:str = obj["PromiseDate"]
      """  Specifies the date on which the supplier has promised to ship the whole Purchase Order. If you set the Promise Date before create lines and releases, it will act as a default value when adding releases.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date and time that the record was last changed.  """  
      self.POTaxReadyToProcess:bool = obj["POTaxReadyToProcess"]
      """  Flag to determine whether PO taxes will be automatically calculated each time a PO line is updated.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Liability for this Purchase Order  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Total Tax amount for this PO in base currency, Totals the TaxAmt from the POTax records of this purchase order  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """  Total Tax amount for this PO in document currency, Totals the DocTaxAmt from the POTax records of this purchase order  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """  Total Tax amount for this PO in Rpt1 currency, Totals the Rpt1TaxAmt from the POTax records of this purchase order  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """  Total Tax amount for this PO in Rpt2 currency, Totals the Rpt2TaxAmt from the POTax records of this purchase order  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """  Total Tax amount for this PO in Rpt3 currency, Totals the Rpt3TaxAmt from the POTax records of this purchase order  """  
      self.TotalWhTax:int = obj["TotalWhTax"]
      """  Total Order Withholding Taxes in base currency  """  
      self.DocTotalWhTax:int = obj["DocTotalWhTax"]
      """  Total Order Withholding Taxes in document currency  """  
      self.Rpt1TotalWhTax:int = obj["Rpt1TotalWhTax"]
      """  Total Order Withholding Taxes in Rpt1 currency  """  
      self.Rpt2TotalWhTax:int = obj["Rpt2TotalWhTax"]
      """  Total Order Withholding Taxes in Rpt2 currency  """  
      self.Rpt3TotalWhTax:int = obj["Rpt3TotalWhTax"]
      """  Total Order Withholding Taxes in Rpt3 currency  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Order Self Assessed Taxes in base currency.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Order Self Assessed Taxes in document currency.  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Order Self Assessed Taxes in Rpt1 currency.  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Order Self Assessed Taxes in Rpt2 currency.  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Order Self Assessed Taxes in Rpt3 currency.  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.HdrTaxNoUpdt:bool = obj["HdrTaxNoUpdt"]
      """  This flag determines whether any manual taxes were created for a header miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code - FUTUREUSE  """  
      self.TotalDedTax:int = obj["TotalDedTax"]
      """  Total deductable tax amount in base currency.  """  
      self.DocTotalDedTax:int = obj["DocTotalDedTax"]
      """  Total deductable tax amount in document currency.  """  
      self.Rpt1TotalDedTax:int = obj["Rpt1TotalDedTax"]
      """  Total deductable tax amount in Rpt1 currency.  """  
      self.Rpt2TotalDedTax:int = obj["Rpt2TotalDedTax"]
      """  Total deductable tax amount in Rpt2 currency.  """  
      self.Rpt3TotalDedTax:int = obj["Rpt3TotalDedTax"]
      """  Total deductable tax amount in Rpt3 currency.  """  
      self.TotalCharges:int = obj["TotalCharges"]
      """  Total charge amount for the PO in base currency,  This is the sum of PODetail.ExtCost for non voided lines.  """  
      self.TotalMiscCharges:int = obj["TotalMiscCharges"]
      """  Total amount for all miscellaneous charges associated to this PO in base currency.  This is the sum of POMisc.MiscAmt.  """  
      self.TotalOrder:int = obj["TotalOrder"]
      """  Total amount for the PO in base currency.  This is the sum of POMisc.MiscAmt + PODetail.ExtCost + POHeader.TotalTax.  """  
      self.DocTotalCharges:int = obj["DocTotalCharges"]
      """  Total charge amount for the PO in document currency,  This is the sum of PODetail.DocExtCost for non voided lines.  """  
      self.DocTotalMisc:int = obj["DocTotalMisc"]
      """  Total amount for all miscellaneous charges associated to this PO in document currency.  This is the sum of POMisc.DocMiscAmt.  """  
      self.DocTotalOrder:int = obj["DocTotalOrder"]
      """  Total amount for the PO in document currency.  This is the sum of POMisc.DocMiscAmt + PODetail.DocExtCost + POHeader.DocTotalTax.  """  
      self.Rpt1TotalCharges:int = obj["Rpt1TotalCharges"]
      """  Total charge amount for the PO in Rpt1 currency,  This is the sum of PODetail.Rpt1ExtCost for non voided lines.  """  
      self.Rpt2TotalCharges:int = obj["Rpt2TotalCharges"]
      """  Total charge amount for the PO in Rpt2 currency,  This is the sum of PODetail.Rpt2ExtCost for non voided lines.  """  
      self.Rpt3TotalCharges:int = obj["Rpt3TotalCharges"]
      """  Total charge amount for the PO in Rpt3 currency,  This is the sum of PODetail.Rpt3ExtCost for non voided lines.  """  
      self.Rpt1TotalMiscCharges:int = obj["Rpt1TotalMiscCharges"]
      """  Total amount for all miscellaneous charges associated to this PO in Rpt1 currency.  This is the sum of POMisc.Rpt1MiscAmt.  """  
      self.Rpt2TotalMiscCharges:int = obj["Rpt2TotalMiscCharges"]
      """  Total amount for all miscellaneous charges associated to this PO in Rpt2 currency.  This is the sum of POMisc.Rpt2MiscAmt.  """  
      self.Rpt3TotalMiscCharges:int = obj["Rpt3TotalMiscCharges"]
      """  Total amount for all miscellaneous charges associated to this PO in Rpt3 currency.  This is the sum of POMisc.Rpt3MiscAmt.  """  
      self.Rpt1TotalOrder:int = obj["Rpt1TotalOrder"]
      """  Total amount for the PO in Rpt1 currency.  This is the sum of POMisc.Rpt1MiscAmt + PODetail.Rpt1ExtCost + POHeader.Rpt1TotalTax.  """  
      self.Rpt2TotalOrder:int = obj["Rpt2TotalOrder"]
      """  Total amount for the PO in Rpt2 currency.  This is the sum of POMisc.Rpt2MiscAmt + PODetail.Rpt2ExtCost + POHeader.Rpt2TotalTax.  """  
      self.Rpt3TotalOrder:int = obj["Rpt3TotalOrder"]
      """  Total amount for the PO in Rpt3 currency.  This is the sum of POMisc.Rpt3MiscAmt + PODetail.Rpt3ExtCost + POHeader.Rpt3TotalTax.  """  
      self.APTaxRoundOption:int = obj["APTaxRoundOption"]
      """  APTaxRoundOption  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  CNBonded  """  
      self.EDIRevNum:int = obj["EDIRevNum"]
      """  EDI Revision number that marks changes in the purchase order since the last time the purchase order was sent.  """  
      self.EDIPosted:bool = obj["EDIPosted"]
      """  Flag used to mark the Purchase Order as posted to EDI  """  
      self.EDIPostedDate:str = obj["EDIPostedDate"]
      """  Date when the PO was last acknowledge from EDI Portal  """  
      self.EDIAckDate:str = obj["EDIAckDate"]
      """  Date when the PO was last acknowledge from EDI Portal  """  
      self.ApproveMessage:str = obj["ApproveMessage"]
      """  Temporarily stores the return message from the PO approval process  """  
      self.RecalcUnitCosts:bool = obj["RecalcUnitCosts"]
      """  Used when switching the Vendor and need to prompt if the user wants to recalculate unit costs.  """  
      self.RuleCode:int = obj["RuleCode"]
      self.UpdateDtlAndRelRecords:bool = obj["UpdateDtlAndRelRecords"]
      self.VendCntFaxNum:str = obj["VendCntFaxNum"]
      self.VendCntPhoneNumber:str = obj["VendCntPhoneNumber"]
      self.ApproveChkBxSensitive:bool = obj["ApproveChkBxSensitive"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.ConfirmChkBxSensitive:bool = obj["ConfirmChkBxSensitive"]
      self.EnableSupplierID:bool = obj["EnableSupplierID"]
      """  Flag for UI to know when to Enable/Disable the SupplierID field in POEntry  """  
      self.HasLines:bool = obj["HasLines"]
      """  True is there are lines for this PO  """  
      self.HoldChkBxSensitive:bool = obj["HoldChkBxSensitive"]
      self.MassPrntChkBxSensitive:bool = obj["MassPrntChkBxSensitive"]
      self.RefCodeCurrSymbol:str = obj["RefCodeCurrSymbol"]
      self.VendAddrFormat:str = obj["VendAddrFormat"]
      """  The formatted vendor address  """  
      self.EDIEnable:bool = obj["EDIEnable"]
      self.BitFlag:int = obj["BitFlag"]
      self.APLOCDescription:str = obj["APLOCDescription"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.ShipCountryNumDescription:str = obj["ShipCountryNumDescription"]
      self.ShipViaCodeInactive:bool = obj["ShipViaCodeInactive"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorName:str = obj["VendorName"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorState:str = obj["VendorState"]
      self.VendorEDISupplier:bool = obj["VendorEDISupplier"]
      self.VendorCntName:str = obj["VendorCntName"]
      self.VendorCntEmailAddress:str = obj["VendorCntEmailAddress"]
      self.VendorCntPhoneNum:str = obj["VendorCntPhoneNum"]
      self.VendorCntFaxNum:str = obj["VendorCntFaxNum"]
      self.VendorPPAddress3:str = obj["VendorPPAddress3"]
      self.VendorPPCountry:str = obj["VendorPPCountry"]
      self.VendorPPZip:str = obj["VendorPPZip"]
      self.VendorPPState:str = obj["VendorPPState"]
      self.VendorPPAddress1:str = obj["VendorPPAddress1"]
      self.VendorPPName:str = obj["VendorPPName"]
      self.VendorPPPrimPCon:int = obj["VendorPPPrimPCon"]
      self.VendorPPAddress2:str = obj["VendorPPAddress2"]
      self.VendorPPCity:str = obj["VendorPPCity"]
      self.XbSystAllowLinkedPOChg:bool = obj["XbSystAllowLinkedPOChg"]
      self.XbSystPOUserInt2Label:str = obj["XbSystPOUserInt2Label"]
      self.XbSystPOUserDate3Label:str = obj["XbSystPOUserDate3Label"]
      self.XbSystPOUserChar3Label:str = obj["XbSystPOUserChar3Label"]
      self.XbSystPOUserChar4Label:str = obj["XbSystPOUserChar4Label"]
      self.XbSystPOUserChar2Label:str = obj["XbSystPOUserChar2Label"]
      self.XbSystPOUserDate2Label:str = obj["XbSystPOUserDate2Label"]
      self.XbSystPOUserInt1Label:str = obj["XbSystPOUserInt1Label"]
      self.XbSystPOUserDec1Label:str = obj["XbSystPOUserDec1Label"]
      self.XbSystPOUserDec2Label:str = obj["XbSystPOUserDec2Label"]
      self.XbSystPOUserDate4Label:str = obj["XbSystPOUserDate4Label"]
      self.XbSystPOUserDate1Label:str = obj["XbSystPOUserDate1Label"]
      self.XbSystPOUserChar1Label:str = obj["XbSystPOUserChar1Label"]
      self.XbSystDisableOverridePriceListOption:bool = obj["XbSystDisableOverridePriceListOption"]
      self.XbSystPOTaxCalculate:bool = obj["XbSystPOTaxCalculate"]
      self.XbSystAPTaxLnLevel:bool = obj["XbSystAPTaxLnLevel"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.PrePaymentFlag_c:bool = obj["PrePaymentFlag_c"]
      self.PrePaymentTerms_c:str = obj["PrePaymentTerms_c"]
      self.ProductFamily_c:str = obj["ProductFamily_c"]
      self.VendorConfirmationNo_c:str = obj["VendorConfirmationNo_c"]
      self.POTerms_c:str = obj["POTerms_c"]
      pass

class Erp_Tablesets_POHeaderTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order.  """  
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
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last changed (seconds since midnight)  """  
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
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.ScrDocDedTaxAmt:int = obj["ScrDocDedTaxAmt"]
      self.ScrDocFixedAmount:int = obj["ScrDocFixedAmount"]
      """  Doc Fixed Amount  """  
      self.ScrDocReportableAmt:int = obj["ScrDocReportableAmt"]
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

class Erp_Tablesets_POMiscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that this miscellaneous record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when they requested miscellaneous maintenance.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. This will be printed on the PO. The default is provided by PurMisc.Description, but it is overridable by the user. This can't be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The Customer Currency amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Sets the miscellaneous line as being taxable. This is used to pass along to invoice processing.  """  
      self.InvoicedAmt:int = obj["InvoicedAmt"]
      """  Amount invoiced against this POMisc record. This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  """  
      self.DocInvoicedAmt:int = obj["DocInvoicedAmt"]
      """  Amount invoiced against this POMisc record(Customer Currency). This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line created for this PO Line for the Inter-Company Trading.  """  
      self.OrderSeqNum:int = obj["OrderSeqNum"]
      """  Order Misc Seq Num created for this PO Misc Seq Num for the Inter-Company Trading.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order misc charge.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.Rpt1InvoicedAmt:int = obj["Rpt1InvoicedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoicedAmt:int = obj["Rpt2InvoicedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoicedAmt:int = obj["Rpt3InvoicedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InMiscAmt:int = obj["InMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.DocInMiscAmt:int = obj["DocInMiscAmt"]
      """  The Customer Currency amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.Rpt1InMiscAmt:int = obj["Rpt1InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InMiscAmt:int = obj["Rpt2InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InMiscAmt:int = obj["Rpt3InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.InInvoiceAmt:int = obj["InInvoiceAmt"]
      """  Amount invoiced against this POMisc record. This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  """  
      self.DocInInvoiceAmt:int = obj["DocInInvoiceAmt"]
      """  Amount invoiced against this POMisc record(Customer Currency). This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  """  
      self.Rpt1InInvoiceAmt:int = obj["Rpt1InInvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InInvoiceAmt:int = obj["Rpt2InInvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InInvoiceAmt:int = obj["Rpt3InInvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True the tax engine will not calculate any miscellaneous charge tax information  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrencySymbol:str = obj["CurrencySymbol"]
      self.DocCurrencySymbol:str = obj["DocCurrencySymbol"]
      self.POHeaderApprove:bool = obj["POHeaderApprove"]
      self.Rpt1ScrMiscAmt:int = obj["Rpt1ScrMiscAmt"]
      self.Rpt2ScrMiscAmt:int = obj["Rpt2ScrMiscAmt"]
      self.Rpt3ScrMiscAmt:int = obj["Rpt3ScrMiscAmt"]
      self.ScrDocMiscAmt:int = obj["ScrDocMiscAmt"]
      self.ScrMiscAmt:int = obj["ScrMiscAmt"]
      self.TaxIDDescription:str = obj["TaxIDDescription"]
      """  Description of Tax ID  """  
      self.DocTotalDedTax:int = obj["DocTotalDedTax"]
      """  Total deductable tax amount for this PO Line in document currency.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in document currency.  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """  Total Tax amount for this PO Line in document currency.  """  
      self.Rpt1TotalDedTax:int = obj["Rpt1TotalDedTax"]
      """  Total deductable tax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """  Total Tax amount for this PO Line in Rpt1 currency,  """  
      self.Rpt2TotalDedTax:int = obj["Rpt2TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """  Total Tax amount for this PO Line in Rpt2 currency,  """  
      self.Rpt3TotalDedTax:int = obj["Rpt3TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt3 currency.  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """  Total Tax amount for this PO Line in Rpt3 currency,  """  
      self.TotalDedTax:int = obj["TotalDedTax"]
      """  Total deductable tax amount for this PO Line in base currency.  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in base currency.  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Total Tax amount for this PO Line in base currency,  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      self.MiscCodeTaxCatID:str = obj["MiscCodeTaxCatID"]
      self.PONumInPrice:bool = obj["PONumInPrice"]
      self.PONumShipName:str = obj["PONumShipName"]
      self.PONumShipToConName:str = obj["PONumShipToConName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PORelAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
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

class Erp_Tablesets_PORelRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenRelease:bool = obj["OpenRelease"]
      """  Indicates if this release is open.  This is normally closed via the receiving program. But can be changed indirectly  by the user during order entry when they "Void" the release..  """  
      self.VoidRelease:bool = obj["VoidRelease"]
      """   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.
When an PORel record is 'voided',  PORel.OpenRelease is set to "no".  If no other open PORel records exist for the related PODetail then the PoDetail.OpenLine is set to "No". If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoDetail or PoHeader is voided.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.DueDate:str = obj["DueDate"]
      """  Specifies the date by which you need to receive a release of a part. This date is taken from the Purchase Order Line Due Date, if it’s null, PORel.DueDate will take the value from POHeader.DueDate. If you're adding releases from: - BTO or Drop Shipments, PORel.DueDate will take the value from OrderRel.NeedByDate  - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  """  
      self.XRelQty:int = obj["XRelQty"]
      """  Order quantity for this release in our unit of measure.  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Vice-Versa.
Formula: XRelQty * Factor = RelQty  """  
      self.RelQty:int = obj["RelQty"]
      """  Order quantity for this release in vendors unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  This is populated for Purchase Direct items only and contains the job number for the purchased direct item.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  This is populated for Purchase Direct items only and contains the assembly number for the purchased direct item.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.
FYI: This field can indirectly sets the TranType field via the write trigger. It can itself be set from the TranType. System keeps them compatible. JobSeqType/TranType values are; M = PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN. This possibly could have been deleted. However we decided to keep it for backward compatablity reasons.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that the item on this release is being purchased for.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Total quantity received to stock to date. In Purchasing unit of measure. This is a field maintained by the receipt process.  """  
      self.ExpOverride:bool = obj["ExpOverride"]
      """  Indicates if the user overrode the default  expense accounts for this release. This field prevents the program from resetting the account #'s when the user changes other fields that trigger new default accounts to be set. If "Yes" then the defaults will not be used.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition which generated this PORel record.  """  
      self.ReqLine:int = obj["ReqLine"]
      """  Requisition line which generated this PORel record.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PromiseDt:str = obj["PromiseDt"]
      """  Specifies the date on which the supplier has promised to ship this release.This date is taken from POHeader.PromiseDate. If you're adding releases from: - BTO or Drop Shipments, PORel.PromiseDt will take the value from OrderRel.NeedByDate. - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.Confirmed:bool = obj["Confirmed"]
      """  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  """  
      self.ConfirmVia:str = obj["ConfirmVia"]
      """  Can be "web", "client", or "rejected"  """  
      self.ReqChgDate:str = obj["ReqChgDate"]
      """   When the Due Date is changed, this is the previous DueDate.
(originally was "Requested pending date change")  """  
      self.ReqChgQty:int = obj["ReqChgQty"]
      """   When the RelQty is changed, this is the previous RelQty.
(was "Requested change quantity")  """  
      self.LockRel:str = obj["LockRel"]
      """  OBSOLETE FIELD-A PO release with a locked status will not generate a change suggestion.  SEV, 11/21/02: New convention to indicate who is blocking new suggestions: the presence of "B" indicates the Buyer, and "V" indicates the Vendor.  "BV" means both Buyer and Vendor want no changes in Date or Qty on this release.  """  
      self.RefDisplayAccount:str = obj["RefDisplayAccount"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!, REPLACED BY ADDING INDIVIDUAL COMPONENT FIELDS) A character string made up of Division, GLDept and Chart fields concatenated using the user defined configuration options found in XaSyst file.  This should be formatted exactly how the user expects to see their account numbers (including separators).  This field is generated via the maintenance program.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line created for this PO Line for the Inter-Company Trading.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order Release Line created for this PO Release for the Inter-Company Trading.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order release.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  Total quantity shipped but not received (In-Transit).  In Purchasing unit of measure.  This is a summary maintained by the receipt process.  This number is 0 every time the company receives every thing the other company ships.  """  
      self.TranType:str = obj["TranType"]
      """   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPlant:str = obj["GlbPlant"]
      """  Global Site identifier.  Relates to the External Site record that is created to correlate the Consolidated Purchasing company to a Site in a local Company.  Used in Consolidated Purchasing.  """  
      self.GlbWarehouse:str = obj["GlbWarehouse"]
      """  Global Warehouse identifier.  Relates to the External Warehouse record that is created to correlate the Consolidated Purchasing company to a Warehouse in a local Company.  Used in Consolidated Purchasing.  """  
      self.GlbCreateJobMtl:bool = obj["GlbCreateJobMtl"]
      """  When this PORel is received in the local company, if this flag is set create JobMtl.  Used in Consolidated Purchasing.  """  
      self.ShippedDate:str = obj["ShippedDate"]
      """  Shipped Date  """  
      self.ContainerID:int = obj["ContainerID"]
      """  ID field to the ContainerHeader table.  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.PreviousDueDate:str = obj["PreviousDueDate"]
      """  This field holds the previous value of Due Date.  """  
      self.BaseQty:int = obj["BaseQty"]
      """  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PORel.XRelQty to the PORel.BaseUOM .  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """   Unit of Measure of the PORel.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  """  
      self.BTOOrderNum:int = obj["BTOOrderNum"]
      """  Order Num related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderLine:int = obj["BTOOrderLine"]
      """  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderRelNum:int = obj["BTOOrderRelNum"]
      """  The release number of the sales order line related to this purchase order. Used only for Buy To Order POs.  """  
      self.DropShip:bool = obj["DropShip"]
      """  The value of this field comes from the sales order release. Used only for Buy To Order POs.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo Num from the sales order release. Used only for Buy To Order POs.  """  
      self.SoldToNum:int = obj["SoldToNum"]
      """  The SoldTo ID from the sales order release. Used only for Buy To Order POs.  """  
      self.SMIRcvdQty:int = obj["SMIRcvdQty"]
      """  This is only updated for SMI type POs.  It will indicate how many items have been received into a SMI bin.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.MangCustNum:int = obj["MangCustNum"]
      """  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates that the One Time ShipTO information defined for this release should be used. OTS fields are only used for Drop Shipments.  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.PORelOpen:bool = obj["PORelOpen"]
      """  Open Purchase Release flag  """  
      self.Mapping:bool = obj["Mapping"]
      """  Mapping  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The Project WBS Phase Id associated with this release. This field can only have data if PORel.ProjectID is not blank.  """  
      self.WBSPhaseID:str = obj["WBSPhaseID"]
      """  Project Phase ID  """  
      self.IsMultiRel:bool = obj["IsMultiRel"]
      """  IsMultiRel  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SMIRemQty:int = obj["SMIRemQty"]
      """  Field to track the SMIRcvdQty that has not yet been moved to stock  """  
      self.LockQty:bool = obj["LockQty"]
      """  When the field is checked, no Increase, Reduce or Cancel suggestions will be created for the PO Release  """  
      self.LockDate:bool = obj["LockDate"]
      """  When the field is checked, no Expedite or Postpone suggestions will be created for the PO Release  """  
      self.DueDateChanged:bool = obj["DueDateChanged"]
      """  Indicates Due Date has been changed.  """  
      self.ContractID:str = obj["ContractID"]
      """  The identifier of the planning contract.  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  """  
      self.Status:str = obj["Status"]
      """  Indicates the current status of the release. This field is maintained by the System automatically. The possible values are: Open (O), Arrived (A), Inspection (I), Received (R), Consumed (U), Drop Shipped (D), Closed (C), Voided (V).  """  
      self.ArrivedQty:int = obj["ArrivedQty"]
      """  Total quantity arrived to our site to date. In Purchasing unit of measure. This is a field maintained by the Receipt Process.  """  
      self.InvoicedQty:int = obj["InvoicedQty"]
      """  Total quantity invoiced to date. In Purchasing unit of measure. This is a field maintained by the AP Invoicing Process.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date the PO Release is required for, this can be either from the Sales Order, Material Job, Subcontract Operation, Due Date set within Generate POSuggestions or the Purchase Order Header Date.  """  
      self.LockNeedByDate:bool = obj["LockNeedByDate"]
      """  Set to 'true' if 'NeedByDate' was derived from a valid demand.  """  
      self.InspectionQty:int = obj["InspectionQty"]
      """  Total to date quantity that has been placed into inspection.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process  """  
      self.DeliverTo:str = obj["DeliverTo"]
      """  PO Line types of 'Other' have no specified warehouse / bin and what this field provides is a means of designating 'where / whom' this delivery is intended for.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Taxable  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this item is exempt from PO tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the PO tax info.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.ReqChgPromiseDate:str = obj["ReqChgPromiseDate"]
      """  When the Promise Date is changed, this is the previous PromiseDt  """  
      self.OTSEMailAddress:str = obj["OTSEMailAddress"]
      """  One Time ShipTo email address.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.NumberOfPiecesUOM:str = obj["NumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.FirmRelease:bool = obj["FirmRelease"]
      """  Indicates if this release is  "FIRM".  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.EDIShipReferenceType:str = obj["EDIShipReferenceType"]
      """  Name of the ship reference that is going to be stored.  """  
      self.EDIShipReferenceData:str = obj["EDIShipReferenceData"]
      """  Data that is going to be stored as ship reference.  """  
      self.EDIEstimatedDockDate:str = obj["EDIEstimatedDockDate"]
      """  Estimated time when the shipment will arrive.  """  
      self.EDIShipQty:int = obj["EDIShipQty"]
      """  Quantity sent by the supplier.  """  
      self.EDIShipQtyUOM:str = obj["EDIShipQtyUOM"]
      """  Unit of Measure of the EDIShipQty.  """  
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      self.ContractOrder:bool = obj["ContractOrder"]
      """  Is this Release related to a Contract Purchase Order?  """  
      self.DelPoSug:bool = obj["DelPoSug"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocTotalDedTax:int = obj["DocTotalDedTax"]
      """  Total deductable tax amount for this PO Line in document currency.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in document currency.  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """  Total Tax amount for this PO Line in document currency.  """  
      self.EnableBTOOrderNum:bool = obj["EnableBTOOrderNum"]
      """  flag to determine whether the BTOOrderNum field can be enabled.  If a drop shipment has been Received/Shipped for this line, we cannot allow them to change the BTOOrderNum.  """  
      self.EnableGLAcct:bool = obj["EnableGLAcct"]
      """  Indicates whether the GL account field should be enabled. Based on GLSyst.PostInvtyWipCos and the line type  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      self.ExpDesc:str = obj["ExpDesc"]
      self.FromPOSugChg:bool = obj["FromPOSugChg"]
      self.GlbPlantName:str = obj["GlbPlantName"]
      self.GlbWhseName:str = obj["GlbWhseName"]
      self.Inspection:bool = obj["Inspection"]
      self.IUM:str = obj["IUM"]
      self.Lock:bool = obj["Lock"]
      """  This field will be used in the UI to Lock and unLock a release.  """  
      self.MangCustID:str = obj["MangCustID"]
      """  For CMI type POs, this is the associated customer that we will verify against the WhseBin.CustNum  """  
      self.MangCustName:str = obj["MangCustName"]
      """  For CMI type POs, this is the associated customer Name that we will verify against the WhseBin.CustNum  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  THIS FIELD COMES DIRECTLY FROM THE POHEADER TABLE.  Indicates if an order is flagged as being HELD , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  """  
      self.POHeaderApprove:bool = obj["POHeaderApprove"]
      self.POType:str = obj["POType"]
      """  Identifies the type of PO  """  
      self.PUM:str = obj["PUM"]
      """  Replicate PUM on detail  """  
      self.PurPoint:str = obj["PurPoint"]
      """  THIS FIELD IS EXTRACTED DIRECTLY FROM THE POHEADER TABLE. Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      self.Rpt1TotalDedTax:int = obj["Rpt1TotalDedTax"]
      """  Total deductable tax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """  Total Tax amount for this PO Line in Rpt1 currency,  """  
      self.Rpt2TotalDedTax:int = obj["Rpt2TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """  Total Tax amount for this PO Line in Rpt2 currency,  """  
      self.Rpt3TotalDedTax:int = obj["Rpt3TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt3 currency.  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """  Total Tax amount for this PO Line in Rpt3 currency,  """  
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      self.StatusDescription:str = obj["StatusDescription"]
      """  Description text of the Status field  """  
      self.TotalDedTax:int = obj["TotalDedTax"]
      """  Total deductable tax amount for this PO Line in base currency.  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in base currency.  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Total Tax amount for this PO Line in base currency,  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """   Transaction Type Description i.e. Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"), 
Stock ("PUR-STK") and Other ("PUR-UKN").  """  
      self.UseGlbFields:bool = obj["UseGlbFields"]
      """  Indicates if Glb fields should be used in place of the non-global equivalent  """  
      self.VendorID:str = obj["VendorID"]
      """  Related Supplier ID  """  
      self.VendorName:str = obj["VendorName"]
      """  Related Vendor Name  """  
      self.ContainerShipped:bool = obj["ContainerShipped"]
      """  Logical indicating if the container has been shipped.  """  
      self.ShipToAddrFormatted:str = obj["ShipToAddrFormatted"]
      """  The formatted ship to address  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  """  
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      """  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  """  
      self.AttributeQtyMismatch:bool = obj["AttributeQtyMismatch"]
      """  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  """  
      self.JobMtlSeq:int = obj["JobMtlSeq"]
      self.JobOprSeq:int = obj["JobOprSeq"]
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.ContainerHeaderPromiseDate:str = obj["ContainerHeaderPromiseDate"]
      self.ContainerHeaderDueDate:str = obj["ContainerHeaderDueDate"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.PlantName:str = obj["PlantName"]
      self.POLineRevisionNum:str = obj["POLineRevisionNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.PONumShipName:str = obj["PONumShipName"]
      self.PONumShipToConName:str = obj["PONumShipToConName"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ReqLineLineDesc:str = obj["ReqLineLineDesc"]
      self.ReqNumShipName:str = obj["ReqNumShipName"]
      self.ReqNumShipToConName:str = obj["ReqNumShipToConName"]
      self.ShipToCustNumInactive:bool = obj["ShipToCustNumInactive"]
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.SoldToNumCustID:str = obj["SoldToNumCustID"]
      self.SoldToNumBTName:str = obj["SoldToNumBTName"]
      self.SoldToNumName:str = obj["SoldToNumName"]
      self.SoldToNumInactive:bool = obj["SoldToNumInactive"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.WBSPhaseDescription:str = obj["WBSPhaseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PORelTGLCRow:
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
      self.POLine:int = obj["POLine"]
      """  POLine of PORel  """  
      self.PONum:int = obj["PONum"]
      """  PONum of PORel  """  
      self.PORelNum:int = obj["PORelNum"]
      """  PORelNum of PORel  """  
      self.ReqRef:bool = obj["ReqRef"]
      self.AcctOverride:bool = obj["AcctOverride"]
      """  Indicates if the user selected a different account from the default.  """  
      self.IsMainBook:bool = obj["IsMainBook"]
      """  Column used to know if the book assigned is the Main Book.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PORelTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
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
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last changed (seconds since midnight)  """  
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
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrencyCode:str = obj["CurrencyCode"]
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
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CalcAutoPORelTGLC_input:
   """ Required : 
   calcTranType
   """  
   def __init__(self, obj):
      self.calcTranType:str = obj["calcTranType"]
      """  Transaction Type  """  
      pass

class CalcAutoPORelTGLC_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ChangeApproveSwitch_input:
   """ Required : 
   ApproveValue
   ds
   """  
   def __init__(self, obj):
      self.ApproveValue:bool = obj["ApproveValue"]
      """  Was PO approved? Yes/No  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeApproveSwitch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ViolationMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeBTOOrderLineWarning_input:
   """ Required : 
   ipOrderNum
   ipOrderLine
   ipPONum
   ipPOLine
   """  
   def __init__(self, obj):
      self.ipOrderNum:int = obj["ipOrderNum"]
      """  Order Number  """  
      self.ipOrderLine:int = obj["ipOrderLine"]
      """  Order Line  """  
      self.ipPONum:int = obj["ipPONum"]
      """  PO Number  """  
      self.ipPOLine:int = obj["ipPOLine"]
      """  PO Line  """  
      pass

class ChangeBTOOrderLineWarning_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWrnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeConfirmSwitch_input:
   """ Required : 
   confirmValue
   ds
   """  
   def __init__(self, obj):
      self.confirmValue:bool = obj["confirmValue"]
      """  Was PO confirmed? Yes/No  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeConfirmSwitch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeContractUOM_input:
   """ Required : 
   NewUOM
   ds
   """  
   def __init__(self, obj):
      self.NewUOM:str = obj["NewUOM"]
      """  New UOM  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeContractUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCountry_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeCountry_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCurrencyCode_input:
   """ Required : 
   iCurrencyCode
   ds
   """  
   def __init__(self, obj):
      self.iCurrencyCode:str = obj["iCurrencyCode"]
      """  Currency Code  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeCurrencyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCurrencySwitch_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeCurrencySwitch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailAssemblySeq_input:
   """ Required : 
   NewAsmSeq
   ds
   """  
   def __init__(self, obj):
      self.NewAsmSeq:int = obj["NewAsmSeq"]
      """  New Assembly to be tested  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailAssemblySeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailCalcOurQty_input:
   """ Required : 
   newCalcOurQty
   ds
   """  
   def __init__(self, obj):
      self.newCalcOurQty:int = obj["newCalcOurQty"]
      """  New Quantity  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailCalcOurQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailCalcVendQty_input:
   """ Required : 
   newCalcVendQty
   ds
   """  
   def __init__(self, obj):
      self.newCalcVendQty:int = obj["newCalcVendQty"]
      """  New Quantity  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailCalcVendQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailCommodityCode_input:
   """ Required : 
   newCommodityCode
   ds
   """  
   def __init__(self, obj):
      self.newCommodityCode:str = obj["newCommodityCode"]
      """  New Commodity Code  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailCommodityCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailContractID_input:
   """ Required : 
   newContractID
   ds
   """  
   def __init__(self, obj):
      self.newContractID:str = obj["newContractID"]
      """  New Contract ID  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailContractID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailCostPerCode_input:
   """ Required : 
   newCostPerCode
   ds
   """  
   def __init__(self, obj):
      self.newCostPerCode:str = obj["newCostPerCode"]
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailCostPerCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailIUM_input:
   """ Required : 
   newIUM
   ds
   """  
   def __init__(self, obj):
      self.newIUM:str = obj["newIUM"]
      """  New IUM  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailIUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailJobNum_input:
   """ Required : 
   NewJobNum
   ds
   """  
   def __init__(self, obj):
      self.NewJobNum:str = obj["NewJobNum"]
      """  New Job Number  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailJobSeq_input:
   """ Required : 
   NewJobSeqNum
   ds
   """  
   def __init__(self, obj):
      self.NewJobSeqNum:int = obj["NewJobSeqNum"]
      """  New job/mtl seq to be tested  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailJobSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailMangCust_input:
   """ Required : 
   NewMangCust
   ds
   """  
   def __init__(self, obj):
      self.NewMangCust:str = obj["NewMangCust"]
      """  New MangCustID  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailMangCust_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailMfgNum_input:
   """ Required : 
   newMfgNum
   ds
   """  
   def __init__(self, obj):
      self.newMfgNum:int = obj["newMfgNum"]
      """  New MfgNum  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailMfgNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailMfgPartNum_input:
   """ Required : 
   newMfgPartNum
   ds
   """  
   def __init__(self, obj):
      self.newMfgPartNum:str = obj["newMfgPartNum"]
      """  New MfgPartNum  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailMfgPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailOrderLine_input:
   """ Required : 
   ipOrderLine
   ds
   """  
   def __init__(self, obj):
      self.ipOrderLine:int = obj["ipOrderLine"]
      """  New OrderLine  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailOrderLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailOrderNum_input:
   """ Required : 
   ipOrderNum
   ds
   """  
   def __init__(self, obj):
      self.ipOrderNum:int = obj["ipOrderNum"]
      """  New OrderNum  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailOrderNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailOverridePriceList_input:
   """ Required : 
   overridePriceList
   ds
   """  
   def __init__(self, obj):
      self.overridePriceList:bool = obj["overridePriceList"]
      """  True is override pricelist has been checked  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailOverridePriceList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailPUM_input:
   """ Required : 
   newPUM
   ds
   """  
   def __init__(self, obj):
      self.newPUM:str = obj["newPUM"]
      """  New PUM  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailPUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailPartClass_input:
   """ Required : 
   NewClassID
   ds
   """  
   def __init__(self, obj):
      self.NewClassID:str = obj["NewClassID"]
      """  New Class ID  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailPartClass_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailPartNum_input:
   """ Required : 
   NewPartNum
   SysRowID
   rowType
   isSubstitute
   ds
   """  
   def __init__(self, obj):
      self.NewPartNum:str = obj["NewPartNum"]
      """  New Part Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Sys Row ID for match (conflict resolution only)  """  
      self.rowType:str = obj["rowType"]
      """  Row Type for match (conflict resolution only)  """  
      self.isSubstitute:bool = obj["isSubstitute"]
      """  True whether it is a Substitute Part  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.NewPartNum:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailRevisionNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailTaxCatID_input:
   """ Required : 
   newTaxCatID
   ds
   """  
   def __init__(self, obj):
      self.newTaxCatID:str = obj["newTaxCatID"]
      """  New Tax Category  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailTaxCatID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailTranType_input:
   """ Required : 
   newTranType
   ds
   """  
   def __init__(self, obj):
      self.newTranType:str = obj["newTranType"]
      """  New Transaction Type  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailTranType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailVenPartNum_input:
   """ Required : 
   newVenPartNum
   ds
   """  
   def __init__(self, obj):
      self.newVenPartNum:str = obj["newVenPartNum"]
      """  New VenPartNum  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeDetailVenPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeExpAcct_input:
   """ Required : 
   proposedAccountNum
   inTGLCTranNum
   ds
   """  
   def __init__(self, obj):
      self.proposedAccountNum:str = obj["proposedAccountNum"]
      """  The proposed account number  """  
      self.inTGLCTranNum:int = obj["inTGLCTranNum"]
      """  The TGLCTranNum of the PORelTGLC record to be checked  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeExpAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHeaderTaxFixedAmount_input:
   """ Required : 
   proposedFixedAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedFixedAmt:int = obj["proposedFixedAmt"]
      """  The proposed fixed amount  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeHeaderTaxFixedAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHeaderTaxRateCodeMaster_input:
   """ Required : 
   proposedRateCode
   ds
   """  
   def __init__(self, obj):
      self.proposedRateCode:str = obj["proposedRateCode"]
      """  The proposed rate code  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeHeaderTaxRateCodeMaster_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHeaderTaxRateCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeHeaderTaxRateCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHeaderTaxReportableAmt_input:
   """ Required : 
   proposedReportableAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedReportableAmt:int = obj["proposedReportableAmt"]
      """  The proposed reportable amount  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeHeaderTaxReportableAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHeaderTaxTaxAmt_input:
   """ Required : 
   proposedTaxAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxAmt:int = obj["proposedTaxAmt"]
      """  The proposed tax amount  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeHeaderTaxTaxAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHeaderTaxTaxCode_input:
   """ Required : 
   proposedTaxCode
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxCode:str = obj["proposedTaxCode"]
      """  The proposed tax code  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeHeaderTaxTaxCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHeaderTaxTaxDeductable_input:
   """ Required : 
   proposedTaxDeductable
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxDeductable:int = obj["proposedTaxDeductable"]
      """  The proposed tax deductable  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeHeaderTaxTaxDeductable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHeaderTaxTaxPercent_input:
   """ Required : 
   proposedTaxPercent
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxPercent:int = obj["proposedTaxPercent"]
      """  The proposed tax percent  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeHeaderTaxTaxPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHeaderTaxTaxableAmt_input:
   """ Required : 
   proposedTaxableAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedTaxableAmt:int = obj["proposedTaxableAmt"]
      """  The proposed taxable amount  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeHeaderTaxTaxableAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePOHeadMiscAmt_input:
   """ Required : 
   proposedMiscAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedMiscAmt:int = obj["proposedMiscAmt"]
      """  The proposed miscellanous amount  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangePOHeadMiscAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePOHeadMiscCode_input:
   """ Required : 
   newMiscCode
   ds
   """  
   def __init__(self, obj):
      self.newMiscCode:str = obj["newMiscCode"]
      """  The code of misc charge  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangePOHeadMiscCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePOHeadMiscPrcnt_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangePOHeadMiscPrcnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePOMiscAmt_input:
   """ Required : 
   proposedMiscAmt
   ds
   """  
   def __init__(self, obj):
      self.proposedMiscAmt:int = obj["proposedMiscAmt"]
      """  The proposed miscellanous amount  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangePOMiscAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePOMiscCode_input:
   """ Required : 
   newMiscCode
   ds
   """  
   def __init__(self, obj):
      self.newMiscCode:str = obj["newMiscCode"]
      """  The code of misc charge  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangePOMiscCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePOMiscPrcnt_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangePOMiscPrcnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePORelContract_input:
   """ Required : 
   ipContractID
   ds
   """  
   def __init__(self, obj):
      self.ipContractID:str = obj["ipContractID"]
      """  New ContractID  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangePORelContract_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ipContractID:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePOTaxRegionCode_input:
   """ Required : 
   newTaxRegionCode
   ds
   """  
   def __init__(self, obj):
      self.newTaxRegionCode:str = obj["newTaxRegionCode"]
      """  New PUM  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangePOTaxRegionCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePOType_input:
   """ Required : 
   newPOType
   ds
   """  
   def __init__(self, obj):
      self.newPOType:str = obj["newPOType"]
      """  Proposed newPOType to be validated  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangePOType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePoMiscCurrSwitch_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangePoMiscCurrSwitch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePrcConNumByNameOrNum_input:
   """ Required : 
   prcConNumOrName
   ds
   """  
   def __init__(self, obj):
      self.prcConNumOrName:str = obj["prcConNumOrName"]
      """  Vendor's contact name or num  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangePrcConNumByNameOrNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePrcConNumByName_input:
   """ Required : 
   prcConName
   ds
   """  
   def __init__(self, obj):
      self.prcConName:str = obj["prcConName"]
      """  Vendor's contact name  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangePrcConNumByName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.prcConNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePrcConNum_input:
   """ Required : 
   PrcConNum
   ds
   """  
   def __init__(self, obj):
      self.PrcConNum:int = obj["PrcConNum"]
      """  Proposed PrcConNum to be validated  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangePrcConNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePurPoint_input:
   """ Required : 
   PurPoint
   ds
   """  
   def __init__(self, obj):
      self.PurPoint:str = obj["PurPoint"]
      """  New Purchase Point  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangePurPoint_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQtyOption_input:
   """ Required : 
   ipQtyOption
   ds
   """  
   def __init__(self, obj):
      self.ipQtyOption:str = obj["ipQtyOption"]
      """  New QtyOption  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeQtyOption_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRelAssemblySeq_input:
   """ Required : 
   NewAsmSeq
   ds
   """  
   def __init__(self, obj):
      self.NewAsmSeq:int = obj["NewAsmSeq"]
      """  New Assembly to be tested  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeRelAssemblySeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRelGlbCompany_input:
   """ Required : 
   ProposedGlbCompany
   ds
   """  
   def __init__(self, obj):
      self.ProposedGlbCompany:str = obj["ProposedGlbCompany"]
      """  Proposed GlbCompany value  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeRelGlbCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRelGlbPlant_input:
   """ Required : 
   ProposedGlbPlant
   ds
   """  
   def __init__(self, obj):
      self.ProposedGlbPlant:str = obj["ProposedGlbPlant"]
      """  Proposed GlbPlant value  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeRelGlbPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRelGlbWarehouse_input:
   """ Required : 
   ProposedGlbWarehouse
   ds
   """  
   def __init__(self, obj):
      self.ProposedGlbWarehouse:str = obj["ProposedGlbWarehouse"]
      """  Proposed GlbCompany value  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeRelGlbWarehouse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRelIUM_input:
   """ Required : 
   NewIUM
   ds
   """  
   def __init__(self, obj):
      self.NewIUM:str = obj["NewIUM"]
      """  New IUM  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeRelIUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRelJobNum_input:
   """ Required : 
   NewJobNum
   ds
   """  
   def __init__(self, obj):
      self.NewJobNum:str = obj["NewJobNum"]
      """  New Job Number  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeRelJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRelJobSeqWarning_input:
   """ Required : 
   ipTranType
   ipJobNum
   ipAssemblySeq
   ipNewJobSeq
   ipPODtlPartNum
   ipPODtlRevNum
   """  
   def __init__(self, obj):
      self.ipTranType:str = obj["ipTranType"]
      """  Transaction Type  """  
      self.ipJobNum:str = obj["ipJobNum"]
      """  Job Number  """  
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      """  Assembly Sequence  """  
      self.ipNewJobSeq:int = obj["ipNewJobSeq"]
      """  Job Sequence  """  
      self.ipPODtlPartNum:str = obj["ipPODtlPartNum"]
      """  Part Number  """  
      self.ipPODtlRevNum:str = obj["ipPODtlRevNum"]
      """  Part Revision  """  
      pass

class ChangeRelJobSeqWarning_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWrnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeRelJobSeq_input:
   """ Required : 
   NewJobSeqNum
   ds
   """  
   def __init__(self, obj):
      self.NewJobSeqNum:int = obj["NewJobSeqNum"]
      """  New job/mtl seq to be tested  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeRelJobSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRelMangCust_input:
   """ Required : 
   NewMangCust
   ds
   """  
   def __init__(self, obj):
      self.NewMangCust:str = obj["NewMangCust"]
      """  New MangCustID  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeRelMangCust_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRelOrderLine_input:
   """ Required : 
   ipOrderLine
   ds
   """  
   def __init__(self, obj):
      self.ipOrderLine:int = obj["ipOrderLine"]
      """  New OrderLine  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeRelOrderLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRelOrderNum_input:
   """ Required : 
   ipOrderNum
   ds
   """  
   def __init__(self, obj):
      self.ipOrderNum:int = obj["ipOrderNum"]
      """  New OrderNum  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeRelOrderNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRelOrderRelNum_input:
   """ Required : 
   ipOrderRelNum
   ds
   """  
   def __init__(self, obj):
      self.ipOrderRelNum:int = obj["ipOrderRelNum"]
      """  New OrderRelNum  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeRelOrderRelNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.opWrnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeRelOurQty_input:
   """ Required : 
   NewOurQty
   ds
   """  
   def __init__(self, obj):
      self.NewOurQty:int = obj["NewOurQty"]
      """  New quantity to be tested  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeRelOurQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.opWarningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeRelPUM_input:
   """ Required : 
   NewPUM
   ds
   """  
   def __init__(self, obj):
      self.NewPUM:str = obj["NewPUM"]
      """  New PUM  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeRelPUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRelPlant_input:
   """ Required : 
   newPlant
   ds
   """  
   def __init__(self, obj):
      self.newPlant:str = obj["newPlant"]
      """  New Plant  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeRelPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRelTaxExempt_input:
   """ Required : 
   newTaxExempt
   ds
   """  
   def __init__(self, obj):
      self.newTaxExempt:str = obj["newTaxExempt"]
      """  New Tax Exempt  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeRelTaxExempt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRelVendQty_input:
   """ Required : 
   NewVendQty
   ds
   """  
   def __init__(self, obj):
      self.NewVendQty:int = obj["NewVendQty"]
      """  New quantity to be tested  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeRelVendQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.opWarningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeTaxDeductable_input:
   """ Required : 
   tableName
   proposedTaxDeductable
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  """  
      self.proposedTaxDeductable:int = obj["proposedTaxDeductable"]
      """  The proposed tax deductible  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeTaxDeductable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaxFixedAmount_input:
   """ Required : 
   tableName
   proposedFixedAmt
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  """  
      self.proposedFixedAmt:int = obj["proposedFixedAmt"]
      """  The proposed reportable amount  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeTaxFixedAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaxPercent_input:
   """ Required : 
   tableName
   proposedTaxPercent
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  """  
      self.proposedTaxPercent:int = obj["proposedTaxPercent"]
      """  The proposed tax percent  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeTaxPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaxRateCode_input:
   """ Required : 
   tableName
   proposedRateCode
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  """  
      self.proposedRateCode:str = obj["proposedRateCode"]
      """  The proposed rate code  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeTaxRateCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaxReportableAmt_input:
   """ Required : 
   tableName
   proposedReportableAmt
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  """  
      self.proposedReportableAmt:int = obj["proposedReportableAmt"]
      """  The proposed reportable amount  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeTaxReportableAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaxTaxAmt_input:
   """ Required : 
   tableName
   proposedTaxAmt
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  """  
      self.proposedTaxAmt:int = obj["proposedTaxAmt"]
      """  The proposed tax amount  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeTaxTaxAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaxTaxCode_input:
   """ Required : 
   tableName
   proposedTaxCode
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  """  
      self.proposedTaxCode:str = obj["proposedTaxCode"]
      """  The proposed tax code  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeTaxTaxCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaxTaxableAmt_input:
   """ Required : 
   tableName
   proposedTaxableAmt
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  """  
      self.proposedTaxableAmt:int = obj["proposedTaxableAmt"]
      """  The proposed taxable amount  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeTaxTaxableAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTranType_input:
   """ Required : 
   newTranType
   ds
   """  
   def __init__(self, obj):
      self.newTranType:str = obj["newTranType"]
      """  New transaction type  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeTranType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeUOMConfirm_input:
   """ Required : 
   poNum
   poLine
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      pass

class ChangeUOMConfirm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.msg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeUnitPriceConfirmOverride_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeUnitPriceConfirmOverride_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.sConfirmMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeUnitPrice_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeUnitPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendor_input:
   """ Required : 
   VendID
   ds
   """  
   def __init__(self, obj):
      self.VendID:str = obj["VendID"]
      """  Proposed vendor ID to be validated  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangeVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedApproveSwitch_input:
   """ Required : 
   poNum
   ds
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      """  The Purchase Order Number  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangedApproveSwitch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.violationMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangedHeaderTaxManual_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangedHeaderTaxManual_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedTaxManual_input:
   """ Required : 
   tableName
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangedTaxManual_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangingDetailRevisionNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ChangingDetailRevisionNum_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBeforeUpdate_input:
   """ Required : 
   viewName
   ds
   """  
   def __init__(self, obj):
      self.viewName:str = obj["viewName"]
      """  ViewName  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class CheckBeforeUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cOrderChangedMsgText:str = obj["parameters"]
      self.taxableChangedMsgText:str = obj["parameters"]
      self.vendorChangedMsgText:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckComplianceFail_input:
   """ Required : 
   poNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      """  Current PO Number.  """  
      pass

class CheckComplianceFail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.compliant:bool = obj["compliant"]
      pass

      """  output parameters  """  

class CheckForMRPAttributes_input:
   """ Required : 
   poNum
   poLine
   poRelNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      """  PO Number  """  
      self.poLine:int = obj["poLine"]
      """  PO Line  """  
      self.poRelNum:int = obj["poRelNum"]
      """  PO rel num  """  
      pass

class CheckForMRPAttributes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.mrpAttributeMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckLOCWithMessages_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class CheckLOCWithMessages_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.opMessageLimit:str = obj["parameters"]
      self.opMessageShipComplete:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckLOC_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class CheckLOC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMsg:list = obj[any]
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPODetailCNBonded_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class CheckPODetailCNBonded_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPONum_input:
   """ Required : 
   ProposedPONum
   """  
   def __init__(self, obj):
      self.ProposedPONum:int = obj["ProposedPONum"]
      """  The proposed PO Number  """  
      pass

class CheckPONum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opFoundPO:bool = obj["opFoundPO"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckProjectID_input:
   """ Required : 
   ipProjectID
   ds
   """  
   def __init__(self, obj):
      self.ipProjectID:str = obj["ipProjectID"]
      """  The Project ID value  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class CheckProjectID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckRateGrpCode_input:
   """ Required : 
   ipRateGrpCode
   ds
   """  
   def __init__(self, obj):
      self.ipRateGrpCode:str = obj["ipRateGrpCode"]
      """  Currency Rate Group Code  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class CheckRateGrpCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CloseOrderLine_input:
   """ Required : 
   PoNum
   PoLine
   """  
   def __init__(self, obj):
      self.PoNum:int = obj["PoNum"]
      """  The purchase order number  """  
      self.PoLine:int = obj["PoLine"]
      """  The purchase order line  """  
      pass

class CloseOrderLine_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POTableset] = obj["returnObj"]
      pass

class CloseOrder_input:
   """ Required : 
   PoNum
   """  
   def __init__(self, obj):
      self.PoNum:int = obj["PoNum"]
      """  The purchase order number  """  
      pass

class CloseOrder_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POTableset] = obj["returnObj"]
      pass

class CloseRelease_input:
   """ Required : 
   PoNum
   PoLine
   PoRelease
   """  
   def __init__(self, obj):
      self.PoNum:int = obj["PoNum"]
      """  The purchase order number  """  
      self.PoLine:int = obj["PoLine"]
      """  The purchase order line  """  
      self.PoRelease:int = obj["PoRelease"]
      """  The purchase order release number  """  
      pass

class CloseRelease_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   poNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DuplicatePO_input:
   """ Required : 
   poNum
   copyUnitCosts
   copyJobInfo
   getLatestSupplierPrice
   getLatestRevision
   newDueDate
   newPromiseDate
   newBuyerID
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      """  The purchase order number  """  
      self.copyUnitCosts:bool = obj["copyUnitCosts"]
      """  Unit Costs  """  
      self.copyJobInfo:bool = obj["copyJobInfo"]
      """  Job Info  """  
      self.getLatestSupplierPrice:bool = obj["getLatestSupplierPrice"]
      """  Supplier Price List  """  
      self.getLatestRevision:bool = obj["getLatestRevision"]
      """  Latest Revision  """  
      self.newDueDate:str = obj["newDueDate"]
      """  new Due Date  """  
      self.newPromiseDate:str = obj["newPromiseDate"]
      """  new Promise Date  """  
      self.newBuyerID:str = obj["newBuyerID"]
      """  new BuyerID  """  
      pass

class DuplicatePO_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.cJobMTLIssuedComplete:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_PODetailAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PONUM:int = obj["PONUM"]
      self.POLine:int = obj["POLine"]
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

class Erp_Tablesets_PODetailInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PONUM:int = obj["PONUM"]
      """  Purchase order number that the detail line item is linked to.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.PlanSeq:int = obj["PlanSeq"]
      """  A sequence number that uniquely identifies the PartMtlInsp record within the Part material  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID.  Must be valid in the SpecHed table.  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PODetailMiscTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PONUM:int = obj["PONUM"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  ** NOT USED TO BE DROPPED 10.2 **  """  
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
      """  User ID of the user who created the record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date/ time that the record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date/ time that the record was last changed  """  
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
      self.Migrated:bool = obj["Migrated"]
      """  Indicates if this row was created as part of the migration process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Desc. Collection Type  """  
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
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PODetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if this line item is Open/Closed. This is not directly maintainable by the user. Normally it gets set to "Closed" as a result of the receiving process. When there are no longer any open PORel records then the PODetail record is closed. This can also be closed when the user Voids the Order or PODetail record.  """  
      self.VoidLine:bool = obj["VoidLine"]
      """   Indicates if the Line was voided. Voided line items are not maintainable, can't "unvoid".  This field is not directly maintainable.  Instead the void function will be performed via a "Void Line" button.  Which then presents a verification dialog box.
When an PODetail record is 'voided',  all current open  PORel records are also closed and voided.  If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoHeader is voided.  """  
      self.PONUM:int = obj["PONUM"]
      """  Purchase order number that the detail line item is linked to.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  (Our) Unit Of Measure.  """  
      self.UnitCost:int = obj["UnitCost"]
      """   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  The unit price in the vendors unit of measure and currency.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little misleading.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the OrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This insures that Order quantity and scheduled  quantities are always in sync.  """  
      self.XOrderQty:int = obj["XOrderQty"]
      """  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  This ensures that Order quantity and scheduled quantities are always in sync.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Taxable  """  
      self.PUM:str = obj["PUM"]
      """  Purchasing UOM  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal Part number for this item.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier Part Number  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail order line item. These will be printed on the purchase order.  Defaults from the related JobOper, JobMtl or Part file.  """  
      self.ClassID:str = obj["ClassID"]
      """  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.ClassID. The PartClass is used in determining a default G/L expense account.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required when this PO line item is received. Inspection may also be enforced if the related PartClass, Vendor, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is a duplicate of the field in POHeader and is maintained  in the write triggers of POHeader and PODetail.  """  
      self.AdvancePayBal:int = obj["AdvancePayBal"]
      """  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  """  
      self.DocAdvancePayBal:int = obj["DocAdvancePayBal"]
      """  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  """  
      self.Confirmed:bool = obj["Confirmed"]
      """  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  """  
      self.DateChgReq:bool = obj["DateChgReq"]
      """  Indicates this line has a pending date change  """  
      self.QtyChgReq:bool = obj["QtyChgReq"]
      """  Indicates this line has a pending qty change  """  
      self.PartNumChgReq:str = obj["PartNumChgReq"]
      """  Requested pending partnumber change  """  
      self.RevisionNumChgReq:str = obj["RevisionNumChgReq"]
      """  Requested pending revision change  """  
      self.ConfirmDate:str = obj["ConfirmDate"]
      """  Date Supplier Confirmed the PO  """  
      self.ConfirmVia:str = obj["ConfirmVia"]
      """  Can be "web" or "client"  """  
      self.PrcChgReq:int = obj["PrcChgReq"]
      """  Requested Price change.  SRM  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line created for this PO Line for the Inter-Company Trading.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order line.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.ContractActive:bool = obj["ContractActive"]
      """  Is this line active on the Contract Purchase Order?  """  
      self.ContractQty:int = obj["ContractQty"]
      """  Quantity for this Contract Purchase Order Line.  """  
      self.ContractUnitCost:int = obj["ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line.  """  
      self.ContractDocUnitCost:int = obj["ContractDocUnitCost"]
      """  Document Unit Price for this Contract Purchase Order Line.  """  
      self.Rpt1AdvancePayBal:int = obj["Rpt1AdvancePayBal"]
      """  Advanced Payments Balance in Rpt1 currency.  """  
      self.Rpt2AdvancePayBal:int = obj["Rpt2AdvancePayBal"]
      """  Advanced Payments Balance in Rpt2 currency.  """  
      self.Rpt3AdvancePayBal:int = obj["Rpt3AdvancePayBal"]
      """  Advanced Payments Balance in Rpt3 currency.  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt1 currency.  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt2 currency.  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt3 currency.  """  
      self.ContractQtyUOM:str = obj["ContractQtyUOM"]
      """  Unit Of Measure of the ContractQty.  """  
      self.Rpt1ContractUnitCost:int = obj["Rpt1ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt1 currency.  """  
      self.Rpt2ContractUnitCost:int = obj["Rpt2ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt2 currency.  """  
      self.Rpt3ContractUnitCost:int = obj["Rpt3ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt3 currency.  """  
      self.BaseQty:int = obj["BaseQty"]
      """  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PODeltail.XOrderQty to the PODetail.BaseUOM .  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """   Unit of Measure of the PODetail.BaseXOrderQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  """  
      self.BTOOrderNum:int = obj["BTOOrderNum"]
      """  Order Num related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderLine:int = obj["BTOOrderLine"]
      """  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  """  
      self.VendorPartOpts:str = obj["VendorPartOpts"]
      """   Vendor Part Print Options. Determines what is printed.
M = Main Part Reference (Default)
S = Secondary Part Reference
O = Only Part Reference
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  """  
      self.MfgPartOpts:str = obj["MfgPartOpts"]
      """   Mfg Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  """  
      self.SubPartOpts:str = obj["SubPartOpts"]
      """   Substitute Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
M = Main Part Reference
S = Secondary Part Reference  """  
      self.MfgNum:int = obj["MfgNum"]
      """  Manufacturer Unique ID  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  Manufacturer's Part Number.  """  
      self.SubPartNum:str = obj["SubPartNum"]
      """  Substitute Part Number  """  
      self.SubPartType:str = obj["SubPartType"]
      """   Substitute Part Type
O = Original
S = Substitute  """  
      self.ConfigUnitCost:int = obj["ConfigUnitCost"]
      """   Same as Unit cost except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitCost:int = obj["ConfigBaseUnitCost"]
      """  This is the base cost for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.ConvOverRide:bool = obj["ConvOverRide"]
      """  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.Direction:str = obj["Direction"]
      """  Direction  """  
      self.Per:str = obj["Per"]
      """  Per  """  
      self.MaintainPricingUnits:bool = obj["MaintainPricingUnits"]
      """  MaintainPricingUnits  """  
      self.OverrideConversion:bool = obj["OverrideConversion"]
      """  OverrideConversion  """  
      self.RowsManualFactor:bool = obj["RowsManualFactor"]
      """  RowsManualFactor  """  
      self.KeepRowsManualFactorTmp:bool = obj["KeepRowsManualFactorTmp"]
      """  KeepRowsManualFactorTmp  """  
      self.ShipToSupplierDate:str = obj["ShipToSupplierDate"]
      """  ShipToSupplierDate  """  
      self.Factor:int = obj["Factor"]
      """  Factor  """  
      self.PricingQty:int = obj["PricingQty"]
      """  PricingQty  """  
      self.PricingUnitPrice:int = obj["PricingUnitPrice"]
      """  PricingUnitPrice  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.DocPricingUnitPrice:int = obj["DocPricingUnitPrice"]
      """  DocPricingUnitPrice  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the supplier price list has been overriden which will in turn prevent the unit price from being updated when taking into account quantity / price breaks.  """  
      self.QtyOption:str = obj["QtyOption"]
      """  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  """  
      self.OrigComment:str = obj["OrigComment"]
      """  Contains old comments about the detail order line item. This field saves old comments about the detail line that are going to be replaced by new comments.  """  
      self.SmartString:str = obj["SmartString"]
      """  SmartString  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  SmartStringProcessed  """  
      self.DueDate:str = obj["DueDate"]
      """  Specifies the date by which you need to receive the part. If you set the Due Date before create releases, it will act as default value when adding new releases. If you're adding lines from:  - BTO or Drop Shipments, PODetail.DueDate will take the value from OrderRel.NeedByDate. - Job Material , PODetail.DueDate  will take the value from JobMtl.ReqDate. - Subcontract Operations, PODetail.DueDate  wil take the value from JobOper.DueDate  """  
      self.ContractID:str = obj["ContractID"]
      """  The identifier of the planning contract.  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  """  
      self.SelCurrPricingUnitPrice:int = obj["SelCurrPricingUnitPrice"]
      """  SelCurrPricingUnitPrice  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date and time that the record was last changed  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this PO line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True the tax engine will not calculate any miscellaneous charge tax information  """  
      self.InUnitCost:int = obj["InUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in base currency.  """  
      self.DocInUnitCost:int = obj["DocInUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in document currency.  """  
      self.Rpt1InUnitCost:int = obj["Rpt1InUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  """  
      self.Rpt2InUnitCost:int = obj["Rpt2InUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  """  
      self.Rpt3InUnitCost:int = obj["Rpt3InUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  """  
      self.InAdvancePayBal:int = obj["InAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in base currency.  """  
      self.DocInAdvancePayBal:int = obj["DocInAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in document currency.  """  
      self.Rpt1InAdvancePayBal:int = obj["Rpt1InAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in Rpt1 currency.  """  
      self.Rpt2InAdvancePayBal:int = obj["Rpt2InAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in Rpt2 currency.  """  
      self.Rpt3InAdvancePayBal:int = obj["Rpt3InAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in Rpt3 currency.  """  
      self.InContractUnitCost:int = obj["InContractUnitCost"]
      """  Contract unit cost inclusive of tax in base currency.  """  
      self.DocInContractUnitCost:int = obj["DocInContractUnitCost"]
      """  Contract unit cost inclusive of tax in document currency.  """  
      self.Rpt1InContractUnitCost:int = obj["Rpt1InContractUnitCost"]
      """  Contract unit cost inclusive of tax in Rpt1 currency.  """  
      self.Rpt2InContractUnitCost:int = obj["Rpt2InContractUnitCost"]
      """  Contract unit cost inclusive of tax in Rpt2 currency.  """  
      self.Rpt3InContractUnitCost:int = obj["Rpt3InContractUnitCost"]
      """  Contract unit cost inclusive of tax in Rpt3 currency.  """  
      self.DocExtCost:int = obj["DocExtCost"]
      """  Extended cost of the PO Line in document currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.DocUnitCost.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended cost of the PO Line in base currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.UnitCost.  """  
      self.Rpt1ExtCost:int = obj["Rpt1ExtCost"]
      """  Extended cost of the PO Line in Rpt1 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt1UnitCost.  """  
      self.Rpt2ExtCost:int = obj["Rpt2ExtCost"]
      """  Extended cost of the PO Line in Rpt2 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt2UnitCost.  """  
      self.Rpt3ExtCost:int = obj["Rpt3ExtCost"]
      """  Extended cost of the PO Line in Rpt3 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt3UnitCost.  """  
      self.DocMiscCost:int = obj["DocMiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in document currency.  This is the sum of POMisc.DocMiscAmt for all line charges.  """  
      self.MiscCost:int = obj["MiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in base currency.  This is the sum of POMisc.MiscAmt for all line charges.  """  
      self.Rpt1MiscCost:int = obj["Rpt1MiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in Rpt1 currency.  This is the sum of POMisc.Rpt1MiscAmt for all line charges.  """  
      self.Rpt2MiscCost:int = obj["Rpt2MiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in Rpt2 currency.  This is the sum of POMisc.Rpt2MiscAmt for all line charges.  """  
      self.Rpt3MiscCost:int = obj["Rpt3MiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in Rpt3 currency.  This is the sum of POMisc.Rpt3MiscAmt for all line charges.  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Total Tax amount for this PO Line in base currency,  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """  Total Tax amount for this PO Line in document currency.  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """  Total Tax amount for this PO Line in Rpt1 currency,  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """  Total Tax amount for this PO Line in Rpt2 currency,  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """  Total Tax amount for this PO Line in Rpt3 currency,  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in base currency.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in document currency.  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  """  
      self.TotalDedTax:int = obj["TotalDedTax"]
      """  Total deductable tax amount for this PO Line in base currency.  """  
      self.DocTotalDedTax:int = obj["DocTotalDedTax"]
      """  Total deductable tax amount for this PO Line in document currency.  """  
      self.Rpt1TotalDedTax:int = obj["Rpt1TotalDedTax"]
      """  Total deductable tax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt2TotalDedTax:int = obj["Rpt2TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt3TotalDedTax:int = obj["Rpt3TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt3 currency.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  CommodityCode  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  CNBonded  """  
      self.EDIAckCode:str = obj["EDIAckCode"]
      """  Acknowledge code received from EDI  """  
      self.EDIAckComment:str = obj["EDIAckComment"]
      """  Additional comments to send with Acknowledge  """  
      self.AskRefCode:bool = obj["AskRefCode"]
      """  The flag to indicate if the user is supposed to be asked to enter a Reference code before saving a new PoDetail record .  """  
      self.CalcAssemblySeq:int = obj["CalcAssemblySeq"]
      self.CalcDocTotalCost:int = obj["CalcDocTotalCost"]
      self.CalcDueDate:str = obj["CalcDueDate"]
      self.CalcJobNum:str = obj["CalcJobNum"]
      self.CalcJobSeq:int = obj["CalcJobSeq"]
      self.CalcJobSeqType:str = obj["CalcJobSeqType"]
      self.calcLeadTime:int = obj["calcLeadTime"]
      self.CalcMangCustID:str = obj["CalcMangCustID"]
      self.CalcMangCustName:str = obj["CalcMangCustName"]
      self.CalcMangCustNum:int = obj["CalcMangCustNum"]
      self.CalcMfg:str = obj["CalcMfg"]
      self.CalcMfgPart:str = obj["CalcMfgPart"]
      self.calcMinOrderQty:int = obj["calcMinOrderQty"]
      self.CalcOurQty:int = obj["CalcOurQty"]
      self.calcPartPUM:str = obj["calcPartPUM"]
      self.CalcPurchasingFactor:int = obj["CalcPurchasingFactor"]
      """  purchasing factor  """  
      self.CalcPurchasingFactorDirection:str = obj["CalcPurchasingFactorDirection"]
      self.CalcTotalCost:int = obj["CalcTotalCost"]
      self.CalcTranType:str = obj["CalcTranType"]
      self.CalcVendQty:int = obj["CalcVendQty"]
      self.Configured:str = obj["Configured"]
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      self.ContractOrder:bool = obj["ContractOrder"]
      self.CostPerCodeContract:str = obj["CostPerCodeContract"]
      """  Indicates the costing per quantity (When Contract PO). It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.CPFactor:int = obj["CPFactor"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DelPoSug:bool = obj["DelPoSug"]
      self.DisablePartRevBtn:bool = obj["DisablePartRevBtn"]
      self.DispAcctDescription:str = obj["DispAcctDescription"]
      """  Display Account Description.  """  
      self.DispExpAccount:str = obj["DispExpAccount"]
      """  A character string made up of Div, Dept, Chart and Segment values and their related separators concatenated into the full GL account number.  """  
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      self.DocScrUnitCost:int = obj["DocScrUnitCost"]
      self.EnableRcvInspectionReq:bool = obj["EnableRcvInspectionReq"]
      """  False if vendor or class requires inspection, otherwise true.  """  
      self.ExpChart:str = obj["ExpChart"]
      """  The Chart ID component of the default G/L account.  """  
      self.ExpDivision:str = obj["ExpDivision"]
      """  The Division Component of the default expence G/L account.  """  
      self.ExpGLDept:str = obj["ExpGLDept"]
      """  The Department component of the default G/L account.  """  
      self.FromPOSugChg:bool = obj["FromPOSugChg"]
      self.LinkedSOConfig:bool = obj["LinkedSOConfig"]
      self.MultiRel:bool = obj["MultiRel"]
      self.NonMasterPart:bool = obj["NonMasterPart"]
      self.OpCode:str = obj["OpCode"]
      self.PartQtyBearing:bool = obj["PartQtyBearing"]
      self.POHeaderApprove:bool = obj["POHeaderApprove"]
      self.PORelOneOpenRelease:bool = obj["PORelOneOpenRelease"]
      """  True if there is only one release and it's open.  """  
      self.PriceBrkBTNSensitive:bool = obj["PriceBrkBTNSensitive"]
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  Reference Code Description  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Reference Code Status  """  
      self.ReferenceCode:str = obj["ReferenceCode"]
      """  Link to the related code in GlRefCod.RefCode  """  
      self.Rpt1CalcTotalCost:int = obj["Rpt1CalcTotalCost"]
      self.Rpt1ScrUnitCost:int = obj["Rpt1ScrUnitCost"]
      self.Rpt2CalcTotalCost:int = obj["Rpt2CalcTotalCost"]
      self.Rpt2ScrUnitCost:int = obj["Rpt2ScrUnitCost"]
      self.Rpt3CalcTotalCost:int = obj["Rpt3CalcTotalCost"]
      self.Rpt3ScrUnitCost:int = obj["Rpt3ScrUnitCost"]
      self.ScrUnitCost:int = obj["ScrUnitCost"]
      """   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  """  
      self.SetCheveron:bool = obj["SetCheveron"]
      self.SubAvail:bool = obj["SubAvail"]
      self.UpdateRelRecords:bool = obj["UpdateRelRecords"]
      self.UpdateRelTaxable:bool = obj["UpdateRelTaxable"]
      """  Update PO Release Taxable Flag on Change of PO Detail Taxable Flag  """  
      self.VendPurPoint:str = obj["VendPurPoint"]
      """  Purchase Point used in the Supplier Tracker.  """  
      self.AllowPORecon:bool = obj["AllowPORecon"]
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      """  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  """  
      self.AttributeQtyMismatch:bool = obj["AttributeQtyMismatch"]
      """  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  """  
      self.CalcJobMtlSeq:int = obj["CalcJobMtlSeq"]
      self.CalcJobOprSeq:int = obj["CalcJobOprSeq"]
      self.HasBuyToOrderRelease:bool = obj["HasBuyToOrderRelease"]
      """  Flag to indicate the current PO Line has at least one Buy To Order Release  """  
      self.LineAmtCalcd:bool = obj["LineAmtCalcd"]
      """  The flag to indicate if PO  doc/base/rpt line amounts are recalculated  whne entered and no need to recalculate on save.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClassInactive:bool = obj["ClassInactive"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.GlPurchPurchDesc:str = obj["GlPurchPurchDesc"]
      self.MfgNumMfgID:str = obj["MfgNumMfgID"]
      self.MfgNumName:str = obj["MfgNumName"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PONUMCurrencyCode:str = obj["PONUMCurrencyCode"]
      self.PONUMOrderDate:str = obj["PONUMOrderDate"]
      self.PONUMInPrice:bool = obj["PONUMInPrice"]
      self.PONUMShipName:str = obj["PONUMShipName"]
      self.PONUMShipToConName:str = obj["PONUMShipToConName"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.DeliveryInstructions_c:str = obj["DeliveryInstructions_c"]
      pass

class Erp_Tablesets_PODetailTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of PODetail record  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  Reportable Amount  """  
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
      """  User ID of the user who created the record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date / time that the record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date/ time that the record was last changed  """  
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
      """  ResolutionNum  """  
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
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
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
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POHeadMiscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that this miscellaneous record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when they requested miscellaneous maintenance.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. This will be printed on the PO. The default is provided by PurMisc.Description, but it is overridable by the user. This can't be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The Customer Currency amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Sets the miscellaneous line as being taxable. This is used to pass along to invoice processing.  """  
      self.InvoicedAmt:int = obj["InvoicedAmt"]
      """  Amount invoiced against this POMisc record. This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  """  
      self.DocInvoicedAmt:int = obj["DocInvoicedAmt"]
      """  Amount invoiced against this POMisc record(Customer Currency). This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line created for this PO Line for the Inter-Company Trading.  """  
      self.OrderSeqNum:int = obj["OrderSeqNum"]
      """  Order Misc Seq Num created for this PO Misc Seq Num for the Inter-Company Trading.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order misc charge.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.Rpt1InvoicedAmt:int = obj["Rpt1InvoicedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoicedAmt:int = obj["Rpt2InvoicedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoicedAmt:int = obj["Rpt3InvoicedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InMiscAmt:int = obj["InMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.DocInMiscAmt:int = obj["DocInMiscAmt"]
      """  The Customer Currency amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.Rpt1InMiscAmt:int = obj["Rpt1InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InMiscAmt:int = obj["Rpt2InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InMiscAmt:int = obj["Rpt3InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.InInvoiceAmt:int = obj["InInvoiceAmt"]
      """  Amount invoiced against this POMisc record. This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  """  
      self.DocInInvoiceAmt:int = obj["DocInInvoiceAmt"]
      """  Amount invoiced against this POMisc record(Customer Currency). This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  """  
      self.Rpt1InInvoiceAmt:int = obj["Rpt1InInvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InInvoiceAmt:int = obj["Rpt2InInvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InInvoiceAmt:int = obj["Rpt3InInvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True the tax engine will not calculate any miscellaneous charge tax information  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrencySymbol:str = obj["CurrencySymbol"]
      self.DocCurrencySymbol:str = obj["DocCurrencySymbol"]
      self.POHeaderApprove:bool = obj["POHeaderApprove"]
      self.Rpt1ScrMiscAmt:int = obj["Rpt1ScrMiscAmt"]
      self.Rpt2ScrMiscAmt:int = obj["Rpt2ScrMiscAmt"]
      self.Rpt3ScrMiscAmt:int = obj["Rpt3ScrMiscAmt"]
      self.ScrDocMiscAmt:int = obj["ScrDocMiscAmt"]
      self.ScrMiscAmt:int = obj["ScrMiscAmt"]
      self.TaxIDDescription:str = obj["TaxIDDescription"]
      """  Description of Tax ID  """  
      self.DocTotalDedTax:int = obj["DocTotalDedTax"]
      """  Total deductable tax amount for this PO Line in document currency.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in document currency.  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """  Total Tax amount for this PO Line in document currency.  """  
      self.Rpt1TotalDedTax:int = obj["Rpt1TotalDedTax"]
      """  Total deductable tax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """  Total Tax amount for this PO Line in Rpt1 currency,  """  
      self.Rpt2TotalDedTax:int = obj["Rpt2TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """  Total Tax amount for this PO Line in Rpt2 currency,  """  
      self.Rpt3TotalDedTax:int = obj["Rpt3TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt3 currency.  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """  Total Tax amount for this PO Line in Rpt3 currency,  """  
      self.TotalDedTax:int = obj["TotalDedTax"]
      """  Total deductable tax amount for this PO Line in base currency.  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in base currency.  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Total Tax amount for this PO Line in base currency,  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeTaxCatID:str = obj["MiscCodeTaxCatID"]
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.PONumInPrice:bool = obj["PONumInPrice"]
      self.PONumShipToConName:str = obj["PONumShipToConName"]
      self.PONumShipName:str = obj["PONumShipName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POHeaderAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PONum:int = obj["PONum"]
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

class Erp_Tablesets_POHeaderListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if the order is open or closed. This is set automatically when all the PODetail records have been closed or can be set if the user Voids the Order. This field is not directly maintainable.  """  
      self.VoidOrder:bool = obj["VoidOrder"]
      """  Indicates if the entire remaining Purchase Order is Voided. When an order is voided the POHeader.OpenOrder is set to No and all remaining PODetail and PORel records for the related order are closed and voided.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Order Date for this purchase order. Initially defaults as "today", then defaults as last date entered in this session.  """  
      self.FOB:str = obj["FOB"]
      """  Incoterms  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Ship Via Code  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms  """  
      self.ShipName:str = obj["ShipName"]
      """  defaults from the company file.  """  
      self.ShipAddress1:str = obj["ShipAddress1"]
      """  First adress line  """  
      self.ShipAddress2:str = obj["ShipAddress2"]
      """  Second address line  """  
      self.ShipAddress3:str = obj["ShipAddress3"]
      """  Third address line  """  
      self.ShipCity:str = obj["ShipCity"]
      """  City portion of the address  """  
      self.ShipState:str = obj["ShipState"]
      """  Statee portion of the address  """  
      self.ShipCountry:str = obj["ShipCountry"]
      """  Country is used as part of the Ship to  address. It can be left blank.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID that links to the Purchasing Agent master file.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  """  
      self.ShipToConName:str = obj["ShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.ReadyToPrint:bool = obj["ReadyToPrint"]
      """  Indicates if the PO can be printed. Print functions are not available if this is = No.  """  
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorName:str = obj["VendorName"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  System date that the PO was approved.  This only pertains to PO which exceeded the buyers limit and have been approved.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  The BuyerID  that approved the PO. (See ApprovedDate for related info)  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.Approve:bool = obj["Approve"]
      """   Inidicates if the PO is "ready" to be approved.  This is checked  when all the information is complete and is ready to be processed. When checked the system will test if PO has exceeded the buyers or system purchasing limit.  (See ApprovalStatus for related info)
When Approve = yes the PO cannot be maintained.  """  
      self.ApprovalStatus:str = obj["ApprovalStatus"]
      """   Indicates the approval status of the PO.
Valid values are; U - Unsubmitted for Approval,  P - Pending Approval, A - Approved, R - Rejected.  Before a PO can be printed it must be approved.  A PO is consider  approved if it doesn't exceed the buyers limit or it has been approved by the approver.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.POType:str = obj["POType"]
      """  PO Type Identifier ('STD' - standard PO, 'CMI' - Customer managed inventory PO, or 'SMI' - Supplier managed inventory PO)  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POHeaderListTableset:
   def __init__(self, obj):
      self.POHeaderList:list[Erp_Tablesets_POHeaderListRow] = obj["POHeaderList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_POHeaderMiscTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number  """  
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
      """  User ID o fthe user who created the record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date / time that the record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date/ time that the record was last changed  """  
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
      self.Migrated:bool = obj["Migrated"]
      """  Indicates if this row was created as part of the migration process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
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
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if the order is open or closed. This is set automatically when all the PODetail records have been closed or can be set if the user Voids the Order. This field is not directly maintainable.  """  
      self.VoidOrder:bool = obj["VoidOrder"]
      """  Indicates if the entire remaining Purchase Order is Voided. When an order is voided the POHeader.OpenOrder is set to No and all remaining PODetail and PORel records for the related order are closed and voided.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Order Date for this purchase order. Initially defaults as "today", then defaults as last date entered in this session.  """  
      self.FOB:str = obj["FOB"]
      """  Incoterms  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Ship Via Code  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms  """  
      self.ShipName:str = obj["ShipName"]
      """  defaults from the company file.  """  
      self.ShipAddress1:str = obj["ShipAddress1"]
      """  First adress line  """  
      self.ShipAddress2:str = obj["ShipAddress2"]
      """  Second address line  """  
      self.ShipAddress3:str = obj["ShipAddress3"]
      """  Third address line  """  
      self.ShipCity:str = obj["ShipCity"]
      """  City portion of the address  """  
      self.ShipState:str = obj["ShipState"]
      """  Statee portion of the address  """  
      self.ShipZIP:str = obj["ShipZIP"]
      """  Postal code or Zip code portion of the address  """  
      self.ShipCountry:str = obj["ShipCountry"]
      """  Country is used as part of the Ship to  address. It can be left blank.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID that links to the Purchasing Agent master file.  """  
      self.FreightPP:bool = obj["FreightPP"]
      """  The freight charge is to be paid by the vendor.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the VendCnt  table. Use the Vendor.PRIMPCON as the default. or the VendorPP.PrimPCon if a vendor purchase point is referenced.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about over all  purchase order. These will be printed on the purchase order.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  """  
      self.ShipToConName:str = obj["ShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.ReadyToPrint:bool = obj["ReadyToPrint"]
      """  Indicates if the PO can be printed. Print functions are not available if this is = No.  """  
      self.PrintAs:str = obj["PrintAs"]
      """  N = New, C = Change Order  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.ShipCountryNum:int = obj["ShipCountryNum"]
      """  Country part of address. This field is in sync with the Country field. Must be a valid entry in the Country table.  """  
      self.LogChanges:bool = obj["LogChanges"]
      """  This field indicates if the system should generate purchase order booking records. Booking tables are used to track changes to POheader.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  System date that the PO was approved.  This only pertains to PO which exceeded the buyers limit and have been approved.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  The BuyerID  that approved the PO. (See ApprovedDate for related info)  """  
      self.Approve:bool = obj["Approve"]
      """   Inidicates if the PO is "ready" to be approved.  This is checked  when all the information is complete and is ready to be processed. When checked the system will test if PO has exceeded the buyers or system purchasing limit.  (See ApprovalStatus for related info)
When Approve = yes the PO cannot be maintained.  """  
      self.ApprovalStatus:str = obj["ApprovalStatus"]
      """   Indicates the approval status of the PO.
Valid values are; U - Unsubmitted for Approval,  P - Pending Approval, A - Approved, R - Rejected.  Before a PO can be printed it must be approved.  A PO is consider  approved if it doesn't exceed the buyers limit or it has been approved by the approver.  """  
      self.ApprovedAmount:int = obj["ApprovedAmount"]
      """   An internally used field that represents the total amount of the PO (in base currency) captured the last time the po was approved/rejected.  Note: this only pertains to PO that required approval in the first place otherwise it's zero.  The limit checking process will compare PO amounts to the greater of the buyers limit or this amount. Basically, if the PO was already approved once for a specific amount then it should not require subsequent approval until that amount is exceeded.
Note: This also contains the PO amount if it was rejected. In this case, the PO remains as rejected until they reduce the PO amount.  """  
      self.PostToWeb:bool = obj["PostToWeb"]
      """  Indicates the Supplier will respond via Suppliers workbench  """  
      self.PostDate:str = obj["PostDate"]
      """  Date Buyer posted the PO  """  
      self.VendorRefNum:str = obj["VendorRefNum"]
      """  Vendor reference number.  """  
      self.ConfirmReq:bool = obj["ConfirmReq"]
      """  Indicated this PO requires a confirmation.  This would default yes for any Web Vendor  """  
      self.Confirmed:bool = obj["Confirmed"]
      """  Indicated Supplier Confirmed the PO  """  
      self.ConfirmVia:str = obj["ConfirmVia"]
      """   Indicates if the Supplier has confirmed that they intend to fill the Order, and that it will be done through Supplier Connect("web"), 
phoned in a confirmation and clicked on the Confirmed checkbox in Epicor ("client"), or they clicked on the "Reject" checkbox in Supplier Connect("rejected").  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.XRefPONum:str = obj["XRefPONum"]
      """  Cross reference PO number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      """  Consolidated PO flag.  Used in Consolidated Purchasing.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.ContractOrder:bool = obj["ContractOrder"]
      """  Is this Purchase Order a Contract Purchase Order?  """  
      self.ContractStartDate:str = obj["ContractStartDate"]
      """  The date the Contract Purchase Order is active.  """  
      self.ContractEndDate:str = obj["ContractEndDate"]
      """  The date the Contract Purchase Order expires.  """  
      self.PrintHeaderAddress:bool = obj["PrintHeaderAddress"]
      """  Print Header Address flag  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.POType:str = obj["POType"]
      """  PO Type Identifier ('STD' - standard PO, 'CMI' - Customer managed inventory PO, or 'SMI' - Supplier managed inventory PO)  """  
      self.APLOCID:str = obj["APLOCID"]
      """  Letter of Credit ID.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document for the record.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.ICPOLocked:bool = obj["ICPOLocked"]
      """  ICPOLocked  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DueDate:str = obj["DueDate"]
      """  Specifies the date by which you need to receive the whole Purchase Order. If you set the Due Date before create lines and releases, it will act as a default value when adding new lines/releases.  """  
      self.PromiseDate:str = obj["PromiseDate"]
      """  Specifies the date on which the supplier has promised to ship the whole Purchase Order. If you set the Promise Date before create lines and releases, it will act as a default value when adding releases.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date and time that the record was last changed.  """  
      self.POTaxReadyToProcess:bool = obj["POTaxReadyToProcess"]
      """  Flag to determine whether PO taxes will be automatically calculated each time a PO line is updated.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Liability for this Purchase Order  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Total Tax amount for this PO in base currency, Totals the TaxAmt from the POTax records of this purchase order  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """  Total Tax amount for this PO in document currency, Totals the DocTaxAmt from the POTax records of this purchase order  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """  Total Tax amount for this PO in Rpt1 currency, Totals the Rpt1TaxAmt from the POTax records of this purchase order  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """  Total Tax amount for this PO in Rpt2 currency, Totals the Rpt2TaxAmt from the POTax records of this purchase order  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """  Total Tax amount for this PO in Rpt3 currency, Totals the Rpt3TaxAmt from the POTax records of this purchase order  """  
      self.TotalWhTax:int = obj["TotalWhTax"]
      """  Total Order Withholding Taxes in base currency  """  
      self.DocTotalWhTax:int = obj["DocTotalWhTax"]
      """  Total Order Withholding Taxes in document currency  """  
      self.Rpt1TotalWhTax:int = obj["Rpt1TotalWhTax"]
      """  Total Order Withholding Taxes in Rpt1 currency  """  
      self.Rpt2TotalWhTax:int = obj["Rpt2TotalWhTax"]
      """  Total Order Withholding Taxes in Rpt2 currency  """  
      self.Rpt3TotalWhTax:int = obj["Rpt3TotalWhTax"]
      """  Total Order Withholding Taxes in Rpt3 currency  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Order Self Assessed Taxes in base currency.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Order Self Assessed Taxes in document currency.  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Order Self Assessed Taxes in Rpt1 currency.  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Order Self Assessed Taxes in Rpt2 currency.  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Order Self Assessed Taxes in Rpt3 currency.  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.HdrTaxNoUpdt:bool = obj["HdrTaxNoUpdt"]
      """  This flag determines whether any manual taxes were created for a header miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code - FUTUREUSE  """  
      self.TotalDedTax:int = obj["TotalDedTax"]
      """  Total deductable tax amount in base currency.  """  
      self.DocTotalDedTax:int = obj["DocTotalDedTax"]
      """  Total deductable tax amount in document currency.  """  
      self.Rpt1TotalDedTax:int = obj["Rpt1TotalDedTax"]
      """  Total deductable tax amount in Rpt1 currency.  """  
      self.Rpt2TotalDedTax:int = obj["Rpt2TotalDedTax"]
      """  Total deductable tax amount in Rpt2 currency.  """  
      self.Rpt3TotalDedTax:int = obj["Rpt3TotalDedTax"]
      """  Total deductable tax amount in Rpt3 currency.  """  
      self.TotalCharges:int = obj["TotalCharges"]
      """  Total charge amount for the PO in base currency,  This is the sum of PODetail.ExtCost for non voided lines.  """  
      self.TotalMiscCharges:int = obj["TotalMiscCharges"]
      """  Total amount for all miscellaneous charges associated to this PO in base currency.  This is the sum of POMisc.MiscAmt.  """  
      self.TotalOrder:int = obj["TotalOrder"]
      """  Total amount for the PO in base currency.  This is the sum of POMisc.MiscAmt + PODetail.ExtCost + POHeader.TotalTax.  """  
      self.DocTotalCharges:int = obj["DocTotalCharges"]
      """  Total charge amount for the PO in document currency,  This is the sum of PODetail.DocExtCost for non voided lines.  """  
      self.DocTotalMisc:int = obj["DocTotalMisc"]
      """  Total amount for all miscellaneous charges associated to this PO in document currency.  This is the sum of POMisc.DocMiscAmt.  """  
      self.DocTotalOrder:int = obj["DocTotalOrder"]
      """  Total amount for the PO in document currency.  This is the sum of POMisc.DocMiscAmt + PODetail.DocExtCost + POHeader.DocTotalTax.  """  
      self.Rpt1TotalCharges:int = obj["Rpt1TotalCharges"]
      """  Total charge amount for the PO in Rpt1 currency,  This is the sum of PODetail.Rpt1ExtCost for non voided lines.  """  
      self.Rpt2TotalCharges:int = obj["Rpt2TotalCharges"]
      """  Total charge amount for the PO in Rpt2 currency,  This is the sum of PODetail.Rpt2ExtCost for non voided lines.  """  
      self.Rpt3TotalCharges:int = obj["Rpt3TotalCharges"]
      """  Total charge amount for the PO in Rpt3 currency,  This is the sum of PODetail.Rpt3ExtCost for non voided lines.  """  
      self.Rpt1TotalMiscCharges:int = obj["Rpt1TotalMiscCharges"]
      """  Total amount for all miscellaneous charges associated to this PO in Rpt1 currency.  This is the sum of POMisc.Rpt1MiscAmt.  """  
      self.Rpt2TotalMiscCharges:int = obj["Rpt2TotalMiscCharges"]
      """  Total amount for all miscellaneous charges associated to this PO in Rpt2 currency.  This is the sum of POMisc.Rpt2MiscAmt.  """  
      self.Rpt3TotalMiscCharges:int = obj["Rpt3TotalMiscCharges"]
      """  Total amount for all miscellaneous charges associated to this PO in Rpt3 currency.  This is the sum of POMisc.Rpt3MiscAmt.  """  
      self.Rpt1TotalOrder:int = obj["Rpt1TotalOrder"]
      """  Total amount for the PO in Rpt1 currency.  This is the sum of POMisc.Rpt1MiscAmt + PODetail.Rpt1ExtCost + POHeader.Rpt1TotalTax.  """  
      self.Rpt2TotalOrder:int = obj["Rpt2TotalOrder"]
      """  Total amount for the PO in Rpt2 currency.  This is the sum of POMisc.Rpt2MiscAmt + PODetail.Rpt2ExtCost + POHeader.Rpt2TotalTax.  """  
      self.Rpt3TotalOrder:int = obj["Rpt3TotalOrder"]
      """  Total amount for the PO in Rpt3 currency.  This is the sum of POMisc.Rpt3MiscAmt + PODetail.Rpt3ExtCost + POHeader.Rpt3TotalTax.  """  
      self.APTaxRoundOption:int = obj["APTaxRoundOption"]
      """  APTaxRoundOption  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  CNBonded  """  
      self.EDIRevNum:int = obj["EDIRevNum"]
      """  EDI Revision number that marks changes in the purchase order since the last time the purchase order was sent.  """  
      self.EDIPosted:bool = obj["EDIPosted"]
      """  Flag used to mark the Purchase Order as posted to EDI  """  
      self.EDIPostedDate:str = obj["EDIPostedDate"]
      """  Date when the PO was last acknowledge from EDI Portal  """  
      self.EDIAckDate:str = obj["EDIAckDate"]
      """  Date when the PO was last acknowledge from EDI Portal  """  
      self.ApproveMessage:str = obj["ApproveMessage"]
      """  Temporarily stores the return message from the PO approval process  """  
      self.RecalcUnitCosts:bool = obj["RecalcUnitCosts"]
      """  Used when switching the Vendor and need to prompt if the user wants to recalculate unit costs.  """  
      self.RuleCode:int = obj["RuleCode"]
      self.UpdateDtlAndRelRecords:bool = obj["UpdateDtlAndRelRecords"]
      self.VendCntFaxNum:str = obj["VendCntFaxNum"]
      self.VendCntPhoneNumber:str = obj["VendCntPhoneNumber"]
      self.ApproveChkBxSensitive:bool = obj["ApproveChkBxSensitive"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.ConfirmChkBxSensitive:bool = obj["ConfirmChkBxSensitive"]
      self.EnableSupplierID:bool = obj["EnableSupplierID"]
      """  Flag for UI to know when to Enable/Disable the SupplierID field in POEntry  """  
      self.HasLines:bool = obj["HasLines"]
      """  True is there are lines for this PO  """  
      self.HoldChkBxSensitive:bool = obj["HoldChkBxSensitive"]
      self.MassPrntChkBxSensitive:bool = obj["MassPrntChkBxSensitive"]
      self.RefCodeCurrSymbol:str = obj["RefCodeCurrSymbol"]
      self.VendAddrFormat:str = obj["VendAddrFormat"]
      """  The formatted vendor address  """  
      self.EDIEnable:bool = obj["EDIEnable"]
      self.BitFlag:int = obj["BitFlag"]
      self.APLOCDescription:str = obj["APLOCDescription"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.ShipCountryNumDescription:str = obj["ShipCountryNumDescription"]
      self.ShipViaCodeInactive:bool = obj["ShipViaCodeInactive"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorName:str = obj["VendorName"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorState:str = obj["VendorState"]
      self.VendorEDISupplier:bool = obj["VendorEDISupplier"]
      self.VendorCntName:str = obj["VendorCntName"]
      self.VendorCntEmailAddress:str = obj["VendorCntEmailAddress"]
      self.VendorCntPhoneNum:str = obj["VendorCntPhoneNum"]
      self.VendorCntFaxNum:str = obj["VendorCntFaxNum"]
      self.VendorPPAddress3:str = obj["VendorPPAddress3"]
      self.VendorPPCountry:str = obj["VendorPPCountry"]
      self.VendorPPZip:str = obj["VendorPPZip"]
      self.VendorPPState:str = obj["VendorPPState"]
      self.VendorPPAddress1:str = obj["VendorPPAddress1"]
      self.VendorPPName:str = obj["VendorPPName"]
      self.VendorPPPrimPCon:int = obj["VendorPPPrimPCon"]
      self.VendorPPAddress2:str = obj["VendorPPAddress2"]
      self.VendorPPCity:str = obj["VendorPPCity"]
      self.XbSystAllowLinkedPOChg:bool = obj["XbSystAllowLinkedPOChg"]
      self.XbSystPOUserInt2Label:str = obj["XbSystPOUserInt2Label"]
      self.XbSystPOUserDate3Label:str = obj["XbSystPOUserDate3Label"]
      self.XbSystPOUserChar3Label:str = obj["XbSystPOUserChar3Label"]
      self.XbSystPOUserChar4Label:str = obj["XbSystPOUserChar4Label"]
      self.XbSystPOUserChar2Label:str = obj["XbSystPOUserChar2Label"]
      self.XbSystPOUserDate2Label:str = obj["XbSystPOUserDate2Label"]
      self.XbSystPOUserInt1Label:str = obj["XbSystPOUserInt1Label"]
      self.XbSystPOUserDec1Label:str = obj["XbSystPOUserDec1Label"]
      self.XbSystPOUserDec2Label:str = obj["XbSystPOUserDec2Label"]
      self.XbSystPOUserDate4Label:str = obj["XbSystPOUserDate4Label"]
      self.XbSystPOUserDate1Label:str = obj["XbSystPOUserDate1Label"]
      self.XbSystPOUserChar1Label:str = obj["XbSystPOUserChar1Label"]
      self.XbSystDisableOverridePriceListOption:bool = obj["XbSystDisableOverridePriceListOption"]
      self.XbSystPOTaxCalculate:bool = obj["XbSystPOTaxCalculate"]
      self.XbSystAPTaxLnLevel:bool = obj["XbSystAPTaxLnLevel"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.PrePaymentFlag_c:bool = obj["PrePaymentFlag_c"]
      self.PrePaymentTerms_c:str = obj["PrePaymentTerms_c"]
      self.ProductFamily_c:str = obj["ProductFamily_c"]
      self.VendorConfirmationNo_c:str = obj["VendorConfirmationNo_c"]
      self.POTerms_c:str = obj["POTerms_c"]
      pass

class Erp_Tablesets_POHeaderTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order.  """  
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
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last changed (seconds since midnight)  """  
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
      self.ScrDedTaxAmt:int = obj["ScrDedTaxAmt"]
      self.ScrDocDedTaxAmt:int = obj["ScrDocDedTaxAmt"]
      self.ScrDocFixedAmount:int = obj["ScrDocFixedAmount"]
      """  Doc Fixed Amount  """  
      self.ScrDocReportableAmt:int = obj["ScrDocReportableAmt"]
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

class Erp_Tablesets_POMiscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that this miscellaneous record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when they requested miscellaneous maintenance.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. This will be printed on the PO. The default is provided by PurMisc.Description, but it is overridable by the user. This can't be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The Customer Currency amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Sets the miscellaneous line as being taxable. This is used to pass along to invoice processing.  """  
      self.InvoicedAmt:int = obj["InvoicedAmt"]
      """  Amount invoiced against this POMisc record. This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  """  
      self.DocInvoicedAmt:int = obj["DocInvoicedAmt"]
      """  Amount invoiced against this POMisc record(Customer Currency). This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line created for this PO Line for the Inter-Company Trading.  """  
      self.OrderSeqNum:int = obj["OrderSeqNum"]
      """  Order Misc Seq Num created for this PO Misc Seq Num for the Inter-Company Trading.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order misc charge.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.Rpt1InvoicedAmt:int = obj["Rpt1InvoicedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoicedAmt:int = obj["Rpt2InvoicedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoicedAmt:int = obj["Rpt3InvoicedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InMiscAmt:int = obj["InMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.DocInMiscAmt:int = obj["DocInMiscAmt"]
      """  The Customer Currency amount of the Miscellaneous Charge/Credit. Can't be zero.  """  
      self.Rpt1InMiscAmt:int = obj["Rpt1InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InMiscAmt:int = obj["Rpt2InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InMiscAmt:int = obj["Rpt3InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.InInvoiceAmt:int = obj["InInvoiceAmt"]
      """  Amount invoiced against this POMisc record. This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  """  
      self.DocInInvoiceAmt:int = obj["DocInInvoiceAmt"]
      """  Amount invoiced against this POMisc record(Customer Currency). This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  """  
      self.Rpt1InInvoiceAmt:int = obj["Rpt1InInvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InInvoiceAmt:int = obj["Rpt2InInvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InInvoiceAmt:int = obj["Rpt3InInvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True the tax engine will not calculate any miscellaneous charge tax information  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrencySymbol:str = obj["CurrencySymbol"]
      self.DocCurrencySymbol:str = obj["DocCurrencySymbol"]
      self.POHeaderApprove:bool = obj["POHeaderApprove"]
      self.Rpt1ScrMiscAmt:int = obj["Rpt1ScrMiscAmt"]
      self.Rpt2ScrMiscAmt:int = obj["Rpt2ScrMiscAmt"]
      self.Rpt3ScrMiscAmt:int = obj["Rpt3ScrMiscAmt"]
      self.ScrDocMiscAmt:int = obj["ScrDocMiscAmt"]
      self.ScrMiscAmt:int = obj["ScrMiscAmt"]
      self.TaxIDDescription:str = obj["TaxIDDescription"]
      """  Description of Tax ID  """  
      self.DocTotalDedTax:int = obj["DocTotalDedTax"]
      """  Total deductable tax amount for this PO Line in document currency.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in document currency.  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """  Total Tax amount for this PO Line in document currency.  """  
      self.Rpt1TotalDedTax:int = obj["Rpt1TotalDedTax"]
      """  Total deductable tax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """  Total Tax amount for this PO Line in Rpt1 currency,  """  
      self.Rpt2TotalDedTax:int = obj["Rpt2TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """  Total Tax amount for this PO Line in Rpt2 currency,  """  
      self.Rpt3TotalDedTax:int = obj["Rpt3TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt3 currency.  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """  Total Tax amount for this PO Line in Rpt3 currency,  """  
      self.TotalDedTax:int = obj["TotalDedTax"]
      """  Total deductable tax amount for this PO Line in base currency.  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in base currency.  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Total Tax amount for this PO Line in base currency,  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      self.MiscCodeTaxCatID:str = obj["MiscCodeTaxCatID"]
      self.PONumInPrice:bool = obj["PONumInPrice"]
      self.PONumShipName:str = obj["PONumShipName"]
      self.PONumShipToConName:str = obj["PONumShipToConName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POReceiptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ContainerID:int = obj["ContainerID"]
      self.ContainerLCAmt:int = obj["ContainerLCAmt"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DropShip:bool = obj["DropShip"]
      self.DueDate:str = obj["DueDate"]
      self.IUM:str = obj["IUM"]
      self.LCFlag:bool = obj["LCFlag"]
      self.Ontime:str = obj["Ontime"]
      self.OpenRelease:bool = obj["OpenRelease"]
      self.OurRemQty:int = obj["OurRemQty"]
      self.PackLine:int = obj["PackLine"]
      self.PackSlip:str = obj["PackSlip"]
      self.PartNum:str = obj["PartNum"]
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
      self.PUM:str = obj["PUM"]
      self.PurPoint:str = obj["PurPoint"]
      self.ReceiptDate:str = obj["ReceiptDate"]
      self.RemainingSMIQty:int = obj["RemainingSMIQty"]
      self.VendorNum:int = obj["VendorNum"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VenRemQty:int = obj["VenRemQty"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.OurQty:int = obj["OurQty"]
      self.Invoiced:bool = obj["Invoiced"]
      self.Volume:int = obj["Volume"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.InvoiceLine:int = obj["InvoiceLine"]
      self.VenPartNum:str = obj["VenPartNum"]
      self.VendorQty:int = obj["VendorQty"]
      self.OurUnitCost:int = obj["OurUnitCost"]
      self.LCSpecLineDutyAmt:int = obj["LCSpecLineDutyAmt"]
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      self.LCUpliftIndCost:int = obj["LCUpliftIndCost"]
      self.LCAmt:int = obj["LCAmt"]
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      self.LCMtlBurUnitCost:int = obj["LCMtlBurUnitCost"]
      self.ArrivedDate:str = obj["ArrivedDate"]
      self.DocVendorUnitCost:int = obj["DocVendorUnitCost"]
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.ThisTranUOM:str = obj["ThisTranUOM"]
      self.EnableInventoryAttributes:bool = obj["EnableInventoryAttributes"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POReceiptsTableset:
   def __init__(self, obj):
      self.POReceipts:list[Erp_Tablesets_POReceiptsRow] = obj["POReceipts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PORelAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
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

class Erp_Tablesets_PORelRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenRelease:bool = obj["OpenRelease"]
      """  Indicates if this release is open.  This is normally closed via the receiving program. But can be changed indirectly  by the user during order entry when they "Void" the release..  """  
      self.VoidRelease:bool = obj["VoidRelease"]
      """   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.
When an PORel record is 'voided',  PORel.OpenRelease is set to "no".  If no other open PORel records exist for the related PODetail then the PoDetail.OpenLine is set to "No". If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoDetail or PoHeader is voided.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.DueDate:str = obj["DueDate"]
      """  Specifies the date by which you need to receive a release of a part. This date is taken from the Purchase Order Line Due Date, if it’s null, PORel.DueDate will take the value from POHeader.DueDate. If you're adding releases from: - BTO or Drop Shipments, PORel.DueDate will take the value from OrderRel.NeedByDate  - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  """  
      self.XRelQty:int = obj["XRelQty"]
      """  Order quantity for this release in our unit of measure.  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Vice-Versa.
Formula: XRelQty * Factor = RelQty  """  
      self.RelQty:int = obj["RelQty"]
      """  Order quantity for this release in vendors unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  This is populated for Purchase Direct items only and contains the job number for the purchased direct item.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  This is populated for Purchase Direct items only and contains the assembly number for the purchased direct item.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.
FYI: This field can indirectly sets the TranType field via the write trigger. It can itself be set from the TranType. System keeps them compatible. JobSeqType/TranType values are; M = PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN. This possibly could have been deleted. However we decided to keep it for backward compatablity reasons.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that the item on this release is being purchased for.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Total quantity received to stock to date. In Purchasing unit of measure. This is a field maintained by the receipt process.  """  
      self.ExpOverride:bool = obj["ExpOverride"]
      """  Indicates if the user overrode the default  expense accounts for this release. This field prevents the program from resetting the account #'s when the user changes other fields that trigger new default accounts to be set. If "Yes" then the defaults will not be used.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition which generated this PORel record.  """  
      self.ReqLine:int = obj["ReqLine"]
      """  Requisition line which generated this PORel record.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PromiseDt:str = obj["PromiseDt"]
      """  Specifies the date on which the supplier has promised to ship this release.This date is taken from POHeader.PromiseDate. If you're adding releases from: - BTO or Drop Shipments, PORel.PromiseDt will take the value from OrderRel.NeedByDate. - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.Confirmed:bool = obj["Confirmed"]
      """  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  """  
      self.ConfirmVia:str = obj["ConfirmVia"]
      """  Can be "web", "client", or "rejected"  """  
      self.ReqChgDate:str = obj["ReqChgDate"]
      """   When the Due Date is changed, this is the previous DueDate.
(originally was "Requested pending date change")  """  
      self.ReqChgQty:int = obj["ReqChgQty"]
      """   When the RelQty is changed, this is the previous RelQty.
(was "Requested change quantity")  """  
      self.LockRel:str = obj["LockRel"]
      """  OBSOLETE FIELD-A PO release with a locked status will not generate a change suggestion.  SEV, 11/21/02: New convention to indicate who is blocking new suggestions: the presence of "B" indicates the Buyer, and "V" indicates the Vendor.  "BV" means both Buyer and Vendor want no changes in Date or Qty on this release.  """  
      self.RefDisplayAccount:str = obj["RefDisplayAccount"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!, REPLACED BY ADDING INDIVIDUAL COMPONENT FIELDS) A character string made up of Division, GLDept and Chart fields concatenated using the user defined configuration options found in XaSyst file.  This should be formatted exactly how the user expects to see their account numbers (including separators).  This field is generated via the maintenance program.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line created for this PO Line for the Inter-Company Trading.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order Release Line created for this PO Release for the Inter-Company Trading.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order release.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  Total quantity shipped but not received (In-Transit).  In Purchasing unit of measure.  This is a summary maintained by the receipt process.  This number is 0 every time the company receives every thing the other company ships.  """  
      self.TranType:str = obj["TranType"]
      """   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPlant:str = obj["GlbPlant"]
      """  Global Site identifier.  Relates to the External Site record that is created to correlate the Consolidated Purchasing company to a Site in a local Company.  Used in Consolidated Purchasing.  """  
      self.GlbWarehouse:str = obj["GlbWarehouse"]
      """  Global Warehouse identifier.  Relates to the External Warehouse record that is created to correlate the Consolidated Purchasing company to a Warehouse in a local Company.  Used in Consolidated Purchasing.  """  
      self.GlbCreateJobMtl:bool = obj["GlbCreateJobMtl"]
      """  When this PORel is received in the local company, if this flag is set create JobMtl.  Used in Consolidated Purchasing.  """  
      self.ShippedDate:str = obj["ShippedDate"]
      """  Shipped Date  """  
      self.ContainerID:int = obj["ContainerID"]
      """  ID field to the ContainerHeader table.  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.PreviousDueDate:str = obj["PreviousDueDate"]
      """  This field holds the previous value of Due Date.  """  
      self.BaseQty:int = obj["BaseQty"]
      """  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PORel.XRelQty to the PORel.BaseUOM .  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """   Unit of Measure of the PORel.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  """  
      self.BTOOrderNum:int = obj["BTOOrderNum"]
      """  Order Num related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderLine:int = obj["BTOOrderLine"]
      """  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderRelNum:int = obj["BTOOrderRelNum"]
      """  The release number of the sales order line related to this purchase order. Used only for Buy To Order POs.  """  
      self.DropShip:bool = obj["DropShip"]
      """  The value of this field comes from the sales order release. Used only for Buy To Order POs.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo Num from the sales order release. Used only for Buy To Order POs.  """  
      self.SoldToNum:int = obj["SoldToNum"]
      """  The SoldTo ID from the sales order release. Used only for Buy To Order POs.  """  
      self.SMIRcvdQty:int = obj["SMIRcvdQty"]
      """  This is only updated for SMI type POs.  It will indicate how many items have been received into a SMI bin.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.MangCustNum:int = obj["MangCustNum"]
      """  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates that the One Time ShipTO information defined for this release should be used. OTS fields are only used for Drop Shipments.  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.PORelOpen:bool = obj["PORelOpen"]
      """  Open Purchase Release flag  """  
      self.Mapping:bool = obj["Mapping"]
      """  Mapping  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The Project WBS Phase Id associated with this release. This field can only have data if PORel.ProjectID is not blank.  """  
      self.WBSPhaseID:str = obj["WBSPhaseID"]
      """  Project Phase ID  """  
      self.IsMultiRel:bool = obj["IsMultiRel"]
      """  IsMultiRel  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SMIRemQty:int = obj["SMIRemQty"]
      """  Field to track the SMIRcvdQty that has not yet been moved to stock  """  
      self.LockQty:bool = obj["LockQty"]
      """  When the field is checked, no Increase, Reduce or Cancel suggestions will be created for the PO Release  """  
      self.LockDate:bool = obj["LockDate"]
      """  When the field is checked, no Expedite or Postpone suggestions will be created for the PO Release  """  
      self.DueDateChanged:bool = obj["DueDateChanged"]
      """  Indicates Due Date has been changed.  """  
      self.ContractID:str = obj["ContractID"]
      """  The identifier of the planning contract.  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  """  
      self.Status:str = obj["Status"]
      """  Indicates the current status of the release. This field is maintained by the System automatically. The possible values are: Open (O), Arrived (A), Inspection (I), Received (R), Consumed (U), Drop Shipped (D), Closed (C), Voided (V).  """  
      self.ArrivedQty:int = obj["ArrivedQty"]
      """  Total quantity arrived to our site to date. In Purchasing unit of measure. This is a field maintained by the Receipt Process.  """  
      self.InvoicedQty:int = obj["InvoicedQty"]
      """  Total quantity invoiced to date. In Purchasing unit of measure. This is a field maintained by the AP Invoicing Process.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date the PO Release is required for, this can be either from the Sales Order, Material Job, Subcontract Operation, Due Date set within Generate POSuggestions or the Purchase Order Header Date.  """  
      self.LockNeedByDate:bool = obj["LockNeedByDate"]
      """  Set to 'true' if 'NeedByDate' was derived from a valid demand.  """  
      self.InspectionQty:int = obj["InspectionQty"]
      """  Total to date quantity that has been placed into inspection.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process  """  
      self.DeliverTo:str = obj["DeliverTo"]
      """  PO Line types of 'Other' have no specified warehouse / bin and what this field provides is a means of designating 'where / whom' this delivery is intended for.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Taxable  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this item is exempt from PO tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the PO tax info.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.ReqChgPromiseDate:str = obj["ReqChgPromiseDate"]
      """  When the Promise Date is changed, this is the previous PromiseDt  """  
      self.OTSEMailAddress:str = obj["OTSEMailAddress"]
      """  One Time ShipTo email address.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.NumberOfPiecesUOM:str = obj["NumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.FirmRelease:bool = obj["FirmRelease"]
      """  Indicates if this release is  "FIRM".  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.EDIShipReferenceType:str = obj["EDIShipReferenceType"]
      """  Name of the ship reference that is going to be stored.  """  
      self.EDIShipReferenceData:str = obj["EDIShipReferenceData"]
      """  Data that is going to be stored as ship reference.  """  
      self.EDIEstimatedDockDate:str = obj["EDIEstimatedDockDate"]
      """  Estimated time when the shipment will arrive.  """  
      self.EDIShipQty:int = obj["EDIShipQty"]
      """  Quantity sent by the supplier.  """  
      self.EDIShipQtyUOM:str = obj["EDIShipQtyUOM"]
      """  Unit of Measure of the EDIShipQty.  """  
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      self.ContractOrder:bool = obj["ContractOrder"]
      """  Is this Release related to a Contract Purchase Order?  """  
      self.DelPoSug:bool = obj["DelPoSug"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocTotalDedTax:int = obj["DocTotalDedTax"]
      """  Total deductable tax amount for this PO Line in document currency.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in document currency.  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """  Total Tax amount for this PO Line in document currency.  """  
      self.EnableBTOOrderNum:bool = obj["EnableBTOOrderNum"]
      """  flag to determine whether the BTOOrderNum field can be enabled.  If a drop shipment has been Received/Shipped for this line, we cannot allow them to change the BTOOrderNum.  """  
      self.EnableGLAcct:bool = obj["EnableGLAcct"]
      """  Indicates whether the GL account field should be enabled. Based on GLSyst.PostInvtyWipCos and the line type  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      self.ExpDesc:str = obj["ExpDesc"]
      self.FromPOSugChg:bool = obj["FromPOSugChg"]
      self.GlbPlantName:str = obj["GlbPlantName"]
      self.GlbWhseName:str = obj["GlbWhseName"]
      self.Inspection:bool = obj["Inspection"]
      self.IUM:str = obj["IUM"]
      self.Lock:bool = obj["Lock"]
      """  This field will be used in the UI to Lock and unLock a release.  """  
      self.MangCustID:str = obj["MangCustID"]
      """  For CMI type POs, this is the associated customer that we will verify against the WhseBin.CustNum  """  
      self.MangCustName:str = obj["MangCustName"]
      """  For CMI type POs, this is the associated customer Name that we will verify against the WhseBin.CustNum  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  THIS FIELD COMES DIRECTLY FROM THE POHEADER TABLE.  Indicates if an order is flagged as being HELD , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  """  
      self.POHeaderApprove:bool = obj["POHeaderApprove"]
      self.POType:str = obj["POType"]
      """  Identifies the type of PO  """  
      self.PUM:str = obj["PUM"]
      """  Replicate PUM on detail  """  
      self.PurPoint:str = obj["PurPoint"]
      """  THIS FIELD IS EXTRACTED DIRECTLY FROM THE POHEADER TABLE. Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      self.Rpt1TotalDedTax:int = obj["Rpt1TotalDedTax"]
      """  Total deductable tax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """  Total Tax amount for this PO Line in Rpt1 currency,  """  
      self.Rpt2TotalDedTax:int = obj["Rpt2TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """  Total Tax amount for this PO Line in Rpt2 currency,  """  
      self.Rpt3TotalDedTax:int = obj["Rpt3TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt3 currency.  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """  Total Tax amount for this PO Line in Rpt3 currency,  """  
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      self.StatusDescription:str = obj["StatusDescription"]
      """  Description text of the Status field  """  
      self.TotalDedTax:int = obj["TotalDedTax"]
      """  Total deductable tax amount for this PO Line in base currency.  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in base currency.  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Total Tax amount for this PO Line in base currency,  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """   Transaction Type Description i.e. Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"), 
Stock ("PUR-STK") and Other ("PUR-UKN").  """  
      self.UseGlbFields:bool = obj["UseGlbFields"]
      """  Indicates if Glb fields should be used in place of the non-global equivalent  """  
      self.VendorID:str = obj["VendorID"]
      """  Related Supplier ID  """  
      self.VendorName:str = obj["VendorName"]
      """  Related Vendor Name  """  
      self.ContainerShipped:bool = obj["ContainerShipped"]
      """  Logical indicating if the container has been shipped.  """  
      self.ShipToAddrFormatted:str = obj["ShipToAddrFormatted"]
      """  The formatted ship to address  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  """  
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      """  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  """  
      self.AttributeQtyMismatch:bool = obj["AttributeQtyMismatch"]
      """  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  """  
      self.JobMtlSeq:int = obj["JobMtlSeq"]
      self.JobOprSeq:int = obj["JobOprSeq"]
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.ContainerHeaderPromiseDate:str = obj["ContainerHeaderPromiseDate"]
      self.ContainerHeaderDueDate:str = obj["ContainerHeaderDueDate"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.PlantName:str = obj["PlantName"]
      self.POLineRevisionNum:str = obj["POLineRevisionNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.PONumShipName:str = obj["PONumShipName"]
      self.PONumShipToConName:str = obj["PONumShipToConName"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ReqLineLineDesc:str = obj["ReqLineLineDesc"]
      self.ReqNumShipName:str = obj["ReqNumShipName"]
      self.ReqNumShipToConName:str = obj["ReqNumShipToConName"]
      self.ShipToCustNumInactive:bool = obj["ShipToCustNumInactive"]
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.SoldToNumCustID:str = obj["SoldToNumCustID"]
      self.SoldToNumBTName:str = obj["SoldToNumBTName"]
      self.SoldToNumName:str = obj["SoldToNumName"]
      self.SoldToNumInactive:bool = obj["SoldToNumInactive"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.WBSPhaseDescription:str = obj["WBSPhaseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PORelTGLCRow:
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
      self.POLine:int = obj["POLine"]
      """  POLine of PORel  """  
      self.PONum:int = obj["PONum"]
      """  PONum of PORel  """  
      self.PORelNum:int = obj["PORelNum"]
      """  PORelNum of PORel  """  
      self.ReqRef:bool = obj["ReqRef"]
      self.AcctOverride:bool = obj["AcctOverride"]
      """  Indicates if the user selected a different account from the default.  """  
      self.IsMainBook:bool = obj["IsMainBook"]
      """  Column used to know if the book assigned is the Main Book.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PORelTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
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
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last changed (seconds since midnight)  """  
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
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrencyCode:str = obj["CurrencyCode"]
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
      self.Rpt1ScrFixedAmount:int = obj["Rpt1ScrFixedAmount"]
      self.Rpt2ScrFixedAmount:int = obj["Rpt2ScrFixedAmount"]
      self.Rpt3ScrFixedAmount:int = obj["Rpt3ScrFixedAmount"]
      self.ScrFixedAmount:int = obj["ScrFixedAmount"]
      """  Display Fixed Amount in base currency.  """  
      self.DescCollectionType:str = obj["DescCollectionType"]
      """  Collection Type Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POTableset:
   def __init__(self, obj):
      self.POHeader:list[Erp_Tablesets_POHeaderRow] = obj["POHeader"]
      self.POHeaderAttch:list[Erp_Tablesets_POHeaderAttchRow] = obj["POHeaderAttch"]
      self.PODetail:list[Erp_Tablesets_PODetailRow] = obj["PODetail"]
      self.PODetailAttch:list[Erp_Tablesets_PODetailAttchRow] = obj["PODetailAttch"]
      self.PORel:list[Erp_Tablesets_PORelRow] = obj["PORel"]
      self.PORelAttch:list[Erp_Tablesets_PORelAttchRow] = obj["PORelAttch"]
      self.PORelTax:list[Erp_Tablesets_PORelTaxRow] = obj["PORelTax"]
      self.PORelTGLC:list[Erp_Tablesets_PORelTGLCRow] = obj["PORelTGLC"]
      self.PODetailInsp:list[Erp_Tablesets_PODetailInspRow] = obj["PODetailInsp"]
      self.PODetailTax:list[Erp_Tablesets_PODetailTaxRow] = obj["PODetailTax"]
      self.POMisc:list[Erp_Tablesets_POMiscRow] = obj["POMisc"]
      self.PODetailMiscTax:list[Erp_Tablesets_PODetailMiscTaxRow] = obj["PODetailMiscTax"]
      self.POHeadMisc:list[Erp_Tablesets_POHeadMiscRow] = obj["POHeadMisc"]
      self.POHeaderMiscTax:list[Erp_Tablesets_POHeaderMiscTaxRow] = obj["POHeaderMiscTax"]
      self.POHeaderTax:list[Erp_Tablesets_POHeaderTaxRow] = obj["POHeaderTax"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartSubsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The Part number that this substitute Part is for.  """  
      self.SubPart:str = obj["SubPart"]
      """  Substitute Part  """  
      self.RecType:str = obj["RecType"]
      """  Indicates the record type. "S" = Substitute, "C" = Compliment  """  
      self.SubType:str = obj["SubType"]
      """  Pertains only to Substitute Parts (RecType = "S"). Values are "C" - Comparable, "D" - Downgrade, "U" - Upgrade  """  
      self.QtyPer:int = obj["QtyPer"]
      """   The quantity of the alternate part per 1 of the parent part in the parents base inventory uom. Cannot be zero.
To convert an existing OrderDtl.SellingQty to a PartSubs. It is converted to the Parents Part Base Inventory UOM  then multiply PartSubs.QtyPer, then converted to  PartSub.SalesUM.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit of measure used when this part is used as a substitute/compliment with the parent part (partsubs.partnum).  Defaults as Part.SUM of the PartSub.SubPart.  """  
      self.Comment:str = obj["Comment"]
      """  Optional Comment  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultSub:bool = obj["DefaultSub"]
      self.Price:int = obj["Price"]
      """  Price for the Suggested Quantity  """  
      self.SuggestedQty:int = obj["SuggestedQty"]
      """  Suggested Quantity  """  
      self.Selected:bool = obj["Selected"]
      """  Selected Row  """  
      self.SugOrderQty:int = obj["SugOrderQty"]
      """  Suggested Quantity for Order Qty in Quote Detail  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.SubPartSellingFactor:int = obj["SubPartSellingFactor"]
      self.SubPartTrackSerialNum:bool = obj["SubPartTrackSerialNum"]
      self.SubPartTrackDimension:bool = obj["SubPartTrackDimension"]
      self.SubPartPartDescription:str = obj["SubPartPartDescription"]
      self.SubPartIUM:str = obj["SubPartIUM"]
      self.SubPartSalesUM:str = obj["SubPartSalesUM"]
      self.SubPartTrackLots:bool = obj["SubPartTrackLots"]
      self.SubPartPricePerCode:str = obj["SubPartPricePerCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartSubsTableset:
   def __init__(self, obj):
      self.PartSubs:list[Erp_Tablesets_PartSubsRow] = obj["PartSubs"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPOTableset:
   def __init__(self, obj):
      self.POHeader:list[Erp_Tablesets_POHeaderRow] = obj["POHeader"]
      self.POHeaderAttch:list[Erp_Tablesets_POHeaderAttchRow] = obj["POHeaderAttch"]
      self.PODetail:list[Erp_Tablesets_PODetailRow] = obj["PODetail"]
      self.PODetailAttch:list[Erp_Tablesets_PODetailAttchRow] = obj["PODetailAttch"]
      self.PORel:list[Erp_Tablesets_PORelRow] = obj["PORel"]
      self.PORelAttch:list[Erp_Tablesets_PORelAttchRow] = obj["PORelAttch"]
      self.PORelTax:list[Erp_Tablesets_PORelTaxRow] = obj["PORelTax"]
      self.PORelTGLC:list[Erp_Tablesets_PORelTGLCRow] = obj["PORelTGLC"]
      self.PODetailInsp:list[Erp_Tablesets_PODetailInspRow] = obj["PODetailInsp"]
      self.PODetailTax:list[Erp_Tablesets_PODetailTaxRow] = obj["PODetailTax"]
      self.POMisc:list[Erp_Tablesets_POMiscRow] = obj["POMisc"]
      self.PODetailMiscTax:list[Erp_Tablesets_PODetailMiscTaxRow] = obj["PODetailMiscTax"]
      self.POHeadMisc:list[Erp_Tablesets_POHeadMiscRow] = obj["POHeadMisc"]
      self.POHeaderMiscTax:list[Erp_Tablesets_POHeaderMiscTaxRow] = obj["POHeaderMiscTax"]
      self.POHeaderTax:list[Erp_Tablesets_POHeaderTaxRow] = obj["POHeaderTax"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAPLOCDescription_input:
   """ Required : 
   poAPLOCID
   ds
   """  
   def __init__(self, obj):
      self.poAPLOCID:str = obj["poAPLOCID"]
      """  Proposed newPOType to be validated  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class GetAPLOCDescription_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetBasePartAndConfigType_input:
   """ Required : 
   sourceSysRowID
   """  
   def __init__(self, obj):
      self.sourceSysRowID:str = obj["sourceSysRowID"]
      """  PODetail sysrowid  """  
      pass

class GetBasePartAndConfigType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cfgPartNum:str = obj["parameters"]
      self.cfgRevisionNum:str = obj["parameters"]
      self.configType:str = obj["parameters"]
      self.configURL:str = obj["parameters"]
      self.configID:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetBasePartForConfig_input:
   """ Required : 
   sourceSysRowID
   """  
   def __init__(self, obj):
      self.sourceSysRowID:str = obj["sourceSysRowID"]
      """  Order Number of the target Assembly  """  
      pass

class GetBasePartForConfig_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cfgPartNum:str = obj["parameters"]
      self.cfgRevisionNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   poNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_POTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_POTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  The TableName  """  
      self.fieldName:str = obj["fieldName"]
      """  The Field Name  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  description List  """  
      pass

class GetCurrencyBase_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCurrencyBase:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDefaultBuyer_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  Returns true if default buyer was found  """  
      pass

   def parameters(self, obj):
      self.buyerID:str = obj["parameters"]
      self.buyerIDName:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDefaultGLAccountAllPOReleases_input:
   """ Required : 
   pPONum
   ds
   """  
   def __init__(self, obj):
      self.pPONum:int = obj["pPONum"]
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class GetDefaultGLAccountAllPOReleases_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDefaultGLAccount_input:
   """ Required : 
   pPONum
   pPOLine
   pPORelNum
   ds
   """  
   def __init__(self, obj):
      self.pPONum:int = obj["pPONum"]
      self.pPOLine:int = obj["pPOLine"]
      self.pPORelNum:int = obj["pPORelNum"]
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class GetDefaultGLAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDropShipPOHeaderList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetDropShipPOHeaderList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POHeaderListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetGlbCompanyList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.GlbCompanyList:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_POHeaderListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewConsolidatedPO_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class GetNewConsolidatedPO_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewContractPO_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class GetNewContractPO_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPODetailAttch_input:
   """ Required : 
   ds
   poNUM
   poLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.poNUM:int = obj["poNUM"]
      self.poLine:int = obj["poLine"]
      pass

class GetNewPODetailAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPODetailInsp_input:
   """ Required : 
   ds
   poNUM
   poLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.poNUM:int = obj["poNUM"]
      self.poLine:int = obj["poLine"]
      pass

class GetNewPODetailInsp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPODetailMiscTax_input:
   """ Required : 
   ds
   poNUM
   poLine
   seqNum
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.poNUM:int = obj["poNUM"]
      self.poLine:int = obj["poLine"]
      self.seqNum:int = obj["seqNum"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewPODetailMiscTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPODetailTax_input:
   """ Required : 
   ds
   poNum
   poLine
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewPODetailTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPODetail_input:
   """ Required : 
   ds
   poNUM
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.poNUM:int = obj["poNUM"]
      pass

class GetNewPODetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPOHeadMisc_input:
   """ Required : 
   ds
   poNum
   poLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      pass

class GetNewPOHeadMisc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPOHeaderAttch_input:
   """ Required : 
   ds
   poNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.poNum:int = obj["poNum"]
      pass

class GetNewPOHeaderAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPOHeaderMiscTax_input:
   """ Required : 
   ds
   poNum
   seqNum
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.poNum:int = obj["poNum"]
      self.seqNum:int = obj["seqNum"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewPOHeaderMiscTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPOHeaderTax_input:
   """ Required : 
   ds
   poNum
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.poNum:int = obj["poNum"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewPOHeaderTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPOHeader_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class GetNewPOHeader_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPOMisc_input:
   """ Required : 
   ds
   poNum
   poLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      pass

class GetNewPOMisc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPORelAttch_input:
   """ Required : 
   ds
   poNum
   poLine
   poRelNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      self.poRelNum:int = obj["poRelNum"]
      pass

class GetNewPORelAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPORelTGLC_input:
   """ Required : 
   ds
   poNum
   poLine
   poRelNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      self.poRelNum:int = obj["poRelNum"]
      pass

class GetNewPORelTGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPORelTax_input:
   """ Required : 
   ds
   poNum
   poLine
   poRelNum
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      self.poRelNum:int = obj["poRelNum"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewPORelTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPORel_input:
   """ Required : 
   ds
   poNum
   poLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      pass

class GetNewPORel_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPOReceipts_input:
   """ Required : 
   ipPONum
   """  
   def __init__(self, obj):
      self.ipPONum:int = obj["ipPONum"]
      """  PONum.  """  
      pass

class GetPOReceipts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POReceiptsTableset] = obj["returnObj"]
      pass

class GetPORelationshipMap_input:
   """ Required : 
   poNum
   maxNumOfCards
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      self.maxNumOfCards:int = obj["maxNumOfCards"]
      pass

class GetPORelationshipMap_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetPartSubList_input:
   """ Required : 
   PartNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      """  The part number  """  
      self.pageSize:int = obj["pageSize"]
      """  pageSize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolutePage  """  
      pass

class GetPartSubList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartSubsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetPlantsForPart_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Part Number  """  
      pass

class GetPlantsForPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPlantList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRowsForAPInvoice_input:
   """ Required : 
   whereClausePOHeader
   whereClausePOHeaderAttch
   whereClausePODetail
   whereClausePODetailAttch
   whereClausePORel
   whereClausePORelAttch
   whereClausePORelTax
   whereClausePORelTGLC
   whereClausePODetailInsp
   whereClausePODetailTax
   whereClausePOMisc
   whereClausePODetailMiscTax
   whereClausePOHeadMisc
   whereClausePOHeaderMiscTax
   whereClausePOHeaderTax
   invoiceNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePOHeader:str = obj["whereClausePOHeader"]
      self.whereClausePOHeaderAttch:str = obj["whereClausePOHeaderAttch"]
      self.whereClausePODetail:str = obj["whereClausePODetail"]
      self.whereClausePODetailAttch:str = obj["whereClausePODetailAttch"]
      self.whereClausePORel:str = obj["whereClausePORel"]
      self.whereClausePORelAttch:str = obj["whereClausePORelAttch"]
      self.whereClausePORelTax:str = obj["whereClausePORelTax"]
      self.whereClausePORelTGLC:str = obj["whereClausePORelTGLC"]
      self.whereClausePODetailInsp:str = obj["whereClausePODetailInsp"]
      self.whereClausePODetailTax:str = obj["whereClausePODetailTax"]
      self.whereClausePOMisc:str = obj["whereClausePOMisc"]
      self.whereClausePODetailMiscTax:str = obj["whereClausePODetailMiscTax"]
      self.whereClausePOHeadMisc:str = obj["whereClausePOHeadMisc"]
      self.whereClausePOHeaderMiscTax:str = obj["whereClausePOHeaderMiscTax"]
      self.whereClausePOHeaderTax:str = obj["whereClausePOHeaderTax"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForAPInvoice_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForPayment_input:
   """ Required : 
   whereClausePOHeader
   whereClausePOHeaderAttch
   whereClausePODetail
   whereClausePODetailAttch
   whereClausePORel
   whereClausePORelAttch
   whereClausePORelTax
   whereClausePORelTGLC
   whereClausePODetailInsp
   whereClausePODetailTax
   whereClausePOMisc
   whereClausePODetailMiscTax
   whereClausePOHeadMisc
   whereClausePOHeaderMiscTax
   whereClausePOHeaderTax
   headNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePOHeader:str = obj["whereClausePOHeader"]
      self.whereClausePOHeaderAttch:str = obj["whereClausePOHeaderAttch"]
      self.whereClausePODetail:str = obj["whereClausePODetail"]
      self.whereClausePODetailAttch:str = obj["whereClausePODetailAttch"]
      self.whereClausePORel:str = obj["whereClausePORel"]
      self.whereClausePORelAttch:str = obj["whereClausePORelAttch"]
      self.whereClausePORelTax:str = obj["whereClausePORelTax"]
      self.whereClausePORelTGLC:str = obj["whereClausePORelTGLC"]
      self.whereClausePODetailInsp:str = obj["whereClausePODetailInsp"]
      self.whereClausePODetailTax:str = obj["whereClausePODetailTax"]
      self.whereClausePOMisc:str = obj["whereClausePOMisc"]
      self.whereClausePODetailMiscTax:str = obj["whereClausePODetailMiscTax"]
      self.whereClausePOHeadMisc:str = obj["whereClausePOHeadMisc"]
      self.whereClausePOHeaderMiscTax:str = obj["whereClausePOHeaderMiscTax"]
      self.whereClausePOHeaderTax:str = obj["whereClausePOHeaderTax"]
      self.headNum:int = obj["headNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForPayment_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForReceipt_input:
   """ Required : 
   whereClausePOHeader
   whereClausePOHeaderAttch
   whereClausePODetail
   whereClausePODetailAttch
   whereClausePORel
   whereClausePORelAttch
   whereClausePORelTax
   whereClausePORelTGLC
   whereClausePODetailInsp
   whereClausePODetailTax
   whereClausePOMisc
   whereClausePODetailMiscTax
   whereClausePOHeadMisc
   whereClausePOHeaderMiscTax
   whereClausePOHeaderTax
   vendorNum
   purPoint
   packSlip
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePOHeader:str = obj["whereClausePOHeader"]
      self.whereClausePOHeaderAttch:str = obj["whereClausePOHeaderAttch"]
      self.whereClausePODetail:str = obj["whereClausePODetail"]
      self.whereClausePODetailAttch:str = obj["whereClausePODetailAttch"]
      self.whereClausePORel:str = obj["whereClausePORel"]
      self.whereClausePORelAttch:str = obj["whereClausePORelAttch"]
      self.whereClausePORelTax:str = obj["whereClausePORelTax"]
      self.whereClausePORelTGLC:str = obj["whereClausePORelTGLC"]
      self.whereClausePODetailInsp:str = obj["whereClausePODetailInsp"]
      self.whereClausePODetailTax:str = obj["whereClausePODetailTax"]
      self.whereClausePOMisc:str = obj["whereClausePOMisc"]
      self.whereClausePODetailMiscTax:str = obj["whereClausePODetailMiscTax"]
      self.whereClausePOHeadMisc:str = obj["whereClausePOHeadMisc"]
      self.whereClausePOHeaderMiscTax:str = obj["whereClausePOHeaderMiscTax"]
      self.whereClausePOHeaderTax:str = obj["whereClausePOHeaderTax"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForReceipt_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePOHeader
   whereClausePOHeaderAttch
   whereClausePODetail
   whereClausePODetailAttch
   whereClausePORel
   whereClausePORelAttch
   whereClausePORelTax
   whereClausePORelTGLC
   whereClausePODetailInsp
   whereClausePODetailTax
   whereClausePOMisc
   whereClausePODetailMiscTax
   whereClausePOHeadMisc
   whereClausePOHeaderMiscTax
   whereClausePOHeaderTax
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePOHeader:str = obj["whereClausePOHeader"]
      self.whereClausePOHeaderAttch:str = obj["whereClausePOHeaderAttch"]
      self.whereClausePODetail:str = obj["whereClausePODetail"]
      self.whereClausePODetailAttch:str = obj["whereClausePODetailAttch"]
      self.whereClausePORel:str = obj["whereClausePORel"]
      self.whereClausePORelAttch:str = obj["whereClausePORelAttch"]
      self.whereClausePORelTax:str = obj["whereClausePORelTax"]
      self.whereClausePORelTGLC:str = obj["whereClausePORelTGLC"]
      self.whereClausePODetailInsp:str = obj["whereClausePODetailInsp"]
      self.whereClausePODetailTax:str = obj["whereClausePODetailTax"]
      self.whereClausePOMisc:str = obj["whereClausePOMisc"]
      self.whereClausePODetailMiscTax:str = obj["whereClausePODetailMiscTax"]
      self.whereClausePOHeadMisc:str = obj["whereClausePOHeadMisc"]
      self.whereClausePOHeaderMiscTax:str = obj["whereClausePOHeaderMiscTax"]
      self.whereClausePOHeaderTax:str = obj["whereClausePOHeaderTax"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetShipToAddressForCompany_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class GetShipToAddressForCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetShipToAddressForCustomer_input:
   """ Required : 
   custNum
   shipToNum
   ds
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class GetShipToAddressForCustomer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetShipToAddressForSite_input:
   """ Required : 
   plant
   ds
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class GetShipToAddressForSite_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetShipToAddressForSupplier_input:
   """ Required : 
   vendorNum
   purPoint
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class GetShipToAddressForSupplier_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetValidManufacturers_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      pass

class GetValidManufacturers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.whereClause:str = obj["parameters"]
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

class PartStatusValidationMessages_input:
   """ Required : 
   valpartnum
   """  
   def __init__(self, obj):
      self.valpartnum:str = obj["valpartnum"]
      """  The new PartNum if a substitute part is found, partNum will be the substitute part  """  
      pass

class PartStatusValidationMessages_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.valpartnum:str = obj["parameters"]
      self.QuestionString:str = obj["parameters"]
      self.SubstitutePartAvail:bool = obj["SubstitutePartAvail"]
      self.MsgType:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreDuplicatePO_input:
   """ Required : 
   ipoNum
   """  
   def __init__(self, obj):
      self.ipoNum:int = obj["ipoNum"]
      pass

class PreDuplicatePO_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ReOpenRelease_input:
   """ Required : 
   PoNum
   PoLine
   PoRelease
   """  
   def __init__(self, obj):
      self.PoNum:int = obj["PoNum"]
      """  The Purchase ordre number  """  
      self.PoLine:int = obj["PoLine"]
      """  The Purchase order line  """  
      self.PoRelease:int = obj["PoRelease"]
      """  The Purchase ordre release  """  
      pass

class ReOpenRelease_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POTableset] = obj["returnObj"]
      pass

class ReopenOrderLine_input:
   """ Required : 
   PoNum
   PoLine
   """  
   def __init__(self, obj):
      self.PoNum:int = obj["PoNum"]
      """  The Purchase ordre number  """  
      self.PoLine:int = obj["PoLine"]
      """  The Purchase ordre line  """  
      pass

class ReopenOrderLine_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POTableset] = obj["returnObj"]
      pass

class ReopenOrder_input:
   """ Required : 
   PoNum
   """  
   def __init__(self, obj):
      self.PoNum:int = obj["PoNum"]
      """  The Purchase ordre number  """  
      pass

class ReopenOrder_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POTableset] = obj["returnObj"]
      pass

class SetReadyToCalc_input:
   """ Required : 
   poNum
   calledFromUI
   ds
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      self.calledFromUI:bool = obj["calledFromUI"]
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class SetReadyToCalc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPOTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPOTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidataPartToLinkToContract_input:
   """ Required : 
   bLinkToContract
   partNum
   tableName
   """  
   def __init__(self, obj):
      self.bLinkToContract:bool = obj["bLinkToContract"]
      self.partNum:str = obj["partNum"]
      self.tableName:str = obj["tableName"]
      pass

class ValidataPartToLinkToContract_output:
   def __init__(self, obj):
      pass

class ValidateAcctForGLControl_input:
   """ Required : 
   ipPONum
   """  
   def __init__(self, obj):
      self.ipPONum:int = obj["ipPONum"]
      """  PONum  """  
      pass

class ValidateAcctForGLControl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateInspection_input:
   """ Required : 
   ipProposedInspPlan
   ipProposedSpecId
   ds
   """  
   def __init__(self, obj):
      self.ipProposedInspPlan:str = obj["ipProposedInspPlan"]
      """  The new proposed InspPlanPartNum value  """  
      self.ipProposedSpecId:str = obj["ipProposedSpecId"]
      """  The new proposed SpecID value  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class ValidateInspection_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidatePOLinesTaxCategoryTypes_input:
   """ Required : 
   PONum
   """  
   def __init__(self, obj):
      self.PONum:int = obj["PONum"]
      """  The order number to validate  """  
      pass

class ValidatePOLinesTaxCategoryTypes_output:
   def __init__(self, obj):
      pass

class VerifyReopenRelease_input:
   """ Required : 
   ds
   iPoNum
   iPoLine
   iPoRelease
   cPartNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.iPoNum:int = obj["iPoNum"]
      """  The Order Number of the Order Release to reopen  """  
      self.iPoLine:int = obj["iPoLine"]
      """  The Order Line Number of the Release to close  """  
      self.iPoRelease:int = obj["iPoRelease"]
      """  The Release Number of the Release to close  """  
      self.cPartNum:str = obj["cPartNum"]
      """  PartNum associated with this release  """  
      pass

class VerifyReopenRelease_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      self.cPromptMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class chkPODatesChanges_input:
   """ Required : 
   viewName
   ds
   """  
   def __init__(self, obj):
      self.viewName:str = obj["viewName"]
      """  Name of the view that is being modified.  """  
      self.ds:list[Erp_Tablesets_POTableset] = obj["ds"]
      pass

class chkPODatesChanges_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cOrderChangedMsgText:str = obj["parameters"]
      pass

      """  output parameters  """  

