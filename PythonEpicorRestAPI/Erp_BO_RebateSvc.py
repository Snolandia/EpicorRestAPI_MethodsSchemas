import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RebateSvc
# Description: This is the maintenance object for Rebates
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Rebates(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Rebates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Rebates
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateHdrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates",headers=creds) as resp:
           return await resp.json()

async def post_Rebates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Rebates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RebateHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RebateHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Rebates_Company_RebateID(Company, RebateID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Rebate item
   Description: Calls GetByID to retrieve the Rebate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Rebate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RebateHdrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Rebates_Company_RebateID(Company, RebateID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Rebate for the service
   Description: Calls UpdateExt to update Rebate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Rebate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RebateHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Rebates_Company_RebateID(Company, RebateID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Rebate item
   Description: Call UpdateExt to delete Rebate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Rebate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Rebates_Company_RebateID_RebateCusts(Company, RebateID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RebateCusts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RebateCusts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateCustRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")/RebateCusts",headers=creds) as resp:
           return await resp.json()

async def get_Rebates_Company_RebateID_RebateCusts_Company_RebateID_CustNum(Company, RebateID, CustNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RebateCust item
   Description: Calls GetByID to retrieve the RebateCust item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateCust1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RebateCustRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")/RebateCusts(" + Company + "," + RebateID + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_Rebates_Company_RebateID_RebateDtls(Company, RebateID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RebateDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RebateDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")/RebateDtls",headers=creds) as resp:
           return await resp.json()

async def get_Rebates_Company_RebateID_RebateDtls_Company_RebateID_LineNum(Company, RebateID, LineNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RebateDtl item
   Description: Calls GetByID to retrieve the RebateDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RebateDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")/RebateDtls(" + Company + "," + RebateID + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_Rebates_Company_RebateID_RebatePymts(Company, RebateID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RebatePymts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RebatePymts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebatePymtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")/RebatePymts",headers=creds) as resp:
           return await resp.json()

async def get_Rebates_Company_RebateID_RebatePymts_Company_RebateID_PymtDate(Company, RebateID, PymtDate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RebatePymt item
   Description: Calls GetByID to retrieve the RebatePymt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebatePymt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param PymtDate: Desc: PymtDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RebatePymtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")/RebatePymts(" + Company + "," + RebateID + "," + PymtDate + ")",headers=creds) as resp:
           return await resp.json()

async def get_Rebates_Company_RebateID_RebateHdrAttches(Company, RebateID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RebateHdrAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RebateHdrAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateHdrAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")/RebateHdrAttches",headers=creds) as resp:
           return await resp.json()

async def get_Rebates_Company_RebateID_RebateHdrAttches_Company_RebateID_DrawingSeq(Company, RebateID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RebateHdrAttch item
   Description: Calls GetByID to retrieve the RebateHdrAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateHdrAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RebateHdrAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/Rebates(" + Company + "," + RebateID + ")/RebateHdrAttches(" + Company + "," + RebateID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RebateCusts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RebateCusts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RebateCusts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateCustRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCusts",headers=creds) as resp:
           return await resp.json()

async def post_RebateCusts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RebateCusts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RebateCustRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RebateCustRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCusts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RebateCusts_Company_RebateID_CustNum(Company, RebateID, CustNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RebateCust item
   Description: Calls GetByID to retrieve the RebateCust item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateCust
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RebateCustRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCusts(" + Company + "," + RebateID + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RebateCusts_Company_RebateID_CustNum(Company, RebateID, CustNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RebateCust for the service
   Description: Calls UpdateExt to update RebateCust. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RebateCust
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RebateCustRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCusts(" + Company + "," + RebateID + "," + CustNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RebateCusts_Company_RebateID_CustNum(Company, RebateID, CustNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RebateCust item
   Description: Call UpdateExt to delete RebateCust item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RebateCust
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCusts(" + Company + "," + RebateID + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_RebateCusts_Company_RebateID_CustNum_RebateCustDtls(Company, RebateID, CustNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RebateCustDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RebateCustDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateCustDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCusts(" + Company + "," + RebateID + "," + CustNum + ")/RebateCustDtls",headers=creds) as resp:
           return await resp.json()

async def get_RebateCusts_Company_RebateID_CustNum_RebateCustDtls_Company_RebateID_LineNum_CustNum(Company, RebateID, CustNum, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RebateCustDtl item
   Description: Calls GetByID to retrieve the RebateCustDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateCustDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RebateCustDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCusts(" + Company + "," + RebateID + "," + CustNum + ")/RebateCustDtls(" + Company + "," + RebateID + "," + LineNum + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_RebateCustDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RebateCustDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RebateCustDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateCustDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCustDtls",headers=creds) as resp:
           return await resp.json()

async def post_RebateCustDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RebateCustDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RebateCustDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RebateCustDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCustDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RebateCustDtls_Company_RebateID_LineNum_CustNum(Company, RebateID, LineNum, CustNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RebateCustDtl item
   Description: Calls GetByID to retrieve the RebateCustDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateCustDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RebateCustDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCustDtls(" + Company + "," + RebateID + "," + LineNum + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RebateCustDtls_Company_RebateID_LineNum_CustNum(Company, RebateID, LineNum, CustNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RebateCustDtl for the service
   Description: Calls UpdateExt to update RebateCustDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RebateCustDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RebateCustDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCustDtls(" + Company + "," + RebateID + "," + LineNum + "," + CustNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RebateCustDtls_Company_RebateID_LineNum_CustNum(Company, RebateID, LineNum, CustNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RebateCustDtl item
   Description: Call UpdateExt to delete RebateCustDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RebateCustDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateCustDtls(" + Company + "," + RebateID + "," + LineNum + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_RebateDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RebateDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RebateDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateDtls",headers=creds) as resp:
           return await resp.json()

async def post_RebateDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RebateDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RebateDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RebateDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RebateDtls_Company_RebateID_LineNum(Company, RebateID, LineNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RebateDtl item
   Description: Calls GetByID to retrieve the RebateDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RebateDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateDtls(" + Company + "," + RebateID + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RebateDtls_Company_RebateID_LineNum(Company, RebateID, LineNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RebateDtl for the service
   Description: Calls UpdateExt to update RebateDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RebateDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RebateDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateDtls(" + Company + "," + RebateID + "," + LineNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RebateDtls_Company_RebateID_LineNum(Company, RebateID, LineNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RebateDtl item
   Description: Call UpdateExt to delete RebateDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RebateDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateDtls(" + Company + "," + RebateID + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_RebateDtls_Company_RebateID_LineNum_RebateBrks(Company, RebateID, LineNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RebateBrks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RebateBrks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateDtls(" + Company + "," + RebateID + "," + LineNum + ")/RebateBrks",headers=creds) as resp:
           return await resp.json()

async def get_RebateDtls_Company_RebateID_LineNum_RebateBrks_Company_RebateID_LineNum_BreakMin(Company, RebateID, LineNum, BreakMin, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RebateBrk item
   Description: Calls GetByID to retrieve the RebateBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateBrk1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param BreakMin: Desc: BreakMin   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RebateBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateDtls(" + Company + "," + RebateID + "," + LineNum + ")/RebateBrks(" + Company + "," + RebateID + "," + LineNum + "," + BreakMin + ")",headers=creds) as resp:
           return await resp.json()

async def get_RebateBrks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RebateBrks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RebateBrks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateBrks",headers=creds) as resp:
           return await resp.json()

async def post_RebateBrks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RebateBrks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RebateBrkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RebateBrkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateBrks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RebateBrks_Company_RebateID_LineNum_BreakMin(Company, RebateID, LineNum, BreakMin, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RebateBrk item
   Description: Calls GetByID to retrieve the RebateBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param BreakMin: Desc: BreakMin   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RebateBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateBrks(" + Company + "," + RebateID + "," + LineNum + "," + BreakMin + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RebateBrks_Company_RebateID_LineNum_BreakMin(Company, RebateID, LineNum, BreakMin, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RebateBrk for the service
   Description: Calls UpdateExt to update RebateBrk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RebateBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param BreakMin: Desc: BreakMin   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RebateBrkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateBrks(" + Company + "," + RebateID + "," + LineNum + "," + BreakMin + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RebateBrks_Company_RebateID_LineNum_BreakMin(Company, RebateID, LineNum, BreakMin, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RebateBrk item
   Description: Call UpdateExt to delete RebateBrk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RebateBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param BreakMin: Desc: BreakMin   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateBrks(" + Company + "," + RebateID + "," + LineNum + "," + BreakMin + ")",headers=creds) as resp:
           return await resp.json()

async def get_RebatePymts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RebatePymts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RebatePymts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebatePymtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebatePymts",headers=creds) as resp:
           return await resp.json()

async def post_RebatePymts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RebatePymts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RebatePymtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RebatePymtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebatePymts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RebatePymts_Company_RebateID_PymtDate(Company, RebateID, PymtDate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RebatePymt item
   Description: Calls GetByID to retrieve the RebatePymt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebatePymt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param PymtDate: Desc: PymtDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RebatePymtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebatePymts(" + Company + "," + RebateID + "," + PymtDate + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RebatePymts_Company_RebateID_PymtDate(Company, RebateID, PymtDate, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RebatePymt for the service
   Description: Calls UpdateExt to update RebatePymt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RebatePymt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param PymtDate: Desc: PymtDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RebatePymtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebatePymts(" + Company + "," + RebateID + "," + PymtDate + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RebatePymts_Company_RebateID_PymtDate(Company, RebateID, PymtDate, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RebatePymt item
   Description: Call UpdateExt to delete RebatePymt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RebatePymt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param PymtDate: Desc: PymtDate   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebatePymts(" + Company + "," + RebateID + "," + PymtDate + ")",headers=creds) as resp:
           return await resp.json()

async def get_RebateHdrAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RebateHdrAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RebateHdrAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateHdrAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateHdrAttches",headers=creds) as resp:
           return await resp.json()

async def post_RebateHdrAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RebateHdrAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RebateHdrAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RebateHdrAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateHdrAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RebateHdrAttches_Company_RebateID_DrawingSeq(Company, RebateID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RebateHdrAttch item
   Description: Calls GetByID to retrieve the RebateHdrAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateHdrAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RebateHdrAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateHdrAttches(" + Company + "," + RebateID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RebateHdrAttches_Company_RebateID_DrawingSeq(Company, RebateID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RebateHdrAttch for the service
   Description: Calls UpdateExt to update RebateHdrAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RebateHdrAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RebateHdrAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateHdrAttches(" + Company + "," + RebateID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RebateHdrAttches_Company_RebateID_DrawingSeq(Company, RebateID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RebateHdrAttch item
   Description: Call UpdateExt to delete RebateHdrAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RebateHdrAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/RebateHdrAttches(" + Company + "," + RebateID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateHdrListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRebateHdr, whereClauseRebateHdrAttch, whereClauseRebateCust, whereClauseRebateCustDtl, whereClauseRebateDtl, whereClauseRebateBrk, whereClauseRebatePymt, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseRebateHdr=" + whereClauseRebateHdr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRebateHdrAttch=" + whereClauseRebateHdrAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRebateCust=" + whereClauseRebateCust
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRebateCustDtl=" + whereClauseRebateCustDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRebateDtl=" + whereClauseRebateDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRebateBrk=" + whereClauseRebateBrk
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRebatePymt=" + whereClauseRebatePymt
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(rebateID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "rebateID=" + rebateID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailPartNum
   Description: This method validates and populates the Part related fields when the
RebateDtl.PartNum changes
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHdrCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHdrCustID
   Description: This method validates and populates the Customer fields when the
ttRebateHdr.CustomerCustID changes
   OperationID: ChangeHdrCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHdrCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHdrCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePymtDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePymtDate
   Description: This method should run before changing the RebatePymt.PymtDate.
   OperationID: ChangePymtDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePymtDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePymtDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePymtDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePymtDate
   Description: This method validates the proposed value of the PymtDate field.
   OperationID: OnChangePymtDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePymtDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePymtDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRCCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRCCustomer
   Description: This method validates and populates the Customer fields when the
RebateCust.CustID changes
   OperationID: ChangeRCCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRCCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRCCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyRebate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyRebate
   Description: This method copies one rebate to a new rebate.  The user can change either
the dates of the rebate or the customers for the rebate.
If changing the dates, then custNum and groupCode fields will be ignored
If date fields are null, then either custID or groupCode must be populated
   OperationID: CopyRebate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyRebate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyRebate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCustGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustGroup
   Description: This method generates RebateCust records for the specified Rebate and Customer Group.
   OperationID: GetCustGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRebateHdr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRebateHdr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRebateHdr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRebateHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRebateHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRebateHdrAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRebateHdrAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRebateHdrAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRebateHdrAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRebateHdrAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRebateCust(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRebateCust
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRebateCust
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRebateCust_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRebateCust_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRebateCustDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRebateCustDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRebateCustDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRebateCustDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRebateCustDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRebateDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRebateDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRebateDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRebateDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRebateDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRebateBrk(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRebateBrk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRebateBrk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRebateBrk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRebateBrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRebatePymt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRebatePymt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRebatePymt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRebatePymt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRebatePymt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateBrkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RebateBrkRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateCustDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RebateCustDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateCustRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RebateCustRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RebateDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateHdrAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RebateHdrAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateHdrListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RebateHdrListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateHdrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RebateHdrRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebatePymtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RebatePymtRow] = obj["value"]
      pass

class Erp_Tablesets_RebateBrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.LineNum:int = obj["LineNum"]
      """  Internal unique identifier for the RebateDtl table  """  
      self.BreakMin:int = obj["BreakMin"]
      """  The miniumum quantity or amount needed to meet this level  """  
      self.RebatePercent:int = obj["RebatePercent"]
      """  The Rebate Percent that is to be given for this rebate break level. Do not allow both a rebate percent and amount for the same break to be non-zero or both of them to be zero.  One must be entered but not both.  """  
      self.RebateAmount:int = obj["RebateAmount"]
      """  The Rebate Amount that is to be given for this rebate break level. Do not allow both a rebate percent and amount for the same break to be non-zero or both of them to be zero.  One must be entered but not both.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RebateCustDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.LineNum:int = obj["LineNum"]
      """  Internal unique identifier for the RebateDtl table  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.Void:bool = obj["Void"]
      """  Indicates if the customer is no longer participating in the Rebate  """  
      self.PaidAmount:int = obj["PaidAmount"]
      """  Total amount of rebate paid to date  """  
      self.AccruedAmount:int = obj["AccruedAmount"]
      """  Amount of rebate that has been earned  """  
      self.AccruedQty:int = obj["AccruedQty"]
      """  Total Invoice Quantity Accrued toward Rebate  """  
      self.UOMCode:str = obj["UOMCode"]
      """  AccuredQty Unit of Measure  """  
      self.AccruedTot:int = obj["AccruedTot"]
      """  Total Invoice Amount accrued towards rebate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BalanceAmount:int = obj["BalanceAmount"]
      """  AccruedAmount less PaidAmount  """  
      self.ProdCodeDesc:str = obj["ProdCodeDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RebateDtlProdCode:str = obj["RebateDtlProdCode"]
      self.RebateDtlPartNum:str = obj["RebateDtlPartNum"]
      self.RebateDtlUOMCode:str = obj["RebateDtlUOMCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RebateCustRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.FixedDisc:int = obj["FixedDisc"]
      """  Populated from the Customer's Terms code.  Discount to reduce invoice amount by before applying the rebate discount  """  
      self.Void:bool = obj["Void"]
      """  Indicates if the customer is no longer participating in the Rebate  """  
      self.PaidAmount:int = obj["PaidAmount"]
      """  Total amount of rebate paid to date  """  
      self.AccruedAmount:int = obj["AccruedAmount"]
      """  Amount of rebate that has been earned  """  
      self.RebateForm:str = obj["RebateForm"]
      """  Indicates if the rebate should be a Check or a Credit Memo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BalanceAmount:int = obj["BalanceAmount"]
      """  Amount remaining between Accrued amount and paid amount  """  
      self.GroupCode:str = obj["GroupCode"]
      self.RebateSuppID:str = obj["RebateSuppID"]
      """  Rebate Supplier ID  """  
      self.VendorName:str = obj["VendorName"]
      """  Rebate Supplier Name  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RebateDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.LineNum:int = obj["LineNum"]
      """  Internal unique identifier for the RebateDtl table  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  """  
      self.Void:bool = obj["Void"]
      """  Part/PartClass is no longer a part of the Rebate  """  
      self.PaidAmount:int = obj["PaidAmount"]
      """  Total amount of rebate paid to date  """  
      self.AccruedAmount:int = obj["AccruedAmount"]
      """  Amount of rebate that has been earned  """  
      self.BreakType:str = obj["BreakType"]
      """  Indicates whether the BreakMin for the levels is a quantity or Amount.  """  
      self.UOMCode:str = obj["UOMCode"]
      """  Unit of Measure  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BalanceAmount:int = obj["BalanceAmount"]
      """  Accrued Amount less Paid Amount  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.ProdGrupDescription:str = obj["ProdGrupDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RebateHdrAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RebateID:str = obj["RebateID"]
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

class Erp_Tablesets_RebateHdrListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.RebateDesc:str = obj["RebateDesc"]
      """  Rebate Description  """  
      self.StartDate:str = obj["StartDate"]
      """  Starting Date of the Rebate  """  
      self.EndDate:str = obj["EndDate"]
      """  End Date of the Rebate  """  
      self.GraceDays:int = obj["GraceDays"]
      """  Number of days after the end date before a rebate check can be processed  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Rebate is active or not  """  
      self.PaidAmount:int = obj["PaidAmount"]
      """  Total amount of rebate paid to date  """  
      self.AccruedAmount:int = obj["AccruedAmount"]
      """  Amount of rebate that has been earned  """  
      self.CustNum:int = obj["CustNum"]
      """  If the Rebate is to be paid to one customer use this Customer.  If this is 0 then a Rebate will go to each customer in the Rebate  """  
      self.AccrualType:str = obj["AccrualType"]
      """  Generate Rebate Transactions based on Invoices or Payments  """  
      self.BillToFlag:bool = obj["BillToFlag"]
      """  If checked, the Invoice Bill to number will be looked at otherwise the soldTo customer number is used for the rebate  """  
      self.RebateForm:str = obj["RebateForm"]
      """  Indicates if the rebate should be a Check or a Credit Memo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BalanceAmount:int = obj["BalanceAmount"]
      """  Accrued Amount less Paid Amount  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RebateHdrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.RebateDesc:str = obj["RebateDesc"]
      """  Rebate Description  """  
      self.StartDate:str = obj["StartDate"]
      """  Starting Date of the Rebate  """  
      self.EndDate:str = obj["EndDate"]
      """  End Date of the Rebate  """  
      self.GraceDays:int = obj["GraceDays"]
      """  Number of days after the end date before a rebate check can be processed  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Rebate is active or not  """  
      self.PaidAmount:int = obj["PaidAmount"]
      """  Total amount of rebate paid to date  """  
      self.AccruedAmount:int = obj["AccruedAmount"]
      """  Amount of rebate that has been earned  """  
      self.CustNum:int = obj["CustNum"]
      """  If the Rebate is to be paid to one customer use this Customer.  If this is 0 then a Rebate will go to each customer in the Rebate  """  
      self.AccrualType:str = obj["AccrualType"]
      """  Generate Rebate Transactions based on Invoices or Payments  """  
      self.BillToFlag:bool = obj["BillToFlag"]
      """  If checked, the Invoice Bill to number will be looked at otherwise the soldTo customer number is used for the rebate  """  
      self.RebateForm:str = obj["RebateForm"]
      """  Indicates if the rebate should be a Check or a Credit Memo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BalanceAmount:int = obj["BalanceAmount"]
      """  Accrued Amount less Paid Amount  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RebatePymtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.PymtDate:str = obj["PymtDate"]
      """  Date to generate the rebate on  """  
      self.Generated:bool = obj["Generated"]
      """  Flag to indicate if the rebates have been generated  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates that the transactions for the rebate have been approved and the check/credit memo can be created  """  
      self.Pulled:bool = obj["Pulled"]
      """  Indicates if the Rebate has been pulled into AR.  If yes, the next pull will ignore the group.  """  
      self.APPulled:bool = obj["APPulled"]
      """  Indicates if the Rebate has been pulled into AP.  If yes, the next pull will ignore the group.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeDetailPartNum_input:
   """ Required : 
   inPartNum
   ds
   """  
   def __init__(self, obj):
      self.inPartNum:str = obj["inPartNum"]
      """  The proposed Part Num  """  
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

class ChangeDetailPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHdrCustID_input:
   """ Required : 
   inCustID
   ds
   """  
   def __init__(self, obj):
      self.inCustID:str = obj["inCustID"]
      """  The proposed Customer ID  """  
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

class ChangeHdrCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePymtDate_input:
   """ Required : 
   ipProposedPymtDate
   ds
   """  
   def __init__(self, obj):
      self.ipProposedPymtDate:str = obj["ipProposedPymtDate"]
      """  The new proposed RebatePymt.PymtDate value  """  
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

class ChangePymtDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRCCustomer_input:
   """ Required : 
   inCustID
   ds
   """  
   def __init__(self, obj):
      self.inCustID:str = obj["inCustID"]
      """  The proposed Customer ID  """  
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

class ChangeRCCustomer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CopyRebate_input:
   """ Required : 
   fromRebateID
   newRebateID
   newRebateDesc
   newDate
   newCustomer
   newSchedule
   startDate
   endDate
   custID
   groupCode
   pRebateForm
   """  
   def __init__(self, obj):
      self.fromRebateID:str = obj["fromRebateID"]
      """  RebateID to copy from  """  
      self.newRebateID:str = obj["newRebateID"]
      """  RebateID to create  """  
      self.newRebateDesc:str = obj["newRebateDesc"]
      """  New description for rebate  """  
      self.newDate:bool = obj["newDate"]
      """  Flag to indicate if a new Date will be added  """  
      self.newCustomer:bool = obj["newCustomer"]
      """  Flag to indicate if Customers are going to be replaced  """  
      self.newSchedule:bool = obj["newSchedule"]
      """  Flag to indicate if Schedule will be copied or defaulted  """  
      self.startDate:str = obj["startDate"]
      """  Rebate Start date  """  
      self.endDate:str = obj["endDate"]
      """  Rebate End date  """  
      self.custID:str = obj["custID"]
      """  Customer to be used for rebate  """  
      self.groupCode:str = obj["groupCode"]
      """  Customer Group Code to be used for rebate  """  
      self.pRebateForm:str = obj["pRebateForm"]
      """  Rebate Form when Rebate Supplier is empty  """  
      pass

class CopyRebate_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RebateTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   rebateID
   """  
   def __init__(self, obj):
      self.rebateID:str = obj["rebateID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_RebateBrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.LineNum:int = obj["LineNum"]
      """  Internal unique identifier for the RebateDtl table  """  
      self.BreakMin:int = obj["BreakMin"]
      """  The miniumum quantity or amount needed to meet this level  """  
      self.RebatePercent:int = obj["RebatePercent"]
      """  The Rebate Percent that is to be given for this rebate break level. Do not allow both a rebate percent and amount for the same break to be non-zero or both of them to be zero.  One must be entered but not both.  """  
      self.RebateAmount:int = obj["RebateAmount"]
      """  The Rebate Amount that is to be given for this rebate break level. Do not allow both a rebate percent and amount for the same break to be non-zero or both of them to be zero.  One must be entered but not both.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RebateCustDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.LineNum:int = obj["LineNum"]
      """  Internal unique identifier for the RebateDtl table  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.Void:bool = obj["Void"]
      """  Indicates if the customer is no longer participating in the Rebate  """  
      self.PaidAmount:int = obj["PaidAmount"]
      """  Total amount of rebate paid to date  """  
      self.AccruedAmount:int = obj["AccruedAmount"]
      """  Amount of rebate that has been earned  """  
      self.AccruedQty:int = obj["AccruedQty"]
      """  Total Invoice Quantity Accrued toward Rebate  """  
      self.UOMCode:str = obj["UOMCode"]
      """  AccuredQty Unit of Measure  """  
      self.AccruedTot:int = obj["AccruedTot"]
      """  Total Invoice Amount accrued towards rebate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BalanceAmount:int = obj["BalanceAmount"]
      """  AccruedAmount less PaidAmount  """  
      self.ProdCodeDesc:str = obj["ProdCodeDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RebateDtlProdCode:str = obj["RebateDtlProdCode"]
      self.RebateDtlPartNum:str = obj["RebateDtlPartNum"]
      self.RebateDtlUOMCode:str = obj["RebateDtlUOMCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RebateCustRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.FixedDisc:int = obj["FixedDisc"]
      """  Populated from the Customer's Terms code.  Discount to reduce invoice amount by before applying the rebate discount  """  
      self.Void:bool = obj["Void"]
      """  Indicates if the customer is no longer participating in the Rebate  """  
      self.PaidAmount:int = obj["PaidAmount"]
      """  Total amount of rebate paid to date  """  
      self.AccruedAmount:int = obj["AccruedAmount"]
      """  Amount of rebate that has been earned  """  
      self.RebateForm:str = obj["RebateForm"]
      """  Indicates if the rebate should be a Check or a Credit Memo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BalanceAmount:int = obj["BalanceAmount"]
      """  Amount remaining between Accrued amount and paid amount  """  
      self.GroupCode:str = obj["GroupCode"]
      self.RebateSuppID:str = obj["RebateSuppID"]
      """  Rebate Supplier ID  """  
      self.VendorName:str = obj["VendorName"]
      """  Rebate Supplier Name  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RebateDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.LineNum:int = obj["LineNum"]
      """  Internal unique identifier for the RebateDtl table  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  """  
      self.Void:bool = obj["Void"]
      """  Part/PartClass is no longer a part of the Rebate  """  
      self.PaidAmount:int = obj["PaidAmount"]
      """  Total amount of rebate paid to date  """  
      self.AccruedAmount:int = obj["AccruedAmount"]
      """  Amount of rebate that has been earned  """  
      self.BreakType:str = obj["BreakType"]
      """  Indicates whether the BreakMin for the levels is a quantity or Amount.  """  
      self.UOMCode:str = obj["UOMCode"]
      """  Unit of Measure  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BalanceAmount:int = obj["BalanceAmount"]
      """  Accrued Amount less Paid Amount  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.ProdGrupDescription:str = obj["ProdGrupDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RebateHdrAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RebateID:str = obj["RebateID"]
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

class Erp_Tablesets_RebateHdrListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.RebateDesc:str = obj["RebateDesc"]
      """  Rebate Description  """  
      self.StartDate:str = obj["StartDate"]
      """  Starting Date of the Rebate  """  
      self.EndDate:str = obj["EndDate"]
      """  End Date of the Rebate  """  
      self.GraceDays:int = obj["GraceDays"]
      """  Number of days after the end date before a rebate check can be processed  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Rebate is active or not  """  
      self.PaidAmount:int = obj["PaidAmount"]
      """  Total amount of rebate paid to date  """  
      self.AccruedAmount:int = obj["AccruedAmount"]
      """  Amount of rebate that has been earned  """  
      self.CustNum:int = obj["CustNum"]
      """  If the Rebate is to be paid to one customer use this Customer.  If this is 0 then a Rebate will go to each customer in the Rebate  """  
      self.AccrualType:str = obj["AccrualType"]
      """  Generate Rebate Transactions based on Invoices or Payments  """  
      self.BillToFlag:bool = obj["BillToFlag"]
      """  If checked, the Invoice Bill to number will be looked at otherwise the soldTo customer number is used for the rebate  """  
      self.RebateForm:str = obj["RebateForm"]
      """  Indicates if the rebate should be a Check or a Credit Memo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BalanceAmount:int = obj["BalanceAmount"]
      """  Accrued Amount less Paid Amount  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RebateHdrListTableset:
   def __init__(self, obj):
      self.RebateHdrList:list[Erp_Tablesets_RebateHdrListRow] = obj["RebateHdrList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RebateHdrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.RebateDesc:str = obj["RebateDesc"]
      """  Rebate Description  """  
      self.StartDate:str = obj["StartDate"]
      """  Starting Date of the Rebate  """  
      self.EndDate:str = obj["EndDate"]
      """  End Date of the Rebate  """  
      self.GraceDays:int = obj["GraceDays"]
      """  Number of days after the end date before a rebate check can be processed  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Rebate is active or not  """  
      self.PaidAmount:int = obj["PaidAmount"]
      """  Total amount of rebate paid to date  """  
      self.AccruedAmount:int = obj["AccruedAmount"]
      """  Amount of rebate that has been earned  """  
      self.CustNum:int = obj["CustNum"]
      """  If the Rebate is to be paid to one customer use this Customer.  If this is 0 then a Rebate will go to each customer in the Rebate  """  
      self.AccrualType:str = obj["AccrualType"]
      """  Generate Rebate Transactions based on Invoices or Payments  """  
      self.BillToFlag:bool = obj["BillToFlag"]
      """  If checked, the Invoice Bill to number will be looked at otherwise the soldTo customer number is used for the rebate  """  
      self.RebateForm:str = obj["RebateForm"]
      """  Indicates if the rebate should be a Check or a Credit Memo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BalanceAmount:int = obj["BalanceAmount"]
      """  Accrued Amount less Paid Amount  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RebatePymtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.PymtDate:str = obj["PymtDate"]
      """  Date to generate the rebate on  """  
      self.Generated:bool = obj["Generated"]
      """  Flag to indicate if the rebates have been generated  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates that the transactions for the rebate have been approved and the check/credit memo can be created  """  
      self.Pulled:bool = obj["Pulled"]
      """  Indicates if the Rebate has been pulled into AR.  If yes, the next pull will ignore the group.  """  
      self.APPulled:bool = obj["APPulled"]
      """  Indicates if the Rebate has been pulled into AP.  If yes, the next pull will ignore the group.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RebateTableset:
   def __init__(self, obj):
      self.RebateHdr:list[Erp_Tablesets_RebateHdrRow] = obj["RebateHdr"]
      self.RebateHdrAttch:list[Erp_Tablesets_RebateHdrAttchRow] = obj["RebateHdrAttch"]
      self.RebateCust:list[Erp_Tablesets_RebateCustRow] = obj["RebateCust"]
      self.RebateCustDtl:list[Erp_Tablesets_RebateCustDtlRow] = obj["RebateCustDtl"]
      self.RebateDtl:list[Erp_Tablesets_RebateDtlRow] = obj["RebateDtl"]
      self.RebateBrk:list[Erp_Tablesets_RebateBrkRow] = obj["RebateBrk"]
      self.RebatePymt:list[Erp_Tablesets_RebatePymtRow] = obj["RebatePymt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtRebateTableset:
   def __init__(self, obj):
      self.RebateHdr:list[Erp_Tablesets_RebateHdrRow] = obj["RebateHdr"]
      self.RebateHdrAttch:list[Erp_Tablesets_RebateHdrAttchRow] = obj["RebateHdrAttch"]
      self.RebateCust:list[Erp_Tablesets_RebateCustRow] = obj["RebateCust"]
      self.RebateCustDtl:list[Erp_Tablesets_RebateCustDtlRow] = obj["RebateCustDtl"]
      self.RebateDtl:list[Erp_Tablesets_RebateDtlRow] = obj["RebateDtl"]
      self.RebateBrk:list[Erp_Tablesets_RebateBrkRow] = obj["RebateBrk"]
      self.RebatePymt:list[Erp_Tablesets_RebatePymtRow] = obj["RebatePymt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   rebateID
   """  
   def __init__(self, obj):
      self.rebateID:str = obj["rebateID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RebateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RebateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RebateTableset] = obj["returnObj"]
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

class GetCustGroup_input:
   """ Required : 
   rebateID
   groupCode
   pRebateForm
   """  
   def __init__(self, obj):
      self.rebateID:str = obj["rebateID"]
      """  Rebate ID  """  
      self.groupCode:str = obj["groupCode"]
      """  Customer Group Code  """  
      self.pRebateForm:str = obj["pRebateForm"]
      """  Rebate Form when Rebate Supplier is empty  """  
      pass

class GetCustGroup_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RebateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RebateHdrListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewRebateBrk_input:
   """ Required : 
   ds
   rebateID
   lineNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      self.rebateID:str = obj["rebateID"]
      self.lineNum:int = obj["lineNum"]
      pass

class GetNewRebateBrk_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRebateCustDtl_input:
   """ Required : 
   ds
   rebateID
   lineNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      self.rebateID:str = obj["rebateID"]
      self.lineNum:int = obj["lineNum"]
      pass

class GetNewRebateCustDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRebateCust_input:
   """ Required : 
   ds
   rebateID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      self.rebateID:str = obj["rebateID"]
      pass

class GetNewRebateCust_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRebateDtl_input:
   """ Required : 
   ds
   rebateID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      self.rebateID:str = obj["rebateID"]
      pass

class GetNewRebateDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRebateHdrAttch_input:
   """ Required : 
   ds
   rebateID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      self.rebateID:str = obj["rebateID"]
      pass

class GetNewRebateHdrAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRebateHdr_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

class GetNewRebateHdr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRebatePymt_input:
   """ Required : 
   ds
   rebateID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      self.rebateID:str = obj["rebateID"]
      pass

class GetNewRebatePymt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseRebateHdr
   whereClauseRebateHdrAttch
   whereClauseRebateCust
   whereClauseRebateCustDtl
   whereClauseRebateDtl
   whereClauseRebateBrk
   whereClauseRebatePymt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRebateHdr:str = obj["whereClauseRebateHdr"]
      self.whereClauseRebateHdrAttch:str = obj["whereClauseRebateHdrAttch"]
      self.whereClauseRebateCust:str = obj["whereClauseRebateCust"]
      self.whereClauseRebateCustDtl:str = obj["whereClauseRebateCustDtl"]
      self.whereClauseRebateDtl:str = obj["whereClauseRebateDtl"]
      self.whereClauseRebateBrk:str = obj["whereClauseRebateBrk"]
      self.whereClauseRebatePymt:str = obj["whereClauseRebatePymt"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RebateTableset] = obj["returnObj"]
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

class OnChangePymtDate_input:
   """ Required : 
   ipProposedPymtDate
   ds
   """  
   def __init__(self, obj):
      self.ipProposedPymtDate:str = obj["ipProposedPymtDate"]
      """  The new proposed RebatePymt.PymtDate value  """  
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

class OnChangePymtDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRebateTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRebateTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RebateTableset] = obj["ds"]
      pass

      """  output parameters  """  

