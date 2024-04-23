import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.AlcHedSvc
# Description: class AlcHedSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_AlcHeds(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcHeds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHeds
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds",headers=creds) as resp:
           return await resp.json()

async def post_AlcHeds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHeds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcHeds_Company_AllocID(Company, AllocID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHed item
   Description: Calls GetByID to retrieve the AlcHed item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcHeds_Company_AllocID(Company, AllocID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcHed for the service
   Description: Calls UpdateExt to update AlcHed. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcHeds_Company_AllocID(Company, AllocID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcHed item
   Description: Call UpdateExt to delete AlcHed item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHeds_Company_AllocID_AlcAccts(Company, AllocID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcAccts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcAccts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcAccts",headers=creds) as resp:
           return await resp.json()

async def get_AlcHeds_Company_AllocID_AlcAccts_Company_AllocID_ParamNbr_AllocGLAcct(Company, AllocID, ParamNbr, AllocGLAcct, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcAcct item
   Description: Calls GetByID to retrieve the AlcAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcAcct1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param AllocGLAcct: Desc: AllocGLAcct   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcAccts(" + Company + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHeds_Company_AllocID_AlcAcctCats(Company, AllocID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcAcctCats items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcAcctCats1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcAcctCatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcAcctCats",headers=creds) as resp:
           return await resp.json()

async def get_AlcHeds_Company_AllocID_AlcAcctCats_Company_AllocID_ParamNbr_CategoryID(Company, AllocID, ParamNbr, CategoryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcAcctCat item
   Description: Calls GetByID to retrieve the AlcAcctCat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcAcctCat1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param CategoryID: Desc: CategoryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcAcctCatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcAcctCats(" + Company + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHeds_Company_AllocID_AlcJrnCds(Company, AllocID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcJrnCds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcJrnCds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcJrnCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcJrnCds",headers=creds) as resp:
           return await resp.json()

async def get_AlcHeds_Company_AllocID_AlcJrnCds_Company_AllocID_ParamNbr_JournalCode(Company, AllocID, ParamNbr, JournalCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcJrnCd item
   Description: Calls GetByID to retrieve the AlcJrnCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcJrnCd1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcJrnCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcJrnCds(" + Company + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHeds_Company_AllocID_AlcParams(Company, AllocID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcParams1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcParams",headers=creds) as resp:
           return await resp.json()

async def get_AlcHeds_Company_AllocID_AlcParams_Company_AllocID_ParamNbr(Company, AllocID, ParamNbr, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcParam item
   Description: Calls GetByID to retrieve the AlcParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcParam1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcParams(" + Company + "," + AllocID + "," + ParamNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHeds_Company_AllocID_AlcRanges(Company, AllocID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcRanges items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcRanges1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcRangeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcRanges",headers=creds) as resp:
           return await resp.json()

async def get_AlcHeds_Company_AllocID_AlcRanges_Company_AllocID_ParamNbr_SegmentNbr(Company, AllocID, ParamNbr, SegmentNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcRange item
   Description: Calls GetByID to retrieve the AlcRange item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcRange1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcRangeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcRanges(" + Company + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHeds_Company_AllocID_AlcTargets(Company, AllocID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcTargets items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcTargets1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcTargetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcTargets",headers=creds) as resp:
           return await resp.json()

async def get_AlcHeds_Company_AllocID_AlcTargets_Company_AllocID_AllocTgtNbr(Company, AllocID, AllocTgtNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcTarget item
   Description: Calls GetByID to retrieve the AlcTarget item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcTarget1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcTargetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcHeds(" + Company + "," + AllocID + ")/AlcTargets(" + Company + "," + AllocID + "," + AllocTgtNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcAccts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcAccts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAccts",headers=creds) as resp:
           return await resp.json()

async def post_AlcAccts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcAccts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAccts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcAccts_Company_AllocID_ParamNbr_AllocGLAcct(Company, AllocID, ParamNbr, AllocGLAcct, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcAcct item
   Description: Calls GetByID to retrieve the AlcAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param AllocGLAcct: Desc: AllocGLAcct   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAccts(" + Company + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcAccts_Company_AllocID_ParamNbr_AllocGLAcct(Company, AllocID, ParamNbr, AllocGLAcct, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcAcct for the service
   Description: Calls UpdateExt to update AlcAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param AllocGLAcct: Desc: AllocGLAcct   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAccts(" + Company + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcAccts_Company_AllocID_ParamNbr_AllocGLAcct(Company, AllocID, ParamNbr, AllocGLAcct, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcAcct item
   Description: Call UpdateExt to delete AlcAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param AllocGLAcct: Desc: AllocGLAcct   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAccts(" + Company + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcAcctCats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcAcctCats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcAcctCats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcAcctCatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAcctCats",headers=creds) as resp:
           return await resp.json()

async def post_AlcAcctCats(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcAcctCats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcAcctCatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcAcctCatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAcctCats", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcAcctCats_Company_AllocID_ParamNbr_CategoryID(Company, AllocID, ParamNbr, CategoryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcAcctCat item
   Description: Calls GetByID to retrieve the AlcAcctCat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcAcctCat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param CategoryID: Desc: CategoryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcAcctCatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAcctCats(" + Company + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcAcctCats_Company_AllocID_ParamNbr_CategoryID(Company, AllocID, ParamNbr, CategoryID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcAcctCat for the service
   Description: Calls UpdateExt to update AlcAcctCat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcAcctCat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param CategoryID: Desc: CategoryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcAcctCatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAcctCats(" + Company + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcAcctCats_Company_AllocID_ParamNbr_CategoryID(Company, AllocID, ParamNbr, CategoryID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcAcctCat item
   Description: Call UpdateExt to delete AlcAcctCat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcAcctCat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param CategoryID: Desc: CategoryID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcAcctCats(" + Company + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcJrnCds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcJrnCds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcJrnCds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcJrnCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcJrnCds",headers=creds) as resp:
           return await resp.json()

async def post_AlcJrnCds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcJrnCds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcJrnCdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcJrnCdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcJrnCds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcJrnCds_Company_AllocID_ParamNbr_JournalCode(Company, AllocID, ParamNbr, JournalCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcJrnCd item
   Description: Calls GetByID to retrieve the AlcJrnCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcJrnCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcJrnCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcJrnCds(" + Company + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcJrnCds_Company_AllocID_ParamNbr_JournalCode(Company, AllocID, ParamNbr, JournalCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcJrnCd for the service
   Description: Calls UpdateExt to update AlcJrnCd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcJrnCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcJrnCdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcJrnCds(" + Company + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcJrnCds_Company_AllocID_ParamNbr_JournalCode(Company, AllocID, ParamNbr, JournalCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcJrnCd item
   Description: Call UpdateExt to delete AlcJrnCd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcJrnCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcJrnCds(" + Company + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcParams(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcParams
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams",headers=creds) as resp:
           return await resp.json()

async def post_AlcParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcParamsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcParamsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcParams_Company_AllocID_ParamNbr(Company, AllocID, ParamNbr, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcParam item
   Description: Calls GetByID to retrieve the AlcParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams(" + Company + "," + AllocID + "," + ParamNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcParams_Company_AllocID_ParamNbr(Company, AllocID, ParamNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcParam for the service
   Description: Calls UpdateExt to update AlcParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcParamsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams(" + Company + "," + AllocID + "," + ParamNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcParams_Company_AllocID_ParamNbr(Company, AllocID, ParamNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcParam item
   Description: Call UpdateExt to delete AlcParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams(" + Company + "," + AllocID + "," + ParamNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcParams_Company_AllocID_ParamNbr_AlcNFSrcs(Company, AllocID, ParamNbr, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcNFSrcs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcNFSrcs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcNFSrcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams(" + Company + "," + AllocID + "," + ParamNbr + ")/AlcNFSrcs",headers=creds) as resp:
           return await resp.json()

async def get_AlcParams_Company_AllocID_ParamNbr_AlcNFSrcs_Company_AllocID_ParamNbr_SrcSeqNbr(Company, AllocID, ParamNbr, SrcSeqNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcNFSrc item
   Description: Calls GetByID to retrieve the AlcNFSrc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcNFSrc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SrcSeqNbr: Desc: SrcSeqNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcNFSrcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams(" + Company + "," + AllocID + "," + ParamNbr + ")/AlcNFSrcs(" + Company + "," + AllocID + "," + ParamNbr + "," + SrcSeqNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcParams_Company_AllocID_ParamNbr_AlcParamsBAQs(Company, AllocID, ParamNbr, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcParamsBAQs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcParamsBAQs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcParamsBAQRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams(" + Company + "," + AllocID + "," + ParamNbr + ")/AlcParamsBAQs",headers=creds) as resp:
           return await resp.json()

async def get_AlcParams_Company_AllocID_ParamNbr_AlcParamsBAQs_Company_AllocID_ParamNbr_BAQExportID_BAQParamValNbr(Company, AllocID, ParamNbr, BAQExportID, BAQParamValNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcParamsBAQ item
   Description: Calls GetByID to retrieve the AlcParamsBAQ item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcParamsBAQ1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param BAQExportID: Desc: BAQExportID   Required: True   Allow empty value : True
      :param BAQParamValNbr: Desc: BAQParamValNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcParamsBAQRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParams(" + Company + "," + AllocID + "," + ParamNbr + ")/AlcParamsBAQs(" + Company + "," + AllocID + "," + ParamNbr + "," + BAQExportID + "," + BAQParamValNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcNFSrcs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcNFSrcs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcNFSrcs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcNFSrcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcNFSrcs",headers=creds) as resp:
           return await resp.json()

async def post_AlcNFSrcs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcNFSrcs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcNFSrcRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcNFSrcRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcNFSrcs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcNFSrcs_Company_AllocID_ParamNbr_SrcSeqNbr(Company, AllocID, ParamNbr, SrcSeqNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcNFSrc item
   Description: Calls GetByID to retrieve the AlcNFSrc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcNFSrc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SrcSeqNbr: Desc: SrcSeqNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcNFSrcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcNFSrcs(" + Company + "," + AllocID + "," + ParamNbr + "," + SrcSeqNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcNFSrcs_Company_AllocID_ParamNbr_SrcSeqNbr(Company, AllocID, ParamNbr, SrcSeqNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcNFSrc for the service
   Description: Calls UpdateExt to update AlcNFSrc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcNFSrc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SrcSeqNbr: Desc: SrcSeqNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcNFSrcRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcNFSrcs(" + Company + "," + AllocID + "," + ParamNbr + "," + SrcSeqNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcNFSrcs_Company_AllocID_ParamNbr_SrcSeqNbr(Company, AllocID, ParamNbr, SrcSeqNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcNFSrc item
   Description: Call UpdateExt to delete AlcNFSrc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcNFSrc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SrcSeqNbr: Desc: SrcSeqNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcNFSrcs(" + Company + "," + AllocID + "," + ParamNbr + "," + SrcSeqNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcParamsBAQs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcParamsBAQs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcParamsBAQs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcParamsBAQRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParamsBAQs",headers=creds) as resp:
           return await resp.json()

async def post_AlcParamsBAQs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcParamsBAQs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcParamsBAQRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcParamsBAQRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParamsBAQs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcParamsBAQs_Company_AllocID_ParamNbr_BAQExportID_BAQParamValNbr(Company, AllocID, ParamNbr, BAQExportID, BAQParamValNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcParamsBAQ item
   Description: Calls GetByID to retrieve the AlcParamsBAQ item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcParamsBAQ
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param BAQExportID: Desc: BAQExportID   Required: True   Allow empty value : True
      :param BAQParamValNbr: Desc: BAQParamValNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcParamsBAQRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParamsBAQs(" + Company + "," + AllocID + "," + ParamNbr + "," + BAQExportID + "," + BAQParamValNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcParamsBAQs_Company_AllocID_ParamNbr_BAQExportID_BAQParamValNbr(Company, AllocID, ParamNbr, BAQExportID, BAQParamValNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcParamsBAQ for the service
   Description: Calls UpdateExt to update AlcParamsBAQ. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcParamsBAQ
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param BAQExportID: Desc: BAQExportID   Required: True   Allow empty value : True
      :param BAQParamValNbr: Desc: BAQParamValNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcParamsBAQRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParamsBAQs(" + Company + "," + AllocID + "," + ParamNbr + "," + BAQExportID + "," + BAQParamValNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcParamsBAQs_Company_AllocID_ParamNbr_BAQExportID_BAQParamValNbr(Company, AllocID, ParamNbr, BAQExportID, BAQParamValNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcParamsBAQ item
   Description: Call UpdateExt to delete AlcParamsBAQ item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcParamsBAQ
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param BAQExportID: Desc: BAQExportID   Required: True   Allow empty value : True
      :param BAQParamValNbr: Desc: BAQParamValNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcParamsBAQs(" + Company + "," + AllocID + "," + ParamNbr + "," + BAQExportID + "," + BAQParamValNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcRanges(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcRanges items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcRanges
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcRangeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcRanges",headers=creds) as resp:
           return await resp.json()

async def post_AlcRanges(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcRanges
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcRangeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcRangeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcRanges", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcRanges_Company_AllocID_ParamNbr_SegmentNbr(Company, AllocID, ParamNbr, SegmentNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcRange item
   Description: Calls GetByID to retrieve the AlcRange item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcRange
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcRangeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcRanges(" + Company + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcRanges_Company_AllocID_ParamNbr_SegmentNbr(Company, AllocID, ParamNbr, SegmentNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcRange for the service
   Description: Calls UpdateExt to update AlcRange. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcRange
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcRangeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcRanges(" + Company + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcRanges_Company_AllocID_ParamNbr_SegmentNbr(Company, AllocID, ParamNbr, SegmentNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcRange item
   Description: Call UpdateExt to delete AlcRange item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcRange
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcRanges(" + Company + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcTargets(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcTargets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcTargets
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcTargetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcTargets",headers=creds) as resp:
           return await resp.json()

async def post_AlcTargets(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcTargets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcTargetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcTargetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcTargets", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcTargets_Company_AllocID_AllocTgtNbr(Company, AllocID, AllocTgtNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcTarget item
   Description: Calls GetByID to retrieve the AlcTarget item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcTarget
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcTargetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcTargets(" + Company + "," + AllocID + "," + AllocTgtNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcTargets_Company_AllocID_AllocTgtNbr(Company, AllocID, AllocTgtNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcTarget for the service
   Description: Calls UpdateExt to update AlcTarget. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcTarget
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcTargetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcTargets(" + Company + "," + AllocID + "," + AllocTgtNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcTargets_Company_AllocID_AllocTgtNbr(Company, AllocID, AllocTgtNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcTarget item
   Description: Call UpdateExt to delete AlcTarget item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcTarget
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/AlcTargets(" + Company + "," + AllocID + "," + AllocTgtNbr + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHedListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAlcHed, whereClauseAlcAcct, whereClauseAlcAcctCat, whereClauseAlcJrnCd, whereClauseAlcParams, whereClauseAlcNFSrc, whereClauseAlcParamsBAQ, whereClauseAlcRange, whereClauseAlcTarget, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAlcHed=" + whereClauseAlcHed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcAcct=" + whereClauseAlcAcct
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcAcctCat=" + whereClauseAlcAcctCat
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcJrnCd=" + whereClauseAlcJrnCd
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcParams=" + whereClauseAlcParams
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcNFSrc=" + whereClauseAlcNFSrc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcParamsBAQ=" + whereClauseAlcParamsBAQ
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcRange=" + whereClauseAlcRange
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcTarget=" + whereClauseAlcTarget
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(allocID, epicorHeaders = None):
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
   params += "allocID=" + allocID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_getExternalMasterCOA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getExternalMasterCOA
   Description: Purpose:  Get the Master COA from the proposted External Company
Parameters:  ProposedExtCompID
   OperationID: getExternalMasterCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getExternalMasterCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getExternalMasterCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeExtCompanyID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeExtCompanyID
   Description: This method resets the regular and Multi-Company G/L Accounts and the Reference Codes
when the External Company ID changes.
Parameters:
<param name="ProposedExtCompID">Proposed company ID</param><param name="allocID">AllocID from the AlcHed</param><param name="ds">The GL Journal Entry data set </param>
Notes:
   OperationID: ChangeExtCompanyID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeExtCompanyID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeExtCompanyID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_createNewBAQParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method createNewBAQParams
   Description: Purpose:called when BAQExportID is changed
Parameters:
<param name="ipBAQExportID">BAQ identifier</param><param name="ipAllocID">Allocation code</param><param name="ipParamNbr">Formula parameter number</param><param name="ds">GL Allocations Data Set</param>
Notes:
   OperationID: createNewBAQParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/createNewBAQParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/createNewBAQParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAllocOption(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAllocOption
   Description: Purpose:warn user if targets exist
Parameters:
<param name="ipProposedAllocOption">proposed allocation option</param><param name="ds">GL Allocations Data Set</param><param name="opWarningMessage">warning message</param>
Notes:
   OperationID: ChangeAllocOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAllocOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAllocOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAllocationType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAllocationType
   Description: Purpose:warn user if targets exist
Parameters:
<param name="ipProposedAllocType">proposed allocation type</param><param name="ds">GL Allocations Data Set</param>
Notes:
   OperationID: ChangeAllocationType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAllocationType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAllocationType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBAQEntryType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBAQEntryType
   Description: Purpose:
Parameters:
<param name="ds">GL Allocations Data Set</param>
   OperationID: ChangeBAQEntryType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBAQEntryType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBAQEntryType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLookupEntryType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLookupEntryType
   Description: Purpose:
Parameters:
<param name="ipAllocID">Allocation code</param><param name="ipParamNbr">Parameter number</param><param name="ipSrcSeqNbr">Source srquence number</param><param name="ds">GL Allocations Data Set</param>
   OperationID: ChangeLookupEntryType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLookupEntryType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLookupEntryType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckArgument(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckArgument
   Description: Validate Argument1 and Argument2 values and return the values in the rigth format.
   OperationID: CheckArgument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckArgument_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckArgument_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBAQExportID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBAQExportID
   Description: Validate BAQ Export ID
   OperationID: CheckBAQExportID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBAQExportID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBAQExportID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBAQParameter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBAQParameter
   Description: Purpose:  Validate the parameter field is a valid BAQ parameter
Parameters:
<param name="ipBAQExportID">ipBAQExportID">BAQ to validate the parameter</param><param name="ipFieldName">Field to validate</param>
Notes:
   OperationID: CheckBAQParameter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBAQParameter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBAQParameter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBAQParameterValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBAQParameterValue
   Description: Purpose:  validate the value entered for the query field to ensure it is a valid type
Parameters:
<param name="ipBAQExportID">ipBAQExportID">BAQ to validate the parameter</param><param name="ipFieldName">Field to validate</param><param name="ipValue">query field value to validate</param>
Notes:
   OperationID: CheckBAQParameterValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBAQParameterValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBAQParameterValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBook
   Description: Validate the selected book is valid and of type standard
   OperationID: CheckBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCanAddNewTarget(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCanAddNewTarget
   Description: Purpose: If fixedvalue and current sum of percent equals total then do not allow add
Parameters:
<param name="ipAllocID">Allocation Code</param>
Notes:
   OperationID: CheckCanAddNewTarget
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCanAddNewTarget_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCanAddNewTarget_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCategory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCategory
   Description: Validate Category
   OperationID: CheckCategory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCategory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCategory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckForDuplicateAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckForDuplicateAccount
   Description: Purpose:  Ensure an account is only entered once as a source
Parameters:
<param name="ipGLAccount">proposed GL Account</param><param name="ipParamNbr">parameter nbr</param><param name="ipAllocID">allocation id</param>
   OperationID: CheckForDuplicateAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForDuplicateAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForDuplicateAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckJournalCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckJournalCode
   Description: Validate Journal Code
   OperationID: CheckJournalCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckJournalCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckJournalCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckMinMax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckMinMax
   Description: Validate Min and max values
   OperationID: CheckMinMax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckMinMax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckMinMax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckParamName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckParamName
   Description: Validate parameter name is not a valid math operator.
   OperationID: CheckParamName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckParamName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckParamName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckParamOption(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckParamOption
   Description: Purpose:
Parameters:  none
<param name="ipAllocID">Allocation code</param><param name="ipParamNbr">parameter number</param><param name="ipSrcSeqNbr">Source sequence number</param><param name="ipParamOpt">parameter option</param><param name="ds">GL Allocations Data Set</param>
   OperationID: CheckParamOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckParamOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckParamOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckParamOptionBAQ(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckParamOptionBAQ
   Description: Purpose:
Parameters:  none
<param name="ipParamOpt">parameter option</param><param name="ds">GL Allocations Data Set</param>
   OperationID: CheckParamOptionBAQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckParamOptionBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckParamOptionBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckParamSegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckParamSegment
   Description: Purpose:
Parameters:  none
<param name="ipParamSegmentNbr">parameter option</param><param name="ipParamType">either NonFin or BAQ</param><param name="ds">GL Allocations Data Set</param>
   OperationID: CheckParamSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckParamSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckParamSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPercentageToAllocate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPercentageToAllocate
   Description: Purpose: Warn the user if the percentage to allocate on the allocation code > 100.
Parameters:
<param name="ipAllocID">Allocation Code</param><param name="ipProposedPercentage">percent to allocate</param><param name="opWarnMsg">warning message</param>
Notes:
   OperationID: CheckPercentageToAllocate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPercentageToAllocate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPercentageToAllocate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPriorTgtStamp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPriorTgtStamp
   Description: Purpose:
Parameters:
<param name="ipPriorTgtStamp">proposed source allocation stamp</param><param name="ds">GL Allocations Data Set</param><param name="opWarningMsg">warning message</param>
Notes:
   OperationID: CheckPriorTgtStamp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPriorTgtStamp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPriorTgtStamp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSegmentNbr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSegmentNbr
   Description: This method is to be used in place of GetNewAlcRange.  This method Validates
there are still COA Segments available.
   OperationID: CheckSegmentNbr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSegmentNbr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSegmentNbr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSyntax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSyntax
   Description: Check Syntax for formula field.
   OperationID: CheckSyntax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSyntax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSyntax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTgtStamp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTgtStamp
   Description: Purpose:
Parameters:
<param name="ipTgtStamp">outgoing allocation mark</param><param name="ds">GL Allocations Data Set</param><param name="opWarningMsg">warning message</param>
Notes:
   OperationID: CheckTgtStamp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTgtStamp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTgtStamp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTier(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTier
   Description: Purpose:
Parameters:
<param name="ipTier">proposed tier</param><param name="ds">GL Allocations Data Set</param>
Notes:
   OperationID: CheckTier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTier_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTotalPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTotalPercent
   Description: Purpose:
Parameters:
<param name="ipProposedPercent">Proposed percent</param><param name="ds">GL Allocations Data Set</param><param name="opTotalPercent">Total percent</param>
Notes:
   OperationID: CheckTotalPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTotalPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTotalPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateAlcNFSrcRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateAlcNFSrcRecords
   Description: Create Source Fields Records for the selected MapUID
   OperationID: CreateAlcNFSrcRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateAlcNFSrcRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateAlcNFSrcRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLinkList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLinkList
   Description: Returns a List of valid values for the cmbLinkUID Combo-box
   OperationID: GetLinkList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLinkList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLinkList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLookupSrcCodeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLookupSrcCodeID
   Description: Returns the Source Field Code in Invariant Format
   OperationID: GetLookupSrcCodeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLookupSrcCodeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLookupSrcCodeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcNFSrc1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcNFSrc1
   Description: This method is to be used in place of GetNewAlcNFSrc.  This method Validates
that only one AlcNFSrc record is created for each AlcParam record created.
   OperationID: GetNewAlcNFSrc1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcNFSrc1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcNFSrc1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcRange1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcRange1
   Description: This method is to be used in place of GetNewAlcRange.  This method Validates
there are still COA Segments available.
   OperationID: GetNewAlcRange1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcRange1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcRange1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOperatorsList(epicorHeaders = None):
   """  
   Summary: Invoke method GetOperatorsList
   Description: Return a list of valid operators in a format ready to be use on a combo-box
   OperationID: GetOperatorsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOperatorsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetOperatorsMenuList(epicorHeaders = None):
   """  
   Summary: Invoke method GetOperatorsMenuList
   Description: Return a list of valid operators in a format ready to be use on the context Menu
(i.e - +'Operators~-'Operators~*'Operators~/'Operators~('Operators~)'Operators
   OperationID: GetOperatorsMenuList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOperatorsMenuList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetParametersList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetParametersList
   Description: Return a list of available parameters in a format ready to be use on a combo-box
   OperationID: GetParametersList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetParametersList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParametersList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetParamMenuList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetParamMenuList
   Description: Return a list of available parameters in a format ready to be use on the context Menu
   OperationID: GetParamMenuList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetParamMenuList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParamMenuList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshAllocationTotals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshAllocationTotals
   Description: Purpose:
Parameters:
<param name="ds">GL Allocations Data Set</param>
Notes:
   OperationID: RefreshAllocationTotals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshAllocationTotals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshAllocationTotals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RetrieveGLAcctDesc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RetrieveGLAcctDesc
   Description: Purpose:
<param name="ipType">source or target</param><param name="ds">GL Allocations Data Set</param>
Notes: Do not use, method is obsolete since 11.2.100. DisplayGLAccountDesc field is obsolete in object. Please use GLAcctDispAccountDesc field.
   OperationID: RetrieveGLAcctDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrieveGLAcctDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveGLAcctDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateAcctBalAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateAcctBalAcct
   Description: Updates Account Balance Account.
   OperationID: UpdateAcctBalAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAcctBalAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAcctBalAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePercentTotals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePercentTotals
   Description: Purpose:  warn the user if the sum of the AlcTarget.RatioValue != AlcHed.PercentToAllocate
Parameters:
<param name="ipAllocID">allocation id</param><param name="opWarnMsg">warning message</param>
Notes:
   OperationID: ValidatePercentTotals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePercentTotals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePercentTotals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidTgtNatSegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidTgtNatSegment
   Description: Purpose:  warn the user if Natural Segment Statistical option not set to Both
Parameters:
<param name="ipSegment">COA Segment Value to validate</param><param name="ipAllocID">Allocation Code</param><param name="opWarnMsg">warning message</param>
Notes:
   OperationID: ValidTgtNatSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidTgtNatSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidTgtNatSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidParamNatSegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidParamNatSegment
   Description: Purpose:  warn the user if Natural Segment Statistical option is set to No
Parameters:
<param name="ipSegment">COA Segment Value to validate</param><param name="ipAllocID">Allocation Code</param><param name="ipParamNbr">Parameter number</param><param name="opWarnMsg">warning message</param>
Notes:
   OperationID: ValidParamNatSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidParamNatSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidParamNatSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MaskValidate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MaskValidate
   Description: Test if account masks are valid
   OperationID: MaskValidate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MaskValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MaskValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcAcct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcAcctCat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcAcctCat
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcAcctCat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcAcctCat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcAcctCat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcJrnCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcJrnCd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcJrnCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcJrnCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcJrnCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcParams
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcNFSrc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcNFSrc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcNFSrc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcNFSrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcNFSrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcParamsBAQ(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcParamsBAQ
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcParamsBAQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcParamsBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcParamsBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcRange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcRange
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcTarget(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcTarget
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcTarget
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcTarget_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcTarget_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcAcctCatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcAcctCatRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcAcctRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcAcctRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHedListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcHedListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcHedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcJrnCdRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcJrnCdRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcNFSrcRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcNFSrcRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcParamsBAQRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcParamsBAQRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcParamsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcParamsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcRangeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcRangeRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcTargetRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcTargetRow] = obj["value"]
      pass

class Erp_Tablesets_AlcAcctCatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """   Intended for internal use only to keep the records unique.  The ParamNbr value is 0  when tied to a source account (AlcHed).
When tied to a parameter criteria (AlcParams) it inherits its value from AlcParams table.  """  
      self.CategoryID:str = obj["CategoryID"]
      """  Unique identifier of this category of accounts.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AlcAcctCatCOAActCatType:str = obj["AlcAcctCatCOAActCatType"]
      self.AlcAcctCatCOAActCatDescription:str = obj["AlcAcctCatCOAActCatDescription"]
      self.COADescription:str = obj["COADescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """   Intended for internal use only to keep the records unique.  The ParamNbr value is 0  when tied to a source account (AlcHed).
When tied to a parameter criteria (AlcParams) it inherits its value from AlcParams table.  """  
      self.AllocGLAcct:str = obj["AllocGLAcct"]
      """  GL Account or GL Account mask  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.AllocSegValue1:str = obj["AllocSegValue1"]
      """  Allocation Segment Value 1  """  
      self.AllocSegValue2:str = obj["AllocSegValue2"]
      """  Allocation Segment Value 2  """  
      self.AllocSegValue3:str = obj["AllocSegValue3"]
      """  Allocation Segment Value 3  """  
      self.AllocSegValue4:str = obj["AllocSegValue4"]
      """  Allocation Segment Value 4  """  
      self.AllocSegValue5:str = obj["AllocSegValue5"]
      """  Allocation Segment Value 5  """  
      self.AllocSegValue6:str = obj["AllocSegValue6"]
      """  Allocation Segment Value 6  """  
      self.AllocSegValue7:str = obj["AllocSegValue7"]
      """  Allocation Segment Value 7  """  
      self.AllocSegValue8:str = obj["AllocSegValue8"]
      """  Allocation Segment Value 8  """  
      self.AllocSegValue9:str = obj["AllocSegValue9"]
      """  Allocation Segment Value 9  """  
      self.AllocSegValue10:str = obj["AllocSegValue10"]
      """  Allocation Segment Value 10  """  
      self.AllocSegValue11:str = obj["AllocSegValue11"]
      """  Allocation Segment Value 11  """  
      self.AllocSegValue12:str = obj["AllocSegValue12"]
      """  Allocation Segment Value 12  """  
      self.AllocSegValue13:str = obj["AllocSegValue13"]
      """  Allocation Segment Value 13  """  
      self.AllocSegValue14:str = obj["AllocSegValue14"]
      """  Allocation Segment Value 14  """  
      self.AllocSegValue15:str = obj["AllocSegValue15"]
      """  Allocation Segment Value 15  """  
      self.AllocSegValue16:str = obj["AllocSegValue16"]
      """  Allocation Segment Value 16  """  
      self.AllocSegValue17:str = obj["AllocSegValue17"]
      """  Allocation Segment Value 17  """  
      self.AllocSegValue18:str = obj["AllocSegValue18"]
      """  Allocation Segment Value 18  """  
      self.AllocSegValue19:str = obj["AllocSegValue19"]
      """  Allocation Segment Value 19  """  
      self.AllocSegValue20:str = obj["AllocSegValue20"]
      """  Allocation Segment Value 20  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.Description:str = obj["Description"]
      """  Allocation code description.  """  
      self.AllocationType:int = obj["AllocationType"]
      """   Identifies whether or not the allocaiton is balance or transaction based.  1 = Transaction and is the default value.
2 = Balance based.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Tier:int = obj["Tier"]
      """  Allocation tier.  """  
      self.PriorTgtStamp:str = obj["PriorTgtStamp"]
      """  Identifies the allocation stamp to which this allocation is to be applied.  """  
      self.TgtStamp:str = obj["TgtStamp"]
      """  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  """  
      self.SrcAllocStamp:str = obj["SrcAllocStamp"]
      """  Identifies the allocation stamp that was processed by this allocation.  """  
      self.IgnoreStamp:bool = obj["IgnoreStamp"]
      """  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  """  
      self.UseAllStamps:bool = obj["UseAllStamps"]
      """  Yes indicates that all allocation stamps are valid for the allocation code.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.AllocOption:int = obj["AllocOption"]
      """  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  """  
      self.PercentToAlloc:int = obj["PercentToAlloc"]
      """  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  """  
      self.UseAllocUnits:bool = obj["UseAllocUnits"]
      """  Indicates if the allocation units are used.  """  
      self.OffsetAcct:str = obj["OffsetAcct"]
      """  The general ledger account the allocation is to be written off.  """  
      self.OffsetSegVal1:str = obj["OffsetSegVal1"]
      """  Offset Segment Value 1  """  
      self.OffsetSegVal2:str = obj["OffsetSegVal2"]
      """  Offset Segment Value 2  """  
      self.OffsetSegVal3:str = obj["OffsetSegVal3"]
      """  Offset Segment Value 3  """  
      self.OffsetSegVal4:str = obj["OffsetSegVal4"]
      """  Offset Segment Value 4  """  
      self.OffsetSegVal5:str = obj["OffsetSegVal5"]
      """  Offset Segment Value 5  """  
      self.OffsetSegVal6:str = obj["OffsetSegVal6"]
      """  Offset Segment Value 6  """  
      self.OffsetSegVal7:str = obj["OffsetSegVal7"]
      """  Offset Segment Value 7  """  
      self.OffsetSegVal8:str = obj["OffsetSegVal8"]
      """  Offset Segment Value 8  """  
      self.OffsetSegVal9:str = obj["OffsetSegVal9"]
      """  Offset Segment Value 9  """  
      self.OffsetSegVal10:str = obj["OffsetSegVal10"]
      """  Offset Segment Value 10  """  
      self.OffsetSegVal11:str = obj["OffsetSegVal11"]
      """  Offset Segment Value 11  """  
      self.OffsetSegVal12:str = obj["OffsetSegVal12"]
      """  Offset Segment Value 12  """  
      self.OffsetSegVal13:str = obj["OffsetSegVal13"]
      """  Offset Segment Value 13  """  
      self.OffsetSegVal14:str = obj["OffsetSegVal14"]
      """  Offset Segment Value 14  """  
      self.OffsetSegVal15:str = obj["OffsetSegVal15"]
      """  Offset Segment Value 15  """  
      self.OffsetSegVal16:str = obj["OffsetSegVal16"]
      """  Offset Segment Value 16  """  
      self.OffsetSegVal17:str = obj["OffsetSegVal17"]
      """  Offset Segment Value 17  """  
      self.OffsetSegVal18:str = obj["OffsetSegVal18"]
      """  Offset Segment Value 18  """  
      self.OffsetSegVal19:str = obj["OffsetSegVal19"]
      """  Offset Segment Value 19  """  
      self.OffsetSegVal20:str = obj["OffsetSegVal20"]
      """  Offset Segment Value 20  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllocIsRunning:bool = obj["AllocIsRunning"]
      """  Indicates whether or not a allocation is currently executing.  """  
      self.TotalAllocUnits:int = obj["TotalAllocUnits"]
      """  Total allocation units.  This is the sum of the allocation units defined on the targets.  """  
      self.TotalPercentage:int = obj["TotalPercentage"]
      """  his is the sum of the percentage values defined on the targets.  """  
      self.OffsetAcctDesc:str = obj["OffsetAcctDesc"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      """  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The value of this field is the concatenation of the first three controlled display order segments.  For example, if a chart has 5 controlled segments that are displayed in the following order: seg5->seg3->seg4->seg2->seg1, this field contains the concatention of seg5->seg3->seg4 up to th  """  
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      """  Text that describes the account.  """  
      self.GLBookDescription:str = obj["GLBookDescription"]
      """  Descripiton of Book  """  
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.Description:str = obj["Description"]
      """  Allocation code description.  """  
      self.AllocationType:int = obj["AllocationType"]
      """   Identifies whether or not the allocaiton is balance or transaction based.  1 = Transaction and is the default value.
2 = Balance based.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Tier:int = obj["Tier"]
      """  Allocation tier.  """  
      self.PriorTgtStamp:str = obj["PriorTgtStamp"]
      """  Identifies the allocation stamp to which this allocation is to be applied.  """  
      self.TgtStamp:str = obj["TgtStamp"]
      """  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  """  
      self.SrcAllocStamp:str = obj["SrcAllocStamp"]
      """  Identifies the allocation stamp that was processed by this allocation.  """  
      self.IgnoreStamp:bool = obj["IgnoreStamp"]
      """  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  """  
      self.UseAllStamps:bool = obj["UseAllStamps"]
      """  Yes indicates that all allocation stamps are valid for the allocation code.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.AllocOption:int = obj["AllocOption"]
      """  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  """  
      self.PercentToAlloc:int = obj["PercentToAlloc"]
      """  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  """  
      self.UseAllocUnits:bool = obj["UseAllocUnits"]
      """  Indicates if the allocation units are used.  """  
      self.OffsetAcct:str = obj["OffsetAcct"]
      """  The general ledger account the allocation is to be written off.  """  
      self.OffsetSegVal1:str = obj["OffsetSegVal1"]
      """  Offset Segment Value 1  """  
      self.OffsetSegVal2:str = obj["OffsetSegVal2"]
      """  Offset Segment Value 2  """  
      self.OffsetSegVal3:str = obj["OffsetSegVal3"]
      """  Offset Segment Value 3  """  
      self.OffsetSegVal4:str = obj["OffsetSegVal4"]
      """  Offset Segment Value 4  """  
      self.OffsetSegVal5:str = obj["OffsetSegVal5"]
      """  Offset Segment Value 5  """  
      self.OffsetSegVal6:str = obj["OffsetSegVal6"]
      """  Offset Segment Value 6  """  
      self.OffsetSegVal7:str = obj["OffsetSegVal7"]
      """  Offset Segment Value 7  """  
      self.OffsetSegVal8:str = obj["OffsetSegVal8"]
      """  Offset Segment Value 8  """  
      self.OffsetSegVal9:str = obj["OffsetSegVal9"]
      """  Offset Segment Value 9  """  
      self.OffsetSegVal10:str = obj["OffsetSegVal10"]
      """  Offset Segment Value 10  """  
      self.OffsetSegVal11:str = obj["OffsetSegVal11"]
      """  Offset Segment Value 11  """  
      self.OffsetSegVal12:str = obj["OffsetSegVal12"]
      """  Offset Segment Value 12  """  
      self.OffsetSegVal13:str = obj["OffsetSegVal13"]
      """  Offset Segment Value 13  """  
      self.OffsetSegVal14:str = obj["OffsetSegVal14"]
      """  Offset Segment Value 14  """  
      self.OffsetSegVal15:str = obj["OffsetSegVal15"]
      """  Offset Segment Value 15  """  
      self.OffsetSegVal16:str = obj["OffsetSegVal16"]
      """  Offset Segment Value 16  """  
      self.OffsetSegVal17:str = obj["OffsetSegVal17"]
      """  Offset Segment Value 17  """  
      self.OffsetSegVal18:str = obj["OffsetSegVal18"]
      """  Offset Segment Value 18  """  
      self.OffsetSegVal19:str = obj["OffsetSegVal19"]
      """  Offset Segment Value 19  """  
      self.OffsetSegVal20:str = obj["OffsetSegVal20"]
      """  Offset Segment Value 20  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StatBalAsAllocUnits:bool = obj["StatBalAsAllocUnits"]
      """  Indicates if Statistical Balance of Target Account should be used as Allocation Units  """  
      self.AllocIsRunning:bool = obj["AllocIsRunning"]
      """  Indicates whether or not a allocation is currently executing.  """  
      self.TotalAllocUnits:int = obj["TotalAllocUnits"]
      """  Total allocation units.  This is the sum of the allocation units defined on the targets.  """  
      self.TotalPercentage:int = obj["TotalPercentage"]
      """  his is the sum of the percentage values defined on the targets.  """  
      self.OffsetAcctDesc:str = obj["OffsetAcctDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcJrnCdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """   Intended for internal use only to keep the records unique.  The ParamNbr value is 0  when tied to a source account (AlcHed).
When tied to a parameter criteria (AlcParams) it inherits its value from AlcParams table.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      self.JrnlCodeSystemJournal:bool = obj["JrnlCodeSystemJournal"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcNFSrcRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique.  The value is inherited from the AlcParams table.  """  
      self.LookupTblMapUID_obsolete:int = obj["LookupTblMapUID_obsolete"]
      """  LookupTblMapUID_obsolete  """  
      self.TgtSeqNbr_obsolete:int = obj["TgtSeqNbr_obsolete"]
      """  TgtSeqNbr_obsolete  """  
      self.LinkUID_obsolete:int = obj["LinkUID_obsolete"]
      """  LinkUID_obsolete  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.ParamOpt:int = obj["ParamOpt"]
      """   Identifes the option for the BAQ parameter.
1 = Use Target Account Segment.  
2 = Use Source Account Segment
3 = Use Allocation Run Start Date
4 = Use allocation Run End Date  """  
      self.ParamSegmentNbr:int = obj["ParamSegmentNbr"]
      """  Identifies the segment number to use to determine the segment code that will be used to look up the result value in the lookup table.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.EntryType:int = obj["EntryType"]
      """  Identifies if the parameter is an actual value or an option.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SrcSeqNbr:int = obj["SrcSeqNbr"]
      """  SrcSeqNbr  """  
      self.SrcCodeID:str = obj["SrcCodeID"]
      """  SrcCodeID  """  
      self.LinkList:str = obj["LinkList"]
      """  List of LookupLink records for the cmbLinkUID combo  """  
      self.SrcFieldDesc:str = obj["SrcFieldDesc"]
      """  Source Field Link Description (Summ of Lookup Link Field1 to Field30 and Value1 to Value30 information)  """  
      self.SrcFieldName:str = obj["SrcFieldName"]
      self.DspSrcCodeID:str = obj["DspSrcCodeID"]
      self.SrcDataType:str = obj["SrcDataType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcParamsBAQRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique.  """  
      self.BAQParamValNbr:int = obj["BAQParamValNbr"]
      """  Intended for internal use only to keep the records unique.  """  
      self.BAQExportID:str = obj["BAQExportID"]
      """  BAQ ID, the unique identifier for this Query table within the company  """  
      self.ParameterName:str = obj["ParameterName"]
      self.BAQParamCode:str = obj["BAQParamCode"]
      """  Specific baq parameter value.  """  
      self.ParamOpt:int = obj["ParamOpt"]
      """   Identifes the option for the BAQ parameter.
1 = Use Target Account Segment.  
2 = Use Source Account Segment
3 = Use Allocation Run Start Date
4 = Use allocation Run End Date  """  
      self.ParamSegmentNbr:int = obj["ParamSegmentNbr"]
      """  Identifies the segment number to use to determine the segment code that will be used to look up the result value in the lookup table.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.EntryType:int = obj["EntryType"]
      """  Identifies if the parameter is an actual value or an option.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ParamSegmentName:str = obj["ParamSegmentName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcParamsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.ParamName:str = obj["ParamName"]
      """  The name assigned to a parameter.  This name must be unique.  """  
      self.ParamType:int = obj["ParamType"]
      """  Identifies the type of parameter used in the allocation logic.  1 = Account Balances, 2 = Summarized balances,  3 = BAQ and 4 = Non Financial Data.  """  
      self.ParamDesc:str = obj["ParamDesc"]
      """  Text that describes the parameter.  """  
      self.AcctParamValSrc:int = obj["AcctParamValSrc"]
      """  Indicates the source data for the value of a parameter value when the parameter is of type Account Balance.  """  
      self.SumParamValSrc:int = obj["SumParamValSrc"]
      """  Indicates the source data for the value of a parameter value when the parameter is of type Summarized.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.AcctBalAcct:str = obj["AcctBalAcct"]
      """  Account balance account.  Only valid when the formula type = 1.  """  
      self.AcctBalSegVal1:str = obj["AcctBalSegVal1"]
      """  Account Segment Value 1  """  
      self.AcctBalSegVal2:str = obj["AcctBalSegVal2"]
      """  Account Segment Value 2  """  
      self.AcctBalSegVal3:str = obj["AcctBalSegVal3"]
      """  Account Segment Value 3  """  
      self.AcctBalSegVal4:str = obj["AcctBalSegVal4"]
      """  Account Segment Value 4  """  
      self.AcctBalSegVal5:str = obj["AcctBalSegVal5"]
      """  Account Segment Value 5  """  
      self.AcctBalSegVal6:str = obj["AcctBalSegVal6"]
      """  Account Segment Value 6  """  
      self.AcctBalSegVal7:str = obj["AcctBalSegVal7"]
      """  Account Segment Value 7  """  
      self.AcctBalSegVal8:str = obj["AcctBalSegVal8"]
      """  Account Segment Value 8  """  
      self.AcctBalSegVal9:str = obj["AcctBalSegVal9"]
      """  Account Segment Value 9  """  
      self.AcctBalSegVal10:str = obj["AcctBalSegVal10"]
      """  Account Segment Value 10  """  
      self.AcctBalSegVal11:str = obj["AcctBalSegVal11"]
      """  Account Segment Value 11  """  
      self.AcctBalSegVal12:str = obj["AcctBalSegVal12"]
      """  Account Segment Value 12  """  
      self.AcctBalSegVal13:str = obj["AcctBalSegVal13"]
      """  Account Segment Value 13  """  
      self.AcctBalSegVal14:str = obj["AcctBalSegVal14"]
      """  Account Segment Value 14  """  
      self.AcctBalSegVal15:str = obj["AcctBalSegVal15"]
      """  Account Segment Value 15  """  
      self.AcctBalSegVal16:str = obj["AcctBalSegVal16"]
      """  Account Segment Value 16  """  
      self.AcctBalSegVal17:str = obj["AcctBalSegVal17"]
      """  Account Segment Value 17  """  
      self.AcctBalSegVal18:str = obj["AcctBalSegVal18"]
      """  Account Segment Value 18  """  
      self.AcctBalSegVal19:str = obj["AcctBalSegVal19"]
      """  Account Segment Value 19  """  
      self.AcctBalSegVal20:str = obj["AcctBalSegVal20"]
      """  Account Segment Value 20  """  
      self.UseTgtAcct:bool = obj["UseTgtAcct"]
      """  Yes indictes the target account's balance is taken and the AcctBalAcct is set equal to the AlcTarget.TgtGLAcct.  This only only valid when the formula type = Account Balances.  """  
      self.BAQExportID:str = obj["BAQExportID"]
      """  BAQ ID, the unique identifier for this Query table within the company  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NFSrcMapUID:int = obj["NFSrcMapUID"]
      """  NFSrcMapUID  """  
      self.NFTgtSeqNbr:int = obj["NFTgtSeqNbr"]
      """  NFTgtSeqNbr  """  
      self.YTDBalance:bool = obj["YTDBalance"]
      """  YTDBalance  """  
      self.BAQEnableParams:bool = obj["BAQEnableParams"]
      """  Indicates whether or not the BAQ has parameters defined.  If not, then the user cannot define BAQ parameters in allocation code maintenance.  """  
      self.BAQExportIDDescription:str = obj["BAQExportIDDescription"]
      """  Dynamic query description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.LookupTableIDDisplayName:str = obj["LookupTableIDDisplayName"]
      self.TargetFieldNameFieldName:str = obj["TargetFieldNameFieldName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcRangeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """   Intended for internal use only to keep the records unique.  The ParamNbr value is 0  when tied to a source account (AlcHed).
When tied to a parameter criteria (AlcParams) it inherits its value from AlcParams table.  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.MinValue:str = obj["MinValue"]
      """  Minimum vale for range selection.  """  
      self.MaxValue:str = obj["MaxValue"]
      """  Maximum value for range selection.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COASegmentSegmentName:str = obj["COASegmentSegmentName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcTargetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.AllocOption:int = obj["AllocOption"]
      """  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  """  
      self.RatioFormula:str = obj["RatioFormula"]
      """  Formula entered by the user used to calculate the allocation amount.  Only valid if the allocation option = 2.  """  
      self.RatioValue:int = obj["RatioValue"]
      """  Postive, fractional value indicating how much of an allocation is applied to this target.  """  
      self.AllocUnits:int = obj["AllocUnits"]
      """   The relative  number of units used to allocate to this account.
Allocation units / Total Allocation units is used to distribute the amount. Total Allocation units are calculated for a given AllocID and not stored.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.TgtGLAcct:str = obj["TgtGLAcct"]
      """  The GL Account an amount is allocated to.  This may be an actual GL Account or a masked account where each mask character is swapped with the corresponding character from the source GL Account.  """  
      self.TgtSegVal1:str = obj["TgtSegVal1"]
      """  Target Segment Value 1  """  
      self.TgtSegVal2:str = obj["TgtSegVal2"]
      """  Target Segment Value 2  """  
      self.TgtSegVal3:str = obj["TgtSegVal3"]
      """  Target Segment Value 3  """  
      self.TgtSegVal4:str = obj["TgtSegVal4"]
      """  Target Segment Value 4  """  
      self.TgtSegVal5:str = obj["TgtSegVal5"]
      """  Target Segment Value 5  """  
      self.TgtSegVal6:str = obj["TgtSegVal6"]
      """  Target Segment Value 6  """  
      self.TgtSegVal7:str = obj["TgtSegVal7"]
      """  Target Segment Value 7  """  
      self.TgtSegVal8:str = obj["TgtSegVal8"]
      """  Target Segment Value 8  """  
      self.TgtSegVal9:str = obj["TgtSegVal9"]
      """  Target Segment Value 9  """  
      self.TgtSegVal10:str = obj["TgtSegVal10"]
      """  Target Segment Value 10  """  
      self.TgtSegVal11:str = obj["TgtSegVal11"]
      """  Target Segment Value 11  """  
      self.TgtSegVal12:str = obj["TgtSegVal12"]
      """  Target Segment Value 12  """  
      self.TgtSegVal13:str = obj["TgtSegVal13"]
      """  Target Segment Value 13  """  
      self.TgtSegVal14:str = obj["TgtSegVal14"]
      """  Target Segment Value 14  """  
      self.TgtSegVal15:str = obj["TgtSegVal15"]
      """  Target Segment Value 15  """  
      self.TgtSegVal16:str = obj["TgtSegVal16"]
      """  Target Segment Value 16  """  
      self.TgtSegVal17:str = obj["TgtSegVal17"]
      """  Target Segment Value 17  """  
      self.TgtSegVal18:str = obj["TgtSegVal18"]
      """  Target Segment Value 18  """  
      self.TgtSegVal19:str = obj["TgtSegVal19"]
      """  Target Segment Value 19  """  
      self.TgtSegVal20:str = obj["TgtSegVal20"]
      """  Target Segment Value 20  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  MultiCompany  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  ExtCompanyID  """  
      self.ExtGLAccount:str = obj["ExtGLAccount"]
      """  ExtGLAccount  """  
      self.ExtCOACode:str = obj["ExtCOACode"]
      """  ExtCOACode  """  
      self.ExtSegValue1:str = obj["ExtSegValue1"]
      """  ExtSegValue1  """  
      self.ExtSegValue2:str = obj["ExtSegValue2"]
      """  ExtSegValue2  """  
      self.ExtSegValue3:str = obj["ExtSegValue3"]
      """  ExtSegValue3  """  
      self.ExtSegValue4:str = obj["ExtSegValue4"]
      """  ExtSegValue4  """  
      self.ExtSegValue5:str = obj["ExtSegValue5"]
      """  ExtSegValue5  """  
      self.ExtSegValue6:str = obj["ExtSegValue6"]
      """  ExtSegValue6  """  
      self.ExtSegValue7:str = obj["ExtSegValue7"]
      """  ExtSegValue7  """  
      self.ExtSegValue8:str = obj["ExtSegValue8"]
      """  ExtSegValue8  """  
      self.ExtSegValue9:str = obj["ExtSegValue9"]
      """  ExtSegValue9  """  
      self.ExtSegValue10:str = obj["ExtSegValue10"]
      """  ExtSegValue10  """  
      self.ExtSegValue11:str = obj["ExtSegValue11"]
      """  ExtSegValue11  """  
      self.ExtSegValue12:str = obj["ExtSegValue12"]
      """  ExtSegValue12  """  
      self.ExtSegValue13:str = obj["ExtSegValue13"]
      """  ExtSegValue13  """  
      self.ExtSegValue14:str = obj["ExtSegValue14"]
      """  ExtSegValue14  """  
      self.ExtSegValue15:str = obj["ExtSegValue15"]
      """  ExtSegValue15  """  
      self.ExtSegValue16:str = obj["ExtSegValue16"]
      """  ExtSegValue16  """  
      self.ExtSegValue17:str = obj["ExtSegValue17"]
      """  ExtSegValue17  """  
      self.ExtSegValue18:str = obj["ExtSegValue18"]
      """  ExtSegValue18  """  
      self.ExtSegValue19:str = obj["ExtSegValue19"]
      """  ExtSegValue19  """  
      self.ExtSegValue20:str = obj["ExtSegValue20"]
      """  ExtSegValue20  """  
      self.OverrideGLAcct:bool = obj["OverrideGLAcct"]
      """  OverrideGLAcct  """  
      self.Argument1:str = obj["Argument1"]
      """  Used to bind UI control.  """  
      self.Argument2:str = obj["Argument2"]
      """  Used to bind UI control.  """  
      self.Operator:str = obj["Operator"]
      """  Used to bind UI control.  """  
      self.TgtGLDesc:str = obj["TgtGLDesc"]
      """  Target GL Account Description  """  
      self.ExtAccountDesc:str = obj["ExtAccountDesc"]
      """  Ext GL Account Description  """  
      self.EnableMultiCompany:bool = obj["EnableMultiCompany"]
      """  Flag to indicate if the MultiCompany check box needs to be enabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeAllocOption_input:
   """ Required : 
   ipProposedAllocOption
   ds
   """  
   def __init__(self, obj):
      self.ipProposedAllocOption:int = obj["ipProposedAllocOption"]
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class ChangeAllocOption_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      self.opWarningMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeAllocationType_input:
   """ Required : 
   ipProposedAllocType
   ds
   """  
   def __init__(self, obj):
      self.ipProposedAllocType:int = obj["ipProposedAllocType"]
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class ChangeAllocationType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeBAQEntryType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class ChangeBAQEntryType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeExtCompanyID_input:
   """ Required : 
   ProposedExtCompID
   allocID
   ds
   """  
   def __init__(self, obj):
      self.ProposedExtCompID:str = obj["ProposedExtCompID"]
      self.allocID:str = obj["allocID"]
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class ChangeExtCompanyID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLookupEntryType_input:
   """ Required : 
   ipAllocID
   ipParamNbr
   ipSrcSeqNbr
   ds
   """  
   def __init__(self, obj):
      self.ipAllocID:str = obj["ipAllocID"]
      self.ipParamNbr:int = obj["ipParamNbr"]
      self.ipSrcSeqNbr:int = obj["ipSrcSeqNbr"]
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class ChangeLookupEntryType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckArgument_input:
   """ Required : 
   ipAllocID
   ipArgument1
   ipArgument2
   """  
   def __init__(self, obj):
      self.ipAllocID:str = obj["ipAllocID"]
      """  ipAllocID of selected record  """  
      self.ipArgument1:str = obj["ipArgument1"]
      """  Argument1 to validate  """  
      self.ipArgument2:str = obj["ipArgument2"]
      """  Argument2 to validate  """  
      pass

class CheckArgument_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opArgument1:str = obj["parameters"]
      self.opArgument2:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckBAQExportID_input:
   """ Required : 
   ipBAQExportID
   ds
   """  
   def __init__(self, obj):
      self.ipBAQExportID:str = obj["ipBAQExportID"]
      """  BAQ proposed value  """  
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class CheckBAQExportID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBAQParameterValue_input:
   """ Required : 
   ipBAQExportID
   ipFieldName
   ipValue
   """  
   def __init__(self, obj):
      self.ipBAQExportID:str = obj["ipBAQExportID"]
      self.ipFieldName:str = obj["ipFieldName"]
      self.ipValue:str = obj["ipValue"]
      pass

class CheckBAQParameterValue_output:
   def __init__(self, obj):
      pass

class CheckBAQParameter_input:
   """ Required : 
   ipBAQExportID
   ipFieldName
   """  
   def __init__(self, obj):
      self.ipBAQExportID:str = obj["ipBAQExportID"]
      self.ipFieldName:str = obj["ipFieldName"]
      pass

class CheckBAQParameter_output:
   def __init__(self, obj):
      pass

class CheckBook_input:
   """ Required : 
   ipBookID
   ds
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  GL Book ID  """  
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class CheckBook_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckCanAddNewTarget_input:
   """ Required : 
   ipAllocID
   """  
   def __init__(self, obj):
      self.ipAllocID:str = obj["ipAllocID"]
      pass

class CheckCanAddNewTarget_output:
   def __init__(self, obj):
      pass

class CheckCategory_input:
   """ Required : 
   ipCategoryID
   ds
   """  
   def __init__(self, obj):
      self.ipCategoryID:str = obj["ipCategoryID"]
      """  Category ID to validate  """  
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class CheckCategory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckForDuplicateAccount_input:
   """ Required : 
   ipGLAccount
   ipParamNbr
   ipAllocID
   """  
   def __init__(self, obj):
      self.ipGLAccount:str = obj["ipGLAccount"]
      self.ipParamNbr:int = obj["ipParamNbr"]
      self.ipAllocID:str = obj["ipAllocID"]
      pass

class CheckForDuplicateAccount_output:
   def __init__(self, obj):
      pass

class CheckJournalCode_input:
   """ Required : 
   ipJournalCode
   ds
   """  
   def __init__(self, obj):
      self.ipJournalCode:str = obj["ipJournalCode"]
      """  Journal Code to validate  """  
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class CheckJournalCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckMinMax_input:
   """ Required : 
   ipMinRange
   ipMaxRange
   ipCOACode
   ipSegmentNbr
   """  
   def __init__(self, obj):
      self.ipMinRange:str = obj["ipMinRange"]
      """  Minimum range to validate  """  
      self.ipMaxRange:str = obj["ipMaxRange"]
      """  Maximum range to validate  """  
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA Code  """  
      self.ipSegmentNbr:int = obj["ipSegmentNbr"]
      """  Segment Number to validate  """  
      pass

class CheckMinMax_output:
   def __init__(self, obj):
      pass

class CheckParamName_input:
   """ Required : 
   ipParamName
   """  
   def __init__(self, obj):
      self.ipParamName:str = obj["ipParamName"]
      """  Proposed parameter name  """  
      pass

class CheckParamName_output:
   def __init__(self, obj):
      pass

class CheckParamOptionBAQ_input:
   """ Required : 
   ipParamOpt
   ds
   """  
   def __init__(self, obj):
      self.ipParamOpt:int = obj["ipParamOpt"]
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class CheckParamOptionBAQ_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckParamOption_input:
   """ Required : 
   ipAllocID
   ipParamNbr
   ipSrcSeqNbr
   ipParamOpt
   ds
   """  
   def __init__(self, obj):
      self.ipAllocID:str = obj["ipAllocID"]
      self.ipParamNbr:int = obj["ipParamNbr"]
      self.ipSrcSeqNbr:int = obj["ipSrcSeqNbr"]
      self.ipParamOpt:int = obj["ipParamOpt"]
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class CheckParamOption_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckParamSegment_input:
   """ Required : 
   ipParamSegmentNbr
   ipParamType
   ds
   """  
   def __init__(self, obj):
      self.ipParamSegmentNbr:int = obj["ipParamSegmentNbr"]
      self.ipParamType:str = obj["ipParamType"]
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class CheckParamSegment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPercentageToAllocate_input:
   """ Required : 
   ipAllocID
   ipProposedPercentage
   """  
   def __init__(self, obj):
      self.ipAllocID:str = obj["ipAllocID"]
      self.ipProposedPercentage:int = obj["ipProposedPercentage"]
      pass

class CheckPercentageToAllocate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWarnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPriorTgtStamp_input:
   """ Required : 
   ipPriorTgtStamp
   ds
   """  
   def __init__(self, obj):
      self.ipPriorTgtStamp:str = obj["ipPriorTgtStamp"]
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class CheckPriorTgtStamp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      self.opWarningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckSegmentNbr_input:
   """ Required : 
   ipAllocID
   ipParamNbr
   ipSegmentNbr
   """  
   def __init__(self, obj):
      self.ipAllocID:str = obj["ipAllocID"]
      """  Allocation ID  """  
      self.ipParamNbr:int = obj["ipParamNbr"]
      """  Parameter Number  """  
      self.ipSegmentNbr:int = obj["ipSegmentNbr"]
      """  Proposed Segment Number  """  
      pass

class CheckSegmentNbr_output:
   def __init__(self, obj):
      pass

class CheckSyntax_input:
   """ Required : 
   ipAllocID
   ipFormula
   """  
   def __init__(self, obj):
      self.ipAllocID:str = obj["ipAllocID"]
      """  AllocID of selected record  """  
      self.ipFormula:str = obj["ipFormula"]
      """  Formula to validate  """  
      pass

class CheckSyntax_output:
   def __init__(self, obj):
      pass

class CheckTgtStamp_input:
   """ Required : 
   ipTgtStamp
   ds
   """  
   def __init__(self, obj):
      self.ipTgtStamp:str = obj["ipTgtStamp"]
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class CheckTgtStamp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      self.opWarningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckTier_input:
   """ Required : 
   ipTier
   ds
   """  
   def __init__(self, obj):
      self.ipTier:int = obj["ipTier"]
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class CheckTier_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckTotalPercent_input:
   """ Required : 
   ipProposedPercent
   ds
   """  
   def __init__(self, obj):
      self.ipProposedPercent:int = obj["ipProposedPercent"]
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class CheckTotalPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      self.opTotalPercent:int = obj["parameters"]
      pass

      """  output parameters  """  

class CreateAlcNFSrcRecords_input:
   """ Required : 
   ipAllocID
   ipParamNbr
   ds
   """  
   def __init__(self, obj):
      self.ipAllocID:str = obj["ipAllocID"]
      """  GL Allocations Id  """  
      self.ipParamNbr:int = obj["ipParamNbr"]
      """  Parameter number  """  
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class CreateAlcNFSrcRecords_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   allocID
   """  
   def __init__(self, obj):
      self.allocID:str = obj["allocID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AlcAcctCatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """   Intended for internal use only to keep the records unique.  The ParamNbr value is 0  when tied to a source account (AlcHed).
When tied to a parameter criteria (AlcParams) it inherits its value from AlcParams table.  """  
      self.CategoryID:str = obj["CategoryID"]
      """  Unique identifier of this category of accounts.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AlcAcctCatCOAActCatType:str = obj["AlcAcctCatCOAActCatType"]
      self.AlcAcctCatCOAActCatDescription:str = obj["AlcAcctCatCOAActCatDescription"]
      self.COADescription:str = obj["COADescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """   Intended for internal use only to keep the records unique.  The ParamNbr value is 0  when tied to a source account (AlcHed).
When tied to a parameter criteria (AlcParams) it inherits its value from AlcParams table.  """  
      self.AllocGLAcct:str = obj["AllocGLAcct"]
      """  GL Account or GL Account mask  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.AllocSegValue1:str = obj["AllocSegValue1"]
      """  Allocation Segment Value 1  """  
      self.AllocSegValue2:str = obj["AllocSegValue2"]
      """  Allocation Segment Value 2  """  
      self.AllocSegValue3:str = obj["AllocSegValue3"]
      """  Allocation Segment Value 3  """  
      self.AllocSegValue4:str = obj["AllocSegValue4"]
      """  Allocation Segment Value 4  """  
      self.AllocSegValue5:str = obj["AllocSegValue5"]
      """  Allocation Segment Value 5  """  
      self.AllocSegValue6:str = obj["AllocSegValue6"]
      """  Allocation Segment Value 6  """  
      self.AllocSegValue7:str = obj["AllocSegValue7"]
      """  Allocation Segment Value 7  """  
      self.AllocSegValue8:str = obj["AllocSegValue8"]
      """  Allocation Segment Value 8  """  
      self.AllocSegValue9:str = obj["AllocSegValue9"]
      """  Allocation Segment Value 9  """  
      self.AllocSegValue10:str = obj["AllocSegValue10"]
      """  Allocation Segment Value 10  """  
      self.AllocSegValue11:str = obj["AllocSegValue11"]
      """  Allocation Segment Value 11  """  
      self.AllocSegValue12:str = obj["AllocSegValue12"]
      """  Allocation Segment Value 12  """  
      self.AllocSegValue13:str = obj["AllocSegValue13"]
      """  Allocation Segment Value 13  """  
      self.AllocSegValue14:str = obj["AllocSegValue14"]
      """  Allocation Segment Value 14  """  
      self.AllocSegValue15:str = obj["AllocSegValue15"]
      """  Allocation Segment Value 15  """  
      self.AllocSegValue16:str = obj["AllocSegValue16"]
      """  Allocation Segment Value 16  """  
      self.AllocSegValue17:str = obj["AllocSegValue17"]
      """  Allocation Segment Value 17  """  
      self.AllocSegValue18:str = obj["AllocSegValue18"]
      """  Allocation Segment Value 18  """  
      self.AllocSegValue19:str = obj["AllocSegValue19"]
      """  Allocation Segment Value 19  """  
      self.AllocSegValue20:str = obj["AllocSegValue20"]
      """  Allocation Segment Value 20  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.Description:str = obj["Description"]
      """  Allocation code description.  """  
      self.AllocationType:int = obj["AllocationType"]
      """   Identifies whether or not the allocaiton is balance or transaction based.  1 = Transaction and is the default value.
2 = Balance based.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Tier:int = obj["Tier"]
      """  Allocation tier.  """  
      self.PriorTgtStamp:str = obj["PriorTgtStamp"]
      """  Identifies the allocation stamp to which this allocation is to be applied.  """  
      self.TgtStamp:str = obj["TgtStamp"]
      """  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  """  
      self.SrcAllocStamp:str = obj["SrcAllocStamp"]
      """  Identifies the allocation stamp that was processed by this allocation.  """  
      self.IgnoreStamp:bool = obj["IgnoreStamp"]
      """  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  """  
      self.UseAllStamps:bool = obj["UseAllStamps"]
      """  Yes indicates that all allocation stamps are valid for the allocation code.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.AllocOption:int = obj["AllocOption"]
      """  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  """  
      self.PercentToAlloc:int = obj["PercentToAlloc"]
      """  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  """  
      self.UseAllocUnits:bool = obj["UseAllocUnits"]
      """  Indicates if the allocation units are used.  """  
      self.OffsetAcct:str = obj["OffsetAcct"]
      """  The general ledger account the allocation is to be written off.  """  
      self.OffsetSegVal1:str = obj["OffsetSegVal1"]
      """  Offset Segment Value 1  """  
      self.OffsetSegVal2:str = obj["OffsetSegVal2"]
      """  Offset Segment Value 2  """  
      self.OffsetSegVal3:str = obj["OffsetSegVal3"]
      """  Offset Segment Value 3  """  
      self.OffsetSegVal4:str = obj["OffsetSegVal4"]
      """  Offset Segment Value 4  """  
      self.OffsetSegVal5:str = obj["OffsetSegVal5"]
      """  Offset Segment Value 5  """  
      self.OffsetSegVal6:str = obj["OffsetSegVal6"]
      """  Offset Segment Value 6  """  
      self.OffsetSegVal7:str = obj["OffsetSegVal7"]
      """  Offset Segment Value 7  """  
      self.OffsetSegVal8:str = obj["OffsetSegVal8"]
      """  Offset Segment Value 8  """  
      self.OffsetSegVal9:str = obj["OffsetSegVal9"]
      """  Offset Segment Value 9  """  
      self.OffsetSegVal10:str = obj["OffsetSegVal10"]
      """  Offset Segment Value 10  """  
      self.OffsetSegVal11:str = obj["OffsetSegVal11"]
      """  Offset Segment Value 11  """  
      self.OffsetSegVal12:str = obj["OffsetSegVal12"]
      """  Offset Segment Value 12  """  
      self.OffsetSegVal13:str = obj["OffsetSegVal13"]
      """  Offset Segment Value 13  """  
      self.OffsetSegVal14:str = obj["OffsetSegVal14"]
      """  Offset Segment Value 14  """  
      self.OffsetSegVal15:str = obj["OffsetSegVal15"]
      """  Offset Segment Value 15  """  
      self.OffsetSegVal16:str = obj["OffsetSegVal16"]
      """  Offset Segment Value 16  """  
      self.OffsetSegVal17:str = obj["OffsetSegVal17"]
      """  Offset Segment Value 17  """  
      self.OffsetSegVal18:str = obj["OffsetSegVal18"]
      """  Offset Segment Value 18  """  
      self.OffsetSegVal19:str = obj["OffsetSegVal19"]
      """  Offset Segment Value 19  """  
      self.OffsetSegVal20:str = obj["OffsetSegVal20"]
      """  Offset Segment Value 20  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllocIsRunning:bool = obj["AllocIsRunning"]
      """  Indicates whether or not a allocation is currently executing.  """  
      self.TotalAllocUnits:int = obj["TotalAllocUnits"]
      """  Total allocation units.  This is the sum of the allocation units defined on the targets.  """  
      self.TotalPercentage:int = obj["TotalPercentage"]
      """  his is the sum of the percentage values defined on the targets.  """  
      self.OffsetAcctDesc:str = obj["OffsetAcctDesc"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      """  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The value of this field is the concatenation of the first three controlled display order segments.  For example, if a chart has 5 controlled segments that are displayed in the following order: seg5->seg3->seg4->seg2->seg1, this field contains the concatention of seg5->seg3->seg4 up to th  """  
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      """  Text that describes the account.  """  
      self.GLBookDescription:str = obj["GLBookDescription"]
      """  Descripiton of Book  """  
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHedListTableset:
   def __init__(self, obj):
      self.AlcHedList:list[Erp_Tablesets_AlcHedListRow] = obj["AlcHedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_AlcHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.Description:str = obj["Description"]
      """  Allocation code description.  """  
      self.AllocationType:int = obj["AllocationType"]
      """   Identifies whether or not the allocaiton is balance or transaction based.  1 = Transaction and is the default value.
2 = Balance based.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Tier:int = obj["Tier"]
      """  Allocation tier.  """  
      self.PriorTgtStamp:str = obj["PriorTgtStamp"]
      """  Identifies the allocation stamp to which this allocation is to be applied.  """  
      self.TgtStamp:str = obj["TgtStamp"]
      """  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  """  
      self.SrcAllocStamp:str = obj["SrcAllocStamp"]
      """  Identifies the allocation stamp that was processed by this allocation.  """  
      self.IgnoreStamp:bool = obj["IgnoreStamp"]
      """  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  """  
      self.UseAllStamps:bool = obj["UseAllStamps"]
      """  Yes indicates that all allocation stamps are valid for the allocation code.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.AllocOption:int = obj["AllocOption"]
      """  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  """  
      self.PercentToAlloc:int = obj["PercentToAlloc"]
      """  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  """  
      self.UseAllocUnits:bool = obj["UseAllocUnits"]
      """  Indicates if the allocation units are used.  """  
      self.OffsetAcct:str = obj["OffsetAcct"]
      """  The general ledger account the allocation is to be written off.  """  
      self.OffsetSegVal1:str = obj["OffsetSegVal1"]
      """  Offset Segment Value 1  """  
      self.OffsetSegVal2:str = obj["OffsetSegVal2"]
      """  Offset Segment Value 2  """  
      self.OffsetSegVal3:str = obj["OffsetSegVal3"]
      """  Offset Segment Value 3  """  
      self.OffsetSegVal4:str = obj["OffsetSegVal4"]
      """  Offset Segment Value 4  """  
      self.OffsetSegVal5:str = obj["OffsetSegVal5"]
      """  Offset Segment Value 5  """  
      self.OffsetSegVal6:str = obj["OffsetSegVal6"]
      """  Offset Segment Value 6  """  
      self.OffsetSegVal7:str = obj["OffsetSegVal7"]
      """  Offset Segment Value 7  """  
      self.OffsetSegVal8:str = obj["OffsetSegVal8"]
      """  Offset Segment Value 8  """  
      self.OffsetSegVal9:str = obj["OffsetSegVal9"]
      """  Offset Segment Value 9  """  
      self.OffsetSegVal10:str = obj["OffsetSegVal10"]
      """  Offset Segment Value 10  """  
      self.OffsetSegVal11:str = obj["OffsetSegVal11"]
      """  Offset Segment Value 11  """  
      self.OffsetSegVal12:str = obj["OffsetSegVal12"]
      """  Offset Segment Value 12  """  
      self.OffsetSegVal13:str = obj["OffsetSegVal13"]
      """  Offset Segment Value 13  """  
      self.OffsetSegVal14:str = obj["OffsetSegVal14"]
      """  Offset Segment Value 14  """  
      self.OffsetSegVal15:str = obj["OffsetSegVal15"]
      """  Offset Segment Value 15  """  
      self.OffsetSegVal16:str = obj["OffsetSegVal16"]
      """  Offset Segment Value 16  """  
      self.OffsetSegVal17:str = obj["OffsetSegVal17"]
      """  Offset Segment Value 17  """  
      self.OffsetSegVal18:str = obj["OffsetSegVal18"]
      """  Offset Segment Value 18  """  
      self.OffsetSegVal19:str = obj["OffsetSegVal19"]
      """  Offset Segment Value 19  """  
      self.OffsetSegVal20:str = obj["OffsetSegVal20"]
      """  Offset Segment Value 20  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StatBalAsAllocUnits:bool = obj["StatBalAsAllocUnits"]
      """  Indicates if Statistical Balance of Target Account should be used as Allocation Units  """  
      self.AllocIsRunning:bool = obj["AllocIsRunning"]
      """  Indicates whether or not a allocation is currently executing.  """  
      self.TotalAllocUnits:int = obj["TotalAllocUnits"]
      """  Total allocation units.  This is the sum of the allocation units defined on the targets.  """  
      self.TotalPercentage:int = obj["TotalPercentage"]
      """  his is the sum of the percentage values defined on the targets.  """  
      self.OffsetAcctDesc:str = obj["OffsetAcctDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHedTableset:
   def __init__(self, obj):
      self.AlcHed:list[Erp_Tablesets_AlcHedRow] = obj["AlcHed"]
      self.AlcAcct:list[Erp_Tablesets_AlcAcctRow] = obj["AlcAcct"]
      self.AlcAcctCat:list[Erp_Tablesets_AlcAcctCatRow] = obj["AlcAcctCat"]
      self.AlcJrnCd:list[Erp_Tablesets_AlcJrnCdRow] = obj["AlcJrnCd"]
      self.AlcParams:list[Erp_Tablesets_AlcParamsRow] = obj["AlcParams"]
      self.AlcNFSrc:list[Erp_Tablesets_AlcNFSrcRow] = obj["AlcNFSrc"]
      self.AlcParamsBAQ:list[Erp_Tablesets_AlcParamsBAQRow] = obj["AlcParamsBAQ"]
      self.AlcRange:list[Erp_Tablesets_AlcRangeRow] = obj["AlcRange"]
      self.AlcTarget:list[Erp_Tablesets_AlcTargetRow] = obj["AlcTarget"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_AlcJrnCdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """   Intended for internal use only to keep the records unique.  The ParamNbr value is 0  when tied to a source account (AlcHed).
When tied to a parameter criteria (AlcParams) it inherits its value from AlcParams table.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      self.JrnlCodeSystemJournal:bool = obj["JrnlCodeSystemJournal"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcNFSrcRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique.  The value is inherited from the AlcParams table.  """  
      self.LookupTblMapUID_obsolete:int = obj["LookupTblMapUID_obsolete"]
      """  LookupTblMapUID_obsolete  """  
      self.TgtSeqNbr_obsolete:int = obj["TgtSeqNbr_obsolete"]
      """  TgtSeqNbr_obsolete  """  
      self.LinkUID_obsolete:int = obj["LinkUID_obsolete"]
      """  LinkUID_obsolete  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.ParamOpt:int = obj["ParamOpt"]
      """   Identifes the option for the BAQ parameter.
1 = Use Target Account Segment.  
2 = Use Source Account Segment
3 = Use Allocation Run Start Date
4 = Use allocation Run End Date  """  
      self.ParamSegmentNbr:int = obj["ParamSegmentNbr"]
      """  Identifies the segment number to use to determine the segment code that will be used to look up the result value in the lookup table.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.EntryType:int = obj["EntryType"]
      """  Identifies if the parameter is an actual value or an option.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SrcSeqNbr:int = obj["SrcSeqNbr"]
      """  SrcSeqNbr  """  
      self.SrcCodeID:str = obj["SrcCodeID"]
      """  SrcCodeID  """  
      self.LinkList:str = obj["LinkList"]
      """  List of LookupLink records for the cmbLinkUID combo  """  
      self.SrcFieldDesc:str = obj["SrcFieldDesc"]
      """  Source Field Link Description (Summ of Lookup Link Field1 to Field30 and Value1 to Value30 information)  """  
      self.SrcFieldName:str = obj["SrcFieldName"]
      self.DspSrcCodeID:str = obj["DspSrcCodeID"]
      self.SrcDataType:str = obj["SrcDataType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcParamsBAQRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique.  """  
      self.BAQParamValNbr:int = obj["BAQParamValNbr"]
      """  Intended for internal use only to keep the records unique.  """  
      self.BAQExportID:str = obj["BAQExportID"]
      """  BAQ ID, the unique identifier for this Query table within the company  """  
      self.ParameterName:str = obj["ParameterName"]
      self.BAQParamCode:str = obj["BAQParamCode"]
      """  Specific baq parameter value.  """  
      self.ParamOpt:int = obj["ParamOpt"]
      """   Identifes the option for the BAQ parameter.
1 = Use Target Account Segment.  
2 = Use Source Account Segment
3 = Use Allocation Run Start Date
4 = Use allocation Run End Date  """  
      self.ParamSegmentNbr:int = obj["ParamSegmentNbr"]
      """  Identifies the segment number to use to determine the segment code that will be used to look up the result value in the lookup table.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.EntryType:int = obj["EntryType"]
      """  Identifies if the parameter is an actual value or an option.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ParamSegmentName:str = obj["ParamSegmentName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcParamsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.ParamName:str = obj["ParamName"]
      """  The name assigned to a parameter.  This name must be unique.  """  
      self.ParamType:int = obj["ParamType"]
      """  Identifies the type of parameter used in the allocation logic.  1 = Account Balances, 2 = Summarized balances,  3 = BAQ and 4 = Non Financial Data.  """  
      self.ParamDesc:str = obj["ParamDesc"]
      """  Text that describes the parameter.  """  
      self.AcctParamValSrc:int = obj["AcctParamValSrc"]
      """  Indicates the source data for the value of a parameter value when the parameter is of type Account Balance.  """  
      self.SumParamValSrc:int = obj["SumParamValSrc"]
      """  Indicates the source data for the value of a parameter value when the parameter is of type Summarized.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.AcctBalAcct:str = obj["AcctBalAcct"]
      """  Account balance account.  Only valid when the formula type = 1.  """  
      self.AcctBalSegVal1:str = obj["AcctBalSegVal1"]
      """  Account Segment Value 1  """  
      self.AcctBalSegVal2:str = obj["AcctBalSegVal2"]
      """  Account Segment Value 2  """  
      self.AcctBalSegVal3:str = obj["AcctBalSegVal3"]
      """  Account Segment Value 3  """  
      self.AcctBalSegVal4:str = obj["AcctBalSegVal4"]
      """  Account Segment Value 4  """  
      self.AcctBalSegVal5:str = obj["AcctBalSegVal5"]
      """  Account Segment Value 5  """  
      self.AcctBalSegVal6:str = obj["AcctBalSegVal6"]
      """  Account Segment Value 6  """  
      self.AcctBalSegVal7:str = obj["AcctBalSegVal7"]
      """  Account Segment Value 7  """  
      self.AcctBalSegVal8:str = obj["AcctBalSegVal8"]
      """  Account Segment Value 8  """  
      self.AcctBalSegVal9:str = obj["AcctBalSegVal9"]
      """  Account Segment Value 9  """  
      self.AcctBalSegVal10:str = obj["AcctBalSegVal10"]
      """  Account Segment Value 10  """  
      self.AcctBalSegVal11:str = obj["AcctBalSegVal11"]
      """  Account Segment Value 11  """  
      self.AcctBalSegVal12:str = obj["AcctBalSegVal12"]
      """  Account Segment Value 12  """  
      self.AcctBalSegVal13:str = obj["AcctBalSegVal13"]
      """  Account Segment Value 13  """  
      self.AcctBalSegVal14:str = obj["AcctBalSegVal14"]
      """  Account Segment Value 14  """  
      self.AcctBalSegVal15:str = obj["AcctBalSegVal15"]
      """  Account Segment Value 15  """  
      self.AcctBalSegVal16:str = obj["AcctBalSegVal16"]
      """  Account Segment Value 16  """  
      self.AcctBalSegVal17:str = obj["AcctBalSegVal17"]
      """  Account Segment Value 17  """  
      self.AcctBalSegVal18:str = obj["AcctBalSegVal18"]
      """  Account Segment Value 18  """  
      self.AcctBalSegVal19:str = obj["AcctBalSegVal19"]
      """  Account Segment Value 19  """  
      self.AcctBalSegVal20:str = obj["AcctBalSegVal20"]
      """  Account Segment Value 20  """  
      self.UseTgtAcct:bool = obj["UseTgtAcct"]
      """  Yes indictes the target account's balance is taken and the AcctBalAcct is set equal to the AlcTarget.TgtGLAcct.  This only only valid when the formula type = Account Balances.  """  
      self.BAQExportID:str = obj["BAQExportID"]
      """  BAQ ID, the unique identifier for this Query table within the company  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NFSrcMapUID:int = obj["NFSrcMapUID"]
      """  NFSrcMapUID  """  
      self.NFTgtSeqNbr:int = obj["NFTgtSeqNbr"]
      """  NFTgtSeqNbr  """  
      self.YTDBalance:bool = obj["YTDBalance"]
      """  YTDBalance  """  
      self.BAQEnableParams:bool = obj["BAQEnableParams"]
      """  Indicates whether or not the BAQ has parameters defined.  If not, then the user cannot define BAQ parameters in allocation code maintenance.  """  
      self.BAQExportIDDescription:str = obj["BAQExportIDDescription"]
      """  Dynamic query description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.LookupTableIDDisplayName:str = obj["LookupTableIDDisplayName"]
      self.TargetFieldNameFieldName:str = obj["TargetFieldNameFieldName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcRangeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """   Intended for internal use only to keep the records unique.  The ParamNbr value is 0  when tied to a source account (AlcHed).
When tied to a parameter criteria (AlcParams) it inherits its value from AlcParams table.  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.MinValue:str = obj["MinValue"]
      """  Minimum vale for range selection.  """  
      self.MaxValue:str = obj["MaxValue"]
      """  Maximum value for range selection.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COASegmentSegmentName:str = obj["COASegmentSegmentName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcTargetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.AllocOption:int = obj["AllocOption"]
      """  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  """  
      self.RatioFormula:str = obj["RatioFormula"]
      """  Formula entered by the user used to calculate the allocation amount.  Only valid if the allocation option = 2.  """  
      self.RatioValue:int = obj["RatioValue"]
      """  Postive, fractional value indicating how much of an allocation is applied to this target.  """  
      self.AllocUnits:int = obj["AllocUnits"]
      """   The relative  number of units used to allocate to this account.
Allocation units / Total Allocation units is used to distribute the amount. Total Allocation units are calculated for a given AllocID and not stored.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.TgtGLAcct:str = obj["TgtGLAcct"]
      """  The GL Account an amount is allocated to.  This may be an actual GL Account or a masked account where each mask character is swapped with the corresponding character from the source GL Account.  """  
      self.TgtSegVal1:str = obj["TgtSegVal1"]
      """  Target Segment Value 1  """  
      self.TgtSegVal2:str = obj["TgtSegVal2"]
      """  Target Segment Value 2  """  
      self.TgtSegVal3:str = obj["TgtSegVal3"]
      """  Target Segment Value 3  """  
      self.TgtSegVal4:str = obj["TgtSegVal4"]
      """  Target Segment Value 4  """  
      self.TgtSegVal5:str = obj["TgtSegVal5"]
      """  Target Segment Value 5  """  
      self.TgtSegVal6:str = obj["TgtSegVal6"]
      """  Target Segment Value 6  """  
      self.TgtSegVal7:str = obj["TgtSegVal7"]
      """  Target Segment Value 7  """  
      self.TgtSegVal8:str = obj["TgtSegVal8"]
      """  Target Segment Value 8  """  
      self.TgtSegVal9:str = obj["TgtSegVal9"]
      """  Target Segment Value 9  """  
      self.TgtSegVal10:str = obj["TgtSegVal10"]
      """  Target Segment Value 10  """  
      self.TgtSegVal11:str = obj["TgtSegVal11"]
      """  Target Segment Value 11  """  
      self.TgtSegVal12:str = obj["TgtSegVal12"]
      """  Target Segment Value 12  """  
      self.TgtSegVal13:str = obj["TgtSegVal13"]
      """  Target Segment Value 13  """  
      self.TgtSegVal14:str = obj["TgtSegVal14"]
      """  Target Segment Value 14  """  
      self.TgtSegVal15:str = obj["TgtSegVal15"]
      """  Target Segment Value 15  """  
      self.TgtSegVal16:str = obj["TgtSegVal16"]
      """  Target Segment Value 16  """  
      self.TgtSegVal17:str = obj["TgtSegVal17"]
      """  Target Segment Value 17  """  
      self.TgtSegVal18:str = obj["TgtSegVal18"]
      """  Target Segment Value 18  """  
      self.TgtSegVal19:str = obj["TgtSegVal19"]
      """  Target Segment Value 19  """  
      self.TgtSegVal20:str = obj["TgtSegVal20"]
      """  Target Segment Value 20  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  MultiCompany  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  ExtCompanyID  """  
      self.ExtGLAccount:str = obj["ExtGLAccount"]
      """  ExtGLAccount  """  
      self.ExtCOACode:str = obj["ExtCOACode"]
      """  ExtCOACode  """  
      self.ExtSegValue1:str = obj["ExtSegValue1"]
      """  ExtSegValue1  """  
      self.ExtSegValue2:str = obj["ExtSegValue2"]
      """  ExtSegValue2  """  
      self.ExtSegValue3:str = obj["ExtSegValue3"]
      """  ExtSegValue3  """  
      self.ExtSegValue4:str = obj["ExtSegValue4"]
      """  ExtSegValue4  """  
      self.ExtSegValue5:str = obj["ExtSegValue5"]
      """  ExtSegValue5  """  
      self.ExtSegValue6:str = obj["ExtSegValue6"]
      """  ExtSegValue6  """  
      self.ExtSegValue7:str = obj["ExtSegValue7"]
      """  ExtSegValue7  """  
      self.ExtSegValue8:str = obj["ExtSegValue8"]
      """  ExtSegValue8  """  
      self.ExtSegValue9:str = obj["ExtSegValue9"]
      """  ExtSegValue9  """  
      self.ExtSegValue10:str = obj["ExtSegValue10"]
      """  ExtSegValue10  """  
      self.ExtSegValue11:str = obj["ExtSegValue11"]
      """  ExtSegValue11  """  
      self.ExtSegValue12:str = obj["ExtSegValue12"]
      """  ExtSegValue12  """  
      self.ExtSegValue13:str = obj["ExtSegValue13"]
      """  ExtSegValue13  """  
      self.ExtSegValue14:str = obj["ExtSegValue14"]
      """  ExtSegValue14  """  
      self.ExtSegValue15:str = obj["ExtSegValue15"]
      """  ExtSegValue15  """  
      self.ExtSegValue16:str = obj["ExtSegValue16"]
      """  ExtSegValue16  """  
      self.ExtSegValue17:str = obj["ExtSegValue17"]
      """  ExtSegValue17  """  
      self.ExtSegValue18:str = obj["ExtSegValue18"]
      """  ExtSegValue18  """  
      self.ExtSegValue19:str = obj["ExtSegValue19"]
      """  ExtSegValue19  """  
      self.ExtSegValue20:str = obj["ExtSegValue20"]
      """  ExtSegValue20  """  
      self.OverrideGLAcct:bool = obj["OverrideGLAcct"]
      """  OverrideGLAcct  """  
      self.Argument1:str = obj["Argument1"]
      """  Used to bind UI control.  """  
      self.Argument2:str = obj["Argument2"]
      """  Used to bind UI control.  """  
      self.Operator:str = obj["Operator"]
      """  Used to bind UI control.  """  
      self.TgtGLDesc:str = obj["TgtGLDesc"]
      """  Target GL Account Description  """  
      self.ExtAccountDesc:str = obj["ExtAccountDesc"]
      """  Ext GL Account Description  """  
      self.EnableMultiCompany:bool = obj["EnableMultiCompany"]
      """  Flag to indicate if the MultiCompany check box needs to be enabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtAlcHedTableset:
   def __init__(self, obj):
      self.AlcHed:list[Erp_Tablesets_AlcHedRow] = obj["AlcHed"]
      self.AlcAcct:list[Erp_Tablesets_AlcAcctRow] = obj["AlcAcct"]
      self.AlcAcctCat:list[Erp_Tablesets_AlcAcctCatRow] = obj["AlcAcctCat"]
      self.AlcJrnCd:list[Erp_Tablesets_AlcJrnCdRow] = obj["AlcJrnCd"]
      self.AlcParams:list[Erp_Tablesets_AlcParamsRow] = obj["AlcParams"]
      self.AlcNFSrc:list[Erp_Tablesets_AlcNFSrcRow] = obj["AlcNFSrc"]
      self.AlcParamsBAQ:list[Erp_Tablesets_AlcParamsBAQRow] = obj["AlcParamsBAQ"]
      self.AlcRange:list[Erp_Tablesets_AlcRangeRow] = obj["AlcRange"]
      self.AlcTarget:list[Erp_Tablesets_AlcTargetRow] = obj["AlcTarget"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   allocID
   """  
   def __init__(self, obj):
      self.allocID:str = obj["allocID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AlcHedTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AlcHedTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AlcHedTableset] = obj["returnObj"]
      pass

class GetLinkList_input:
   """ Required : 
   ipMapUID
   ipSrcSeqNbr
   ipWhereClause
   """  
   def __init__(self, obj):
      self.ipMapUID:int = obj["ipMapUID"]
      """  Map Unique ID  """  
      self.ipSrcSeqNbr:int = obj["ipSrcSeqNbr"]
      """  Src Sequence Number  """  
      self.ipWhereClause:str = obj["ipWhereClause"]
      """  Where Clause  """  
      pass

class GetLinkList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opLinkList:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_AlcHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetLookupSrcCodeID_input:
   """ Required : 
   ipDspSrcCodeID
   ipSrcDataType
   """  
   def __init__(self, obj):
      self.ipDspSrcCodeID:str = obj["ipDspSrcCodeID"]
      """  Display Source Field Code  """  
      self.ipSrcDataType:str = obj["ipSrcDataType"]
      """  Source Field Code Data Type  """  
      pass

class GetLookupSrcCodeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opSrcCodeID:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewAlcAcctCat_input:
   """ Required : 
   ds
   allocID
   paramNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      self.allocID:str = obj["allocID"]
      self.paramNbr:int = obj["paramNbr"]
      pass

class GetNewAlcAcctCat_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcAcct_input:
   """ Required : 
   ds
   allocID
   paramNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      self.allocID:str = obj["allocID"]
      self.paramNbr:int = obj["paramNbr"]
      pass

class GetNewAlcAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcHed_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class GetNewAlcHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcJrnCd_input:
   """ Required : 
   ds
   allocID
   paramNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      self.allocID:str = obj["allocID"]
      self.paramNbr:int = obj["paramNbr"]
      pass

class GetNewAlcJrnCd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcNFSrc1_input:
   """ Required : 
   ipAllocID
   ipParamNbr
   ds
   """  
   def __init__(self, obj):
      self.ipAllocID:str = obj["ipAllocID"]
      """  Allocation ID  """  
      self.ipParamNbr:int = obj["ipParamNbr"]
      """  Parameter Number  """  
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class GetNewAlcNFSrc1_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcNFSrc_input:
   """ Required : 
   ds
   allocID
   paramNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      self.allocID:str = obj["allocID"]
      self.paramNbr:int = obj["paramNbr"]
      pass

class GetNewAlcNFSrc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcParamsBAQ_input:
   """ Required : 
   ds
   allocID
   paramNbr
   baQExportID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      self.allocID:str = obj["allocID"]
      self.paramNbr:int = obj["paramNbr"]
      self.baQExportID:str = obj["baQExportID"]
      pass

class GetNewAlcParamsBAQ_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcParams_input:
   """ Required : 
   ds
   allocID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      self.allocID:str = obj["allocID"]
      pass

class GetNewAlcParams_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcRange1_input:
   """ Required : 
   ipAllocID
   ipParamNbr
   ipCOACode
   ds
   """  
   def __init__(self, obj):
      self.ipAllocID:str = obj["ipAllocID"]
      """  Allocation ID  """  
      self.ipParamNbr:int = obj["ipParamNbr"]
      """  Parameter Number  """  
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA Code  """  
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class GetNewAlcRange1_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcRange_input:
   """ Required : 
   ds
   allocID
   paramNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      self.allocID:str = obj["allocID"]
      self.paramNbr:int = obj["paramNbr"]
      pass

class GetNewAlcRange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcTarget_input:
   """ Required : 
   ds
   allocID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      self.allocID:str = obj["allocID"]
      pass

class GetNewAlcTarget_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOperatorsList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opOperatorsList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetOperatorsMenuList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMenuItem:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetParamMenuList_input:
   """ Required : 
   ipAllocID
   """  
   def __init__(self, obj):
      self.ipAllocID:str = obj["ipAllocID"]
      """  Allocation ID  """  
      pass

class GetParamMenuList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMenuItem:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetParametersList_input:
   """ Required : 
   ipAllocID
   """  
   def __init__(self, obj):
      self.ipAllocID:str = obj["ipAllocID"]
      """  Allocation ID  """  
      pass

class GetParametersList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opParametersList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAlcHed
   whereClauseAlcAcct
   whereClauseAlcAcctCat
   whereClauseAlcJrnCd
   whereClauseAlcParams
   whereClauseAlcNFSrc
   whereClauseAlcParamsBAQ
   whereClauseAlcRange
   whereClauseAlcTarget
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAlcHed:str = obj["whereClauseAlcHed"]
      self.whereClauseAlcAcct:str = obj["whereClauseAlcAcct"]
      self.whereClauseAlcAcctCat:str = obj["whereClauseAlcAcctCat"]
      self.whereClauseAlcJrnCd:str = obj["whereClauseAlcJrnCd"]
      self.whereClauseAlcParams:str = obj["whereClauseAlcParams"]
      self.whereClauseAlcNFSrc:str = obj["whereClauseAlcNFSrc"]
      self.whereClauseAlcParamsBAQ:str = obj["whereClauseAlcParamsBAQ"]
      self.whereClauseAlcRange:str = obj["whereClauseAlcRange"]
      self.whereClauseAlcTarget:str = obj["whereClauseAlcTarget"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AlcHedTableset] = obj["returnObj"]
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

class MaskValidate_input:
   """ Required : 
   tableName
   glAccount
   mask
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table name the tested account belongs to  """  
      self.glAccount:str = obj["glAccount"]
      """  GL account  """  
      self.mask:str = obj["mask"]
      """  Mask symbol '_' or '%'  """  
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class MaskValidate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefreshAllocationTotals_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class RefreshAllocationTotals_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RetrieveGLAcctDesc_input:
   """ Required : 
   ipType
   ds
   """  
   def __init__(self, obj):
      self.ipType:str = obj["ipType"]
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class RetrieveGLAcctDesc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateAcctBalAcct_input:
   """ Required : 
   ipUseTgtAcct
   ds
   """  
   def __init__(self, obj):
      self.ipUseTgtAcct:bool = obj["ipUseTgtAcct"]
      """  Use Target Account field value  """  
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class UpdateAcctBalAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAlcHedTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAlcHedTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidParamNatSegment_input:
   """ Required : 
   ipAllocID
   ipParamNbr
   ipSegment
   """  
   def __init__(self, obj):
      self.ipAllocID:str = obj["ipAllocID"]
      self.ipParamNbr:int = obj["ipParamNbr"]
      self.ipSegment:str = obj["ipSegment"]
      pass

class ValidParamNatSegment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWarnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidTgtNatSegment_input:
   """ Required : 
   ipAllocID
   ipSegment
   """  
   def __init__(self, obj):
      self.ipAllocID:str = obj["ipAllocID"]
      self.ipSegment:str = obj["ipSegment"]
      pass

class ValidTgtNatSegment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWarnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidatePercentTotals_input:
   """ Required : 
   ipAllocID
   """  
   def __init__(self, obj):
      self.ipAllocID:str = obj["ipAllocID"]
      pass

class ValidatePercentTotals_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWarnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class createNewBAQParams_input:
   """ Required : 
   ipBAQExportID
   ipAllocID
   ipParamNbr
   ds
   """  
   def __init__(self, obj):
      self.ipBAQExportID:str = obj["ipBAQExportID"]
      self.ipAllocID:str = obj["ipAllocID"]
      self.ipParamNbr:int = obj["ipParamNbr"]
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

class createNewBAQParams_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class getExternalMasterCOA_input:
   """ Required : 
   ProposedExtCompID
   """  
   def __init__(self, obj):
      self.ProposedExtCompID:str = obj["ProposedExtCompID"]
      pass

class getExternalMasterCOA_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

