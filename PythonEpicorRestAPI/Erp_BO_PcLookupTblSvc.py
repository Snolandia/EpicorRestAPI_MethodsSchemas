import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PcLookupTblSvc
# Description: PcLookupTbl Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PcLookupTbls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcLookupTbls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcLookupTbls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcLookupTblHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTbls",headers=creds) as resp:
           return await resp.json()

async def post_PcLookupTbls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcLookupTbls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcLookupTblHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcLookupTblHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTbls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcLookupTbls_Company_LookupTblID(Company, LookupTblID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcLookupTbl item
   Description: Calls GetByID to retrieve the PcLookupTbl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcLookupTbl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LookupTblID: Desc: LookupTblID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcLookupTblHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTbls(" + Company + "," + LookupTblID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcLookupTbls_Company_LookupTblID(Company, LookupTblID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcLookupTbl for the service
   Description: Calls UpdateExt to update PcLookupTbl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcLookupTbl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LookupTblID: Desc: LookupTblID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcLookupTblHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTbls(" + Company + "," + LookupTblID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcLookupTbls_Company_LookupTblID(Company, LookupTblID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcLookupTbl item
   Description: Call UpdateExt to delete PcLookupTbl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcLookupTbl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LookupTblID: Desc: LookupTblID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTbls(" + Company + "," + LookupTblID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcLookupTblHedAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcLookupTblHedAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcLookupTblHedAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcLookupTblHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblHedAttches",headers=creds) as resp:
           return await resp.json()

async def post_PcLookupTblHedAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcLookupTblHedAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcLookupTblHedAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcLookupTblHedAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblHedAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcLookupTblHedAttches_Company_LookupTblID_DrawingSeq(Company, LookupTblID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcLookupTblHedAttch item
   Description: Calls GetByID to retrieve the PcLookupTblHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcLookupTblHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LookupTblID: Desc: LookupTblID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcLookupTblHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblHedAttches(" + Company + "," + LookupTblID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcLookupTblHedAttches_Company_LookupTblID_DrawingSeq(Company, LookupTblID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcLookupTblHedAttch for the service
   Description: Calls UpdateExt to update PcLookupTblHedAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcLookupTblHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LookupTblID: Desc: LookupTblID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcLookupTblHedAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblHedAttches(" + Company + "," + LookupTblID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcLookupTblHedAttches_Company_LookupTblID_DrawingSeq(Company, LookupTblID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcLookupTblHedAttch item
   Description: Call UpdateExt to delete PcLookupTblHedAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcLookupTblHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LookupTblID: Desc: LookupTblID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblHedAttches(" + Company + "," + LookupTblID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcLookupColSetHeds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcLookupColSetHeds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcLookupColSetHeds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcLookupColSetHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetHeds",headers=creds) as resp:
           return await resp.json()

async def post_PcLookupColSetHeds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcLookupColSetHeds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcLookupColSetHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcLookupColSetHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetHeds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcLookupColSetHeds_Company_LookupTblID_ColSetID(Company, LookupTblID, ColSetID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcLookupColSetHed item
   Description: Calls GetByID to retrieve the PcLookupColSetHed item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcLookupColSetHed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LookupTblID: Desc: LookupTblID   Required: True   Allow empty value : True
      :param ColSetID: Desc: ColSetID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcLookupColSetHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetHeds(" + Company + "," + LookupTblID + "," + ColSetID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcLookupColSetHeds_Company_LookupTblID_ColSetID(Company, LookupTblID, ColSetID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcLookupColSetHed for the service
   Description: Calls UpdateExt to update PcLookupColSetHed. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcLookupColSetHed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LookupTblID: Desc: LookupTblID   Required: True   Allow empty value : True
      :param ColSetID: Desc: ColSetID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcLookupColSetHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetHeds(" + Company + "," + LookupTblID + "," + ColSetID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcLookupColSetHeds_Company_LookupTblID_ColSetID(Company, LookupTblID, ColSetID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcLookupColSetHed item
   Description: Call UpdateExt to delete PcLookupColSetHed item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcLookupColSetHed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LookupTblID: Desc: LookupTblID   Required: True   Allow empty value : True
      :param ColSetID: Desc: ColSetID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetHeds(" + Company + "," + LookupTblID + "," + ColSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcLookupColSetDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcLookupColSetDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcLookupColSetDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcLookupColSetDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetDtls",headers=creds) as resp:
           return await resp.json()

async def post_PcLookupColSetDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcLookupColSetDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcLookupColSetDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcLookupColSetDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcLookupColSetDtls_Company_LookupTblID_ColSetID_ColName(Company, LookupTblID, ColSetID, ColName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcLookupColSetDtl item
   Description: Calls GetByID to retrieve the PcLookupColSetDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcLookupColSetDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LookupTblID: Desc: LookupTblID   Required: True   Allow empty value : True
      :param ColSetID: Desc: ColSetID   Required: True   Allow empty value : True
      :param ColName: Desc: ColName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcLookupColSetDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetDtls(" + Company + "," + LookupTblID + "," + ColSetID + "," + ColName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcLookupColSetDtls_Company_LookupTblID_ColSetID_ColName(Company, LookupTblID, ColSetID, ColName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcLookupColSetDtl for the service
   Description: Calls UpdateExt to update PcLookupColSetDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcLookupColSetDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LookupTblID: Desc: LookupTblID   Required: True   Allow empty value : True
      :param ColSetID: Desc: ColSetID   Required: True   Allow empty value : True
      :param ColName: Desc: ColName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcLookupColSetDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetDtls(" + Company + "," + LookupTblID + "," + ColSetID + "," + ColName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcLookupColSetDtls_Company_LookupTblID_ColSetID_ColName(Company, LookupTblID, ColSetID, ColName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcLookupColSetDtl item
   Description: Call UpdateExt to delete PcLookupColSetDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcLookupColSetDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LookupTblID: Desc: LookupTblID   Required: True   Allow empty value : True
      :param ColSetID: Desc: ColSetID   Required: True   Allow empty value : True
      :param ColName: Desc: ColName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetDtls(" + Company + "," + LookupTblID + "," + ColSetID + "," + ColName + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcLookupTblValues(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcLookupTblValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcLookupTblValues
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcLookupTblValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblValues",headers=creds) as resp:
           return await resp.json()

async def post_PcLookupTblValues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcLookupTblValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcLookupTblValuesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcLookupTblValuesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblValues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcLookupTblValues_Company_LookupTblID_RowNum_ColName(Company, LookupTblID, RowNum, ColName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcLookupTblValue item
   Description: Calls GetByID to retrieve the PcLookupTblValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcLookupTblValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LookupTblID: Desc: LookupTblID   Required: True   Allow empty value : True
      :param RowNum: Desc: RowNum   Required: True
      :param ColName: Desc: ColName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcLookupTblValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblValues(" + Company + "," + LookupTblID + "," + RowNum + "," + ColName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcLookupTblValues_Company_LookupTblID_RowNum_ColName(Company, LookupTblID, RowNum, ColName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcLookupTblValue for the service
   Description: Calls UpdateExt to update PcLookupTblValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcLookupTblValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LookupTblID: Desc: LookupTblID   Required: True   Allow empty value : True
      :param RowNum: Desc: RowNum   Required: True
      :param ColName: Desc: ColName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcLookupTblValuesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblValues(" + Company + "," + LookupTblID + "," + RowNum + "," + ColName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcLookupTblValues_Company_LookupTblID_RowNum_ColName(Company, LookupTblID, RowNum, ColName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcLookupTblValue item
   Description: Call UpdateExt to delete PcLookupTblValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcLookupTblValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LookupTblID: Desc: LookupTblID   Required: True   Allow empty value : True
      :param RowNum: Desc: RowNum   Required: True
      :param ColName: Desc: ColName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblValues(" + Company + "," + LookupTblID + "," + RowNum + "," + ColName + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcLookupTblListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePcLookupTblHed, whereClausePcLookupTblHedAttch, whereClausePcLookupColSetHed, whereClausePcLookupColSetDtl, whereClausePcLookupTblValues, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClausePcLookupTblHed=" + whereClausePcLookupTblHed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcLookupTblHedAttch=" + whereClausePcLookupTblHedAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcLookupColSetHed=" + whereClausePcLookupColSetHed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcLookupColSetDtl=" + whereClausePcLookupColSetDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcLookupTblValues=" + whereClausePcLookupTblValues
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(lookupTblID, epicorHeaders = None):
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
   params += "lookupTblID=" + lookupTblID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetDisplayColumns(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDisplayColumns
   Description: Generate Columns that will be displayed in the grid
   OperationID: GetDisplayColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDisplayColumns_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDisplayColumns_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFormatOptions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFormatOptions
   Description: Get the valid options that are used for populating format options.
   OperationID: GetFormatOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFormatOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFormatOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportPcLookupTblFromCSV(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportPcLookupTblFromCSV
   Description: Create a new PCLookupImportExportTableset from the imported CSV file and then call the ImportPcLookupTbl to insert it into the database.
   OperationID: ImportPcLookupTblFromCSV
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportPcLookupTblFromCSV_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportPcLookupTblFromCSV_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportPcLookupTbl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportPcLookupTbl
   Description: Inserts values into database from the imported file.
   OperationID: ImportPcLookupTbl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportPcLookupTbl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportPcLookupTbl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetExportPcLookupTables(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExportPcLookupTables
   Description: Gets the PcLookupTbl records set to export
   OperationID: GetExportPcLookupTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExportPcLookupTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExportPcLookupTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDataTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDataTable
   OperationID: GetDataTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDataTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyColSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyColSet
   Description: Copy column set from source to desctination.
   OperationID: CopyColSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyColSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyColSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateLookupTblValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateLookupTblValue
   Description: Update lookup table value
   OperationID: UpdateLookupTblValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateLookupTblValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateLookupTblValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteLookupTblValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteLookupTblValue
   Description: Delete lookup table row
   OperationID: DeleteLookupTblValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteLookupTblValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteLookupTblValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcLookupTblDisplay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcLookupTblDisplay
   Description: Creates new Lookup table row
   OperationID: GetNewPcLookupTblDisplay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcLookupTblDisplay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcLookupTblDisplay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ColSetDtlColumnChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ColSetDtlColumnChanged
   OperationID: ColSetDtlColumnChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ColSetDtlColumnChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ColSetDtlColumnChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMinValueOfDecimals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMinValueOfDecimals
   Description: Returns minimum value of decimals.
   OperationID: GetMinValueOfDecimals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMinValueOfDecimals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMinValueOfDecimals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportLookupTbl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportLookupTbl
   Description: Export table(s) from Kinetic
   OperationID: ExportLookupTbl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportLookupTbl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportLookupTbl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportPcLookupTableExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportPcLookupTableExt
   Description: Main entry point for import files  from Kinetic
   OperationID: ImportPcLookupTableExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportPcLookupTableExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportPcLookupTableExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportPcLookupTableFromCSV(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportPcLookupTableFromCSV
   Description: Process CVS file to DataTable structure
   OperationID: ImportPcLookupTableFromCSV
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportPcLookupTableFromCSV_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportPcLookupTableFromCSV_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ColSetIDColumnChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ColSetIDColumnChanging
   OperationID: ColSetIDColumnChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ColSetIDColumnChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ColSetIDColumnChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcLookupTblHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcLookupTblHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcLookupTblHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcLookupTblHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcLookupTblHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcLookupTblHedAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcLookupTblHedAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcLookupTblHedAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcLookupTblHedAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcLookupTblHedAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcLookupColSetHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcLookupColSetHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcLookupColSetHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcLookupColSetHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcLookupColSetHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcLookupColSetDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcLookupColSetDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcLookupColSetDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcLookupColSetDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcLookupColSetDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcLookupTblValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcLookupTblValues
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcLookupTblValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcLookupTblValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcLookupTblValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupColSetDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcLookupColSetDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupColSetHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcLookupColSetHedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupTblHedAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcLookupTblHedAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupTblHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcLookupTblHedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupTblListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcLookupTblListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupTblValuesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcLookupTblValuesRow] = obj["value"]
      pass

class Erp_Tablesets_PcLookupColSetDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LookupTblID:str = obj["LookupTblID"]
      """  LookupTblID  """  
      self.ColSetID:str = obj["ColSetID"]
      """  ColSetID  """  
      self.ColName:str = obj["ColName"]
      """  ColName  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.ColFormat:str = obj["ColFormat"]
      """  ColFormat  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllowNegative:bool = obj["AllowNegative"]
      """  AllowNegative  """  
      self.NumericOnly:bool = obj["NumericOnly"]
      """  NumericOnly  """  
      self.UseSeparator:bool = obj["UseSeparator"]
      """  UseSeparator  """  
      self.Digits:int = obj["Digits"]
      """  Digits  """  
      self.Decimals:int = obj["Decimals"]
      """  Decimals  """  
      self.DisplayFormat:str = obj["DisplayFormat"]
      self.StringDigits:int = obj["StringDigits"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcLookupColSetHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LookupTblID:str = obj["LookupTblID"]
      """  LookupTblID  """  
      self.ColSetID:str = obj["ColSetID"]
      """  ColSetID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Template:bool = obj["Template"]
      """  Template  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.UsedExternally:bool = obj["UsedExternally"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcLookupTblHedAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LookupTblID:str = obj["LookupTblID"]
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

class Erp_Tablesets_PcLookupTblHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LookupTblID:str = obj["LookupTblID"]
      """  LookupTblID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.GlobalLookup:bool = obj["GlobalLookup"]
      """  GlobalLookup  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if Lookup table is global (master or link)  """  
      self.EnableGlobalLookup:bool = obj["EnableGlobalLookup"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcLookupTblListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LookupTblID:str = obj["LookupTblID"]
      """  LookupTblID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.GlobalLookup:bool = obj["GlobalLookup"]
      """  GlobalLookup  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcLookupTblValuesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LookupTblID:str = obj["LookupTblID"]
      """  LookupTblID  """  
      self.RowNum:int = obj["RowNum"]
      """  RowNum  """  
      self.ColName:str = obj["ColName"]
      """  ColName  """  
      self.ColSetID:str = obj["ColSetID"]
      """  ColSetID  """  
      self.RowSetID:str = obj["RowSetID"]
      """  RowSetID  """  
      self.DataValue:str = obj["DataValue"]
      """  DataValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DataValueDecimal:int = obj["DataValueDecimal"]
      """  DataValueDecimal  """  
      self.DataValueBool:bool = obj["DataValueBool"]
      """  DataValueBool  """  
      self.DataValueDate:str = obj["DataValueDate"]
      """  DataValueDate  """  
      self.DataValueString:str = obj["DataValueString"]
      """  DataValueString  """  
      self.DataType:str = obj["DataType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ColSetDtlColumnChanged_input:
   """ Required : 
   proposedValue
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:str = obj["proposedValue"]
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

class ColSetDtlColumnChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ColSetIDColumnChanging_input:
   """ Required : 
   proposedValue
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:str = obj["proposedValue"]
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

class ColSetIDColumnChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CopyColSet_input:
   """ Required : 
   sourceLookupTblID
   sourceColSetID
   destLookupTblID
   ds
   """  
   def __init__(self, obj):
      self.sourceLookupTblID:str = obj["sourceLookupTblID"]
      self.sourceColSetID:str = obj["sourceColSetID"]
      self.destLookupTblID:str = obj["destLookupTblID"]
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

class CopyColSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   lookupTblID
   """  
   def __init__(self, obj):
      self.lookupTblID:str = obj["lookupTblID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteLookupTblValue_input:
   """ Required : 
   lookupTblID
   rowNum
   """  
   def __init__(self, obj):
      self.lookupTblID:str = obj["lookupTblID"]
      self.rowNum:int = obj["rowNum"]
      pass

class DeleteLookupTblValue_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DynFieldAttributesRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      self.FieldName:str = obj["FieldName"]
      self.DataType:str = obj["DataType"]
      self.Required:bool = obj["Required"]
      self.ReadOnly:bool = obj["ReadOnly"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.LikeDataFieldSystemCode:str = obj["LikeDataFieldSystemCode"]
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.CurrencyCodeColumn:str = obj["CurrencyCodeColumn"]
      self.CurrencyType:str = obj["CurrencyType"]
      self.CurrencySource:str = obj["CurrencySource"]
      self.BizType:str = obj["BizType"]
      self.CGCCode:str = obj["CGCCode"]
      self.UomColumn:str = obj["UomColumn"]
      self.CodeDescriptionList:str = obj["CodeDescriptionList"]
      self.Seq:int = obj["Seq"]
      self.IsHidden:bool = obj["IsHidden"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynFieldHelpRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      self.FieldName:str = obj["FieldName"]
      self.Description:str = obj["Description"]
      self.DBTableName:str = obj["DBTableName"]
      self.DBFieldName:str = obj["DBFieldName"]
      self.External:bool = obj["External"]
      self.InitialValue:str = obj["InitialValue"]
      self.IsDescriptionField:bool = obj["IsDescriptionField"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynTableAttributesRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      """  The actual generic table name used by the BL  """  
      self.UniqueTableID:str = obj["UniqueTableID"]
      """  Unique identifier for the virtual schema  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynamicMetadataTableset:
   def __init__(self, obj):
      self.DynTableAttributes:list[Erp_Tablesets_DynTableAttributesRow] = obj["DynTableAttributes"]
      self.DynFieldAttributes:list[Erp_Tablesets_DynFieldAttributesRow] = obj["DynFieldAttributes"]
      self.DynFieldHelp:list[Erp_Tablesets_DynFieldHelpRow] = obj["DynFieldHelp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcLookupColSetDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LookupTblID:str = obj["LookupTblID"]
      """  LookupTblID  """  
      self.ColSetID:str = obj["ColSetID"]
      """  ColSetID  """  
      self.ColName:str = obj["ColName"]
      """  ColName  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.ColFormat:str = obj["ColFormat"]
      """  ColFormat  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllowNegative:bool = obj["AllowNegative"]
      """  AllowNegative  """  
      self.NumericOnly:bool = obj["NumericOnly"]
      """  NumericOnly  """  
      self.UseSeparator:bool = obj["UseSeparator"]
      """  UseSeparator  """  
      self.Digits:int = obj["Digits"]
      """  Digits  """  
      self.Decimals:int = obj["Decimals"]
      """  Decimals  """  
      self.DisplayFormat:str = obj["DisplayFormat"]
      self.StringDigits:int = obj["StringDigits"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcLookupColSetHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LookupTblID:str = obj["LookupTblID"]
      """  LookupTblID  """  
      self.ColSetID:str = obj["ColSetID"]
      """  ColSetID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Template:bool = obj["Template"]
      """  Template  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.UsedExternally:bool = obj["UsedExternally"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcLookupImportExportTableset:
   def __init__(self, obj):
      self.PcLookupTblHed:list[Erp_Tablesets_PcLookupTblHedRow] = obj["PcLookupTblHed"]
      self.PcLookupColSetDtl:list[Erp_Tablesets_PcLookupColSetDtlRow] = obj["PcLookupColSetDtl"]
      self.PcLookupColSetHed:list[Erp_Tablesets_PcLookupColSetHedRow] = obj["PcLookupColSetHed"]
      self.PcLookupTblValues:list[Erp_Tablesets_PcLookupTblValuesRow] = obj["PcLookupTblValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcLookupTblDispColumnsRow:
   def __init__(self, obj):
      self.ColSetID:str = obj["ColSetID"]
      self.ColumnFormat:str = obj["ColumnFormat"]
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnSequence:int = obj["ColumnSequence"]
      self.ColumnType:str = obj["ColumnType"]
      self.LookupTblID:str = obj["LookupTblID"]
      """  The ID of the Lookup Table.  """  
      self.Digits:int = obj["Digits"]
      self.Decimals:int = obj["Decimals"]
      self.AllowNegatives:bool = obj["AllowNegatives"]
      self.UseSeparator:bool = obj["UseSeparator"]
      self.NumericOnly:bool = obj["NumericOnly"]
      self.StringDigits:int = obj["StringDigits"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcLookupTblDisplayTableset:
   def __init__(self, obj):
      self.PcLookupTblDispColumns:list[Erp_Tablesets_PcLookupTblDispColumnsRow] = obj["PcLookupTblDispColumns"]
      self.PcLookupTblValues:list[Erp_Tablesets_PcLookupTblValuesRow] = obj["PcLookupTblValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcLookupTblHedAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LookupTblID:str = obj["LookupTblID"]
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

class Erp_Tablesets_PcLookupTblHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LookupTblID:str = obj["LookupTblID"]
      """  LookupTblID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.GlobalLookup:bool = obj["GlobalLookup"]
      """  GlobalLookup  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if Lookup table is global (master or link)  """  
      self.EnableGlobalLookup:bool = obj["EnableGlobalLookup"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcLookupTblListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LookupTblID:str = obj["LookupTblID"]
      """  LookupTblID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.GlobalLookup:bool = obj["GlobalLookup"]
      """  GlobalLookup  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcLookupTblListTableset:
   def __init__(self, obj):
      self.PcLookupTblList:list[Erp_Tablesets_PcLookupTblListRow] = obj["PcLookupTblList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcLookupTblTableset:
   def __init__(self, obj):
      self.PcLookupTblHed:list[Erp_Tablesets_PcLookupTblHedRow] = obj["PcLookupTblHed"]
      self.PcLookupTblHedAttch:list[Erp_Tablesets_PcLookupTblHedAttchRow] = obj["PcLookupTblHedAttch"]
      self.PcLookupColSetHed:list[Erp_Tablesets_PcLookupColSetHedRow] = obj["PcLookupColSetHed"]
      self.PcLookupColSetDtl:list[Erp_Tablesets_PcLookupColSetDtlRow] = obj["PcLookupColSetDtl"]
      self.PcLookupTblValues:list[Erp_Tablesets_PcLookupTblValuesRow] = obj["PcLookupTblValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcLookupTblValuesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LookupTblID:str = obj["LookupTblID"]
      """  LookupTblID  """  
      self.RowNum:int = obj["RowNum"]
      """  RowNum  """  
      self.ColName:str = obj["ColName"]
      """  ColName  """  
      self.ColSetID:str = obj["ColSetID"]
      """  ColSetID  """  
      self.RowSetID:str = obj["RowSetID"]
      """  RowSetID  """  
      self.DataValue:str = obj["DataValue"]
      """  DataValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DataValueDecimal:int = obj["DataValueDecimal"]
      """  DataValueDecimal  """  
      self.DataValueBool:bool = obj["DataValueBool"]
      """  DataValueBool  """  
      self.DataValueDate:str = obj["DataValueDate"]
      """  DataValueDate  """  
      self.DataValueString:str = obj["DataValueString"]
      """  DataValueString  """  
      self.DataType:str = obj["DataType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtPcLookupTblTableset:
   def __init__(self, obj):
      self.PcLookupTblHed:list[Erp_Tablesets_PcLookupTblHedRow] = obj["PcLookupTblHed"]
      self.PcLookupTblHedAttch:list[Erp_Tablesets_PcLookupTblHedAttchRow] = obj["PcLookupTblHedAttch"]
      self.PcLookupColSetHed:list[Erp_Tablesets_PcLookupColSetHedRow] = obj["PcLookupColSetHed"]
      self.PcLookupColSetDtl:list[Erp_Tablesets_PcLookupColSetDtlRow] = obj["PcLookupColSetDtl"]
      self.PcLookupTblValues:list[Erp_Tablesets_PcLookupTblValuesRow] = obj["PcLookupTblValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportLookupTbl_input:
   """ Required : 
   lookupTblID
   fileName
   fileType
   """  
   def __init__(self, obj):
      self.lookupTblID:str = obj["lookupTblID"]
      """  One ID or delimited list of IDs for export.  """  
      self.fileName:str = obj["fileName"]
      """  Empty or subfolders of UserData server special folder  """  
      self.fileType:str = obj["fileType"]
      """  xml or csv  """  
      pass

class ExportLookupTbl_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcLookupImportExportTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   lookupTblID
   """  
   def __init__(self, obj):
      self.lookupTblID:str = obj["lookupTblID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcLookupTblTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PcLookupTblTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PcLookupTblTableset] = obj["returnObj"]
      pass

class GetDataTable_input:
   """ Required : 
   lookupTblID
   """  
   def __init__(self, obj):
      self.lookupTblID:str = obj["lookupTblID"]
      pass

class GetDataTable_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynamicMetadataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDisplayColumns_input:
   """ Required : 
   inLookupTblID
   """  
   def __init__(self, obj):
      self.inLookupTblID:str = obj["inLookupTblID"]
      """  The LookupTbl ID  """  
      pass

class GetDisplayColumns_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcLookupTblDisplayTableset] = obj["returnObj"]
      pass

class GetExportPcLookupTables_input:
   """ Required : 
   pcLookupTblID
   """  
   def __init__(self, obj):
      self.pcLookupTblID:str = obj["pcLookupTblID"]
      """  The PcLookupTbl Ids  """  
      pass

class GetExportPcLookupTables_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcLookupImportExportTableset] = obj["returnObj"]
      pass

class GetFormatOptions_input:
   """ Required : 
   optionType
   """  
   def __init__(self, obj):
      self.optionType:str = obj["optionType"]
      """  The type of option to get.
             Valid values are: NumberFormats, PriceMultipliers,
             SmartStringDateFormats, SmartStringDateSeparators, SmartStringLogicalFormats, NumFormatSignOptions, HTMLProducts  """  
      pass

class GetFormatOptions_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.optionList:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_PcLookupTblListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMinValueOfDecimals_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

class GetMinValueOfDecimals_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcLookupColSetDtl_input:
   """ Required : 
   ds
   lookupTblID
   colSetID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      self.lookupTblID:str = obj["lookupTblID"]
      self.colSetID:str = obj["colSetID"]
      pass

class GetNewPcLookupColSetDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcLookupColSetHed_input:
   """ Required : 
   ds
   lookupTblID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      self.lookupTblID:str = obj["lookupTblID"]
      pass

class GetNewPcLookupColSetHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcLookupTblDisplay_input:
   """ Required : 
   lookupTblID
   colSetID
   """  
   def __init__(self, obj):
      self.lookupTblID:str = obj["lookupTblID"]
      self.colSetID:str = obj["colSetID"]
      pass

class GetNewPcLookupTblDisplay_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynamicMetadataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcLookupTblHedAttch_input:
   """ Required : 
   ds
   lookupTblID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      self.lookupTblID:str = obj["lookupTblID"]
      pass

class GetNewPcLookupTblHedAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcLookupTblHed_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

class GetNewPcLookupTblHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcLookupTblValues_input:
   """ Required : 
   ds
   lookupTblID
   rowNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      self.lookupTblID:str = obj["lookupTblID"]
      self.rowNum:int = obj["rowNum"]
      pass

class GetNewPcLookupTblValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePcLookupTblHed
   whereClausePcLookupTblHedAttch
   whereClausePcLookupColSetHed
   whereClausePcLookupColSetDtl
   whereClausePcLookupTblValues
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePcLookupTblHed:str = obj["whereClausePcLookupTblHed"]
      self.whereClausePcLookupTblHedAttch:str = obj["whereClausePcLookupTblHedAttch"]
      self.whereClausePcLookupColSetHed:str = obj["whereClausePcLookupColSetHed"]
      self.whereClausePcLookupColSetDtl:str = obj["whereClausePcLookupColSetDtl"]
      self.whereClausePcLookupTblValues:str = obj["whereClausePcLookupTblValues"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcLookupTblTableset] = obj["returnObj"]
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

class ImportPcLookupTableExt_input:
   """ Required : 
   files
   processOption
   columnOption
   valuesOption
   ds
   """  
   def __init__(self, obj):
      self.files:str = obj["files"]
      self.processOption:str = obj["processOption"]
      self.columnOption:str = obj["columnOption"]
      self.valuesOption:str = obj["valuesOption"]
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

class ImportPcLookupTableExt_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ImportPcLookupTableFromCSV_input:
   """ Required : 
   fileName
   processOption
   columnOption
   valuesOption
   ds
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      self.processOption:str = obj["processOption"]
      self.columnOption:str = obj["columnOption"]
      self.valuesOption:str = obj["valuesOption"]
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

class ImportPcLookupTableFromCSV_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ImportPcLookupTblFromCSV_input:
   """ Required : 
   columnOption
   valuesOption
   dataSet
   lookupTblID
   lookupTblDesc
   lookupTblGlobalLookup
   lookupTblGlobalLock
   colSetID
   colSetDesc
   colSetTemplate
   """  
   def __init__(self, obj):
      self.columnOption:str = obj["columnOption"]
      self.valuesOption:str = obj["valuesOption"]
      self.dataSet      #schema had no properties on an object.
      self.lookupTblID:str = obj["lookupTblID"]
      self.lookupTblDesc:str = obj["lookupTblDesc"]
      self.lookupTblGlobalLookup:bool = obj["lookupTblGlobalLookup"]
      self.lookupTblGlobalLock:bool = obj["lookupTblGlobalLock"]
      self.colSetID:str = obj["colSetID"]
      self.colSetDesc:str = obj["colSetDesc"]
      self.colSetTemplate:bool = obj["colSetTemplate"]
      pass

class ImportPcLookupTblFromCSV_output:
   def __init__(self, obj):
      pass

class ImportPcLookupTbl_input:
   """ Required : 
   columnOption
   valuesOption
   ttPcLookupImportExportDS
   lookupTblID
   colsetID
   """  
   def __init__(self, obj):
      self.columnOption:str = obj["columnOption"]
      self.valuesOption:str = obj["valuesOption"]
      self.ttPcLookupImportExportDS:list[Erp_Tablesets_PcLookupImportExportTableset] = obj["ttPcLookupImportExportDS"]
      self.lookupTblID:str = obj["lookupTblID"]
      self.colsetID:str = obj["colsetID"]
      pass

class ImportPcLookupTbl_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPcLookupTblTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPcLookupTblTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateLookupTblValue_input:
   """ Required : 
   lookupTblID
   colSetID
   rowNum
   colName
   proposedValue
   rowGuid
   ds
   """  
   def __init__(self, obj):
      self.lookupTblID:str = obj["lookupTblID"]
      self.colSetID:str = obj["colSetID"]
      self.rowNum:int = obj["rowNum"]
      self.colName:str = obj["colName"]
      self.proposedValue:str = obj["proposedValue"]
      self.rowGuid:str = obj["rowGuid"]
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

class UpdateLookupTblValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.rowGuid:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcLookupTblTableset] = obj["ds"]
      pass

      """  output parameters  """  

