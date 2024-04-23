import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PCashEntrySvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PCashEntries(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PCashEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDocRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries",headers=creds) as resp:
           return await resp.json()

async def post_PCashEntries(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashDocRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PCashDocRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PCashEntries_Company_CashDeskID_ReferenceNum(Company, CashDeskID, ReferenceNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PCashEntry item
   Description: Calls GetByID to retrieve the PCashEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDocRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PCashEntries_Company_CashDeskID_ReferenceNum(Company, CashDeskID, ReferenceNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PCashEntry for the service
   Description: Calls UpdateExt to update PCashEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashDocRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PCashEntries_Company_CashDeskID_ReferenceNum(Company, CashDeskID, ReferenceNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PCashEntry item
   Description: Call UpdateExt to delete PCashEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PCashEntries_Company_CashDeskID_ReferenceNum_PCashDocTGLCs(Company, CashDeskID, ReferenceNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PCashDocTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PCashDocTGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDocTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")/PCashDocTGLCs",headers=creds) as resp:
           return await resp.json()

async def get_PCashEntries_Company_CashDeskID_ReferenceNum_PCashDocTGLCs_Company_CashDeskID_ReferenceNum_SysRowID(Company, CashDeskID, ReferenceNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PCashDocTGLC item
   Description: Calls GetByID to retrieve the PCashDocTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDocTGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDocTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")/PCashDocTGLCs(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PCashEntries_Company_CashDeskID_ReferenceNum_BankTrans(Company, CashDeskID, ReferenceNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BankTrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankTrans1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")/BankTrans",headers=creds) as resp:
           return await resp.json()

async def get_PCashEntries_Company_CashDeskID_ReferenceNum_BankTrans_Company_BankAcctID_TranNum_Voided(Company, CashDeskID, ReferenceNum, BankAcctID, TranNum, Voided, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTran item
   Description: Calls GetByID to retrieve the BankTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTran1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def get_PCashEntries_Company_CashDeskID_ReferenceNum_PCashDocLinkeds(Company, CashDeskID, ReferenceNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PCashDocLinkeds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PCashDocLinkeds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDocLinkedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")/PCashDocLinkeds",headers=creds) as resp:
           return await resp.json()

async def get_PCashEntries_Company_CashDeskID_ReferenceNum_PCashDocLinkeds_Company_CashDeskID_ReferenceNum_LinkedSeq(Company, CashDeskID, ReferenceNum, LinkedSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PCashDocLinked item
   Description: Calls GetByID to retrieve the PCashDocLinked item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDocLinked1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param LinkedSeq: Desc: LinkedSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDocLinkedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")/PCashDocLinkeds(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + LinkedSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PCashEntries_Company_CashDeskID_ReferenceNum_PCashDocAttches(Company, CashDeskID, ReferenceNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PCashDocAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PCashDocAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDocAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")/PCashDocAttches",headers=creds) as resp:
           return await resp.json()

async def get_PCashEntries_Company_CashDeskID_ReferenceNum_PCashDocAttches_Company_CashDeskID_ReferenceNum_DrawingSeq(Company, CashDeskID, ReferenceNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PCashDocAttch item
   Description: Calls GetByID to retrieve the PCashDocAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDocAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDocAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashEntries(" + Company + "," + CashDeskID + "," + ReferenceNum + ")/PCashDocAttches(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PCashDocTGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PCashDocTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashDocTGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDocTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocTGLCs",headers=creds) as resp:
           return await resp.json()

async def post_PCashDocTGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashDocTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashDocTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PCashDocTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocTGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PCashDocTGLCs_Company_CashDeskID_ReferenceNum_SysRowID(Company, CashDeskID, ReferenceNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PCashDocTGLC item
   Description: Calls GetByID to retrieve the PCashDocTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDocTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDocTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocTGLCs(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PCashDocTGLCs_Company_CashDeskID_ReferenceNum_SysRowID(Company, CashDeskID, ReferenceNum, SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PCashDocTGLC for the service
   Description: Calls UpdateExt to update PCashDocTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashDocTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashDocTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocTGLCs(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PCashDocTGLCs_Company_CashDeskID_ReferenceNum_SysRowID(Company, CashDeskID, ReferenceNum, SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PCashDocTGLC item
   Description: Call UpdateExt to delete PCashDocTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashDocTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocTGLCs(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankTrans(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BankTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankTrans
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans",headers=creds) as resp:
           return await resp.json()

async def post_BankTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BankTrans_Company_BankAcctID_TranNum_Voided(Company, BankAcctID, TranNum, Voided, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTran item
   Description: Calls GetByID to retrieve the BankTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BankTrans_Company_BankAcctID_TranNum_Voided(Company, BankAcctID, TranNum, Voided, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BankTran for the service
   Description: Calls UpdateExt to update BankTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BankTrans_Company_BankAcctID_TranNum_Voided(Company, BankAcctID, TranNum, Voided, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BankTran item
   Description: Call UpdateExt to delete BankTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranTaxDtls(Company, BankAcctID, TranNum, Voided, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BankTranTaxDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankTranTaxDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranTaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTaxDtls",headers=creds) as resp:
           return await resp.json()

async def get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company, BankAcctID, TranNum, Voided, SourceModule, HeadNum, APTranNo, InvoiceNum, InvoiceRef, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTranTaxDtl item
   Description: Calls GetByID to retrieve the BankTranTaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTranTaxDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranTGLCs(Company, BankAcctID, TranNum, Voided, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BankTranTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankTranTGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTGLCs",headers=creds) as resp:
           return await resp.json()

async def get_BankTrans_Company_BankAcctID_TranNum_Voided_BankTranTGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company, BankAcctID, TranNum, Voided, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTranTGLC item
   Description: Calls GetByID to retrieve the BankTranTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTranTGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTrans(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + ")/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankTranTaxDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BankTranTaxDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankTranTaxDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranTaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTaxDtls",headers=creds) as resp:
           return await resp.json()

async def post_BankTranTaxDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankTranTaxDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTaxDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BankTranTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company, SourceModule, HeadNum, APTranNo, InvoiceNum, InvoiceRef, BankAcctID, TranNum, Voided, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTranTaxDtl item
   Description: Calls GetByID to retrieve the BankTranTaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTranTaxDtl
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BankTranTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company, SourceModule, HeadNum, APTranNo, InvoiceNum, InvoiceRef, BankAcctID, TranNum, Voided, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BankTranTaxDtl for the service
   Description: Calls UpdateExt to update BankTranTaxDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankTranTaxDtl
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
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankTranTaxDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BankTranTaxDtls_Company_SourceModule_HeadNum_APTranNo_InvoiceNum_InvoiceRef_BankAcctID_TranNum_Voided_TaxCode_RateCode_ECAcquisitionSeq(Company, SourceModule, HeadNum, APTranNo, InvoiceNum, InvoiceRef, BankAcctID, TranNum, Voided, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BankTranTaxDtl item
   Description: Call UpdateExt to delete BankTranTaxDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankTranTaxDtl
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTaxDtls(" + Company + "," + SourceModule + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + InvoiceRef + "," + BankAcctID + "," + TranNum + "," + Voided + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankTranTGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BankTranTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankTranTGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankTranTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTGLCs",headers=creds) as resp:
           return await resp.json()

async def post_BankTranTGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankTranTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BankTranTGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company, BankAcctID, TranNum, Voided, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankTranTGLC item
   Description: Calls GetByID to retrieve the BankTranTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankTranTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BankTranTGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company, BankAcctID, TranNum, Voided, SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BankTranTGLC for the service
   Description: Calls UpdateExt to update BankTranTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankTranTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankTranTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BankTranTGLCs_Company_BankAcctID_TranNum_Voided_SysRowID(Company, BankAcctID, TranNum, Voided, SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BankTranTGLC item
   Description: Call UpdateExt to delete BankTranTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankTranTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param Voided: Desc: Voided   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/BankTranTGLCs(" + Company + "," + BankAcctID + "," + TranNum + "," + Voided + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PCashDocLinkeds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PCashDocLinkeds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashDocLinkeds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDocLinkedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocLinkeds",headers=creds) as resp:
           return await resp.json()

async def post_PCashDocLinkeds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashDocLinkeds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashDocLinkedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PCashDocLinkedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocLinkeds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PCashDocLinkeds_Company_CashDeskID_ReferenceNum_LinkedSeq(Company, CashDeskID, ReferenceNum, LinkedSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PCashDocLinked item
   Description: Calls GetByID to retrieve the PCashDocLinked item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDocLinked
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param LinkedSeq: Desc: LinkedSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDocLinkedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocLinkeds(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + LinkedSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PCashDocLinkeds_Company_CashDeskID_ReferenceNum_LinkedSeq(Company, CashDeskID, ReferenceNum, LinkedSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PCashDocLinked for the service
   Description: Calls UpdateExt to update PCashDocLinked. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashDocLinked
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param LinkedSeq: Desc: LinkedSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashDocLinkedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocLinkeds(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + LinkedSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PCashDocLinkeds_Company_CashDeskID_ReferenceNum_LinkedSeq(Company, CashDeskID, ReferenceNum, LinkedSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PCashDocLinked item
   Description: Call UpdateExt to delete PCashDocLinked item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashDocLinked
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param LinkedSeq: Desc: LinkedSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocLinkeds(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + LinkedSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PCashDocAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PCashDocAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashDocAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDocAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocAttches",headers=creds) as resp:
           return await resp.json()

async def post_PCashDocAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashDocAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashDocAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PCashDocAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PCashDocAttches_Company_CashDeskID_ReferenceNum_DrawingSeq(Company, CashDeskID, ReferenceNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PCashDocAttch item
   Description: Calls GetByID to retrieve the PCashDocAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDocAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDocAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocAttches(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PCashDocAttches_Company_CashDeskID_ReferenceNum_DrawingSeq(Company, CashDeskID, ReferenceNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PCashDocAttch for the service
   Description: Calls UpdateExt to update PCashDocAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashDocAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashDocAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocAttches(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PCashDocAttches_Company_CashDeskID_ReferenceNum_DrawingSeq(Company, CashDeskID, ReferenceNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PCashDocAttch item
   Description: Call UpdateExt to delete PCashDocAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashDocAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param ReferenceNum: Desc: ReferenceNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/PCashDocAttches(" + Company + "," + CashDeskID + "," + ReferenceNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/LegalNumGenOpts",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDocListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePCashDoc, whereClausePCashDocAttch, whereClauseBankTran, whereClauseBankTranTaxDtl, whereClauseBankTranTGLC, whereClausePCashDocLinked, whereClausePCashDocTGLC, whereClauseLegalNumGenOpts, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePCashDoc=" + whereClausePCashDoc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePCashDocAttch=" + whereClausePCashDocAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBankTran=" + whereClauseBankTran
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBankTranTaxDtl=" + whereClauseBankTranTaxDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBankTranTGLC=" + whereClauseBankTranTGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePCashDocLinked=" + whereClausePCashDocLinked
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePCashDocTGLC=" + whereClausePCashDocTGLC
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(cashDeskID, referenceNum, epicorHeaders = None):
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
   params += "cashDeskID=" + cashDeskID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "referenceNum=" + referenceNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateLine
   Description: Call this method before calling other business objects like
Cash Receipts, PaymentEntry, Bank Adjustment etc.
This method creates the CashBDtl record and any other records
required to call the business object.
   OperationID: CreateLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBankFeeDefaultAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBankFeeDefaultAccount
   Description: This method is used to get the default account(s) for a Bank Fee
   OperationID: GetBankFeeDefaultAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankFeeDefaultAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankFeeDefaultAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankTranForPCashDoc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankTranForPCashDoc
   Description: Get New BankTran record for Petty Cash Document
   OperationID: GetNewBankTranForPCashDoc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankTranForPCashDoc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTranForPCashDoc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPCashDocByType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPCashDocByType
   OperationID: GetNewPCashDocByType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCashDocByType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashDocByType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPCashDocDefaultAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPCashDocDefaultAccount
   Description: This method is used to get the default account(s) for a Petty Cash Document
   OperationID: GetPCashDocDefaultAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPCashDocDefaultAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPCashDocDefaultAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankTranBankFeeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankTranBankFeeID
   OperationID: OnChangeBankTranBankFeeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankTranBankFeeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankTranBankFeeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankTranTaxAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankTranTaxAmt
   Description: Call method when the user changes the Tax Amt in Tax screen.
   OperationID: OnChangeBankTranTaxAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankTranTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankTranTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankTranTaxCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankTranTaxCode
   Description: Call method when the user changes the Tax ID in Tax maintainence.
   OperationID: OnChangeBankTranTaxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankTranTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankTranTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankTranTaxPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankTranTaxPercent
   Description: Call method when the user changes the Tax Percent.
   OperationID: OnChangeBankTranTaxPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankTranTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankTranTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankTranTaxRateCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankTranTaxRateCode
   Description: This method updates the dataset when the RateCode field changes
   OperationID: OnChangeBankTranTaxRateCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankTranTaxRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankTranTaxRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankTranTaxTaxableAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankTranTaxTaxableAmt
   Description: Call method when the user changes the Taxable Amt in Tax screen.
   OperationID: OnChangeBankTranTaxTaxableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankTranTaxTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankTranTaxTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankTranTranAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankTranTranAmt
   Description: This method updates the BankTran amounts when the adjustment amount changes or
the currency switch toggles.
   OperationID: OnChangeBankTranTranAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankTranTranAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankTranTranAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCashDocApplyDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCashDocApplyDate
   Description: Occurs when Apply Date is changed
   OperationID: OnChangePCashDocApplyDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCashDocBankAcctID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCashDocBankAcctID
   Description: Occurs when Bank Account is changed
   OperationID: OnChangePCashDocBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCashDocCashAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCashDocCashAmt
   Description: This method updates the bank amounts when the cash amount changes
   OperationID: OnChangePCashDocCashAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocCashAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocCashAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCashDocCashDeskIDTransfer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCashDocCashDeskIDTransfer
   Description: Occurs when Cash Desk ID Transfer is changed
   OperationID: OnChangePCashDocCashDeskIDTransfer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocCashDeskIDTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocCashDeskIDTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCashDocCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCashDocCustID
   Description: Occurs when Customer is changed
   OperationID: OnChangePCashDocCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCashDocDraft(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCashDocDraft
   Description: Occurs when Apply Date is changed
   OperationID: OnChangePCashDocDraft
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocDraft_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocDraft_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCashDocEmployeeNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCashDocEmployeeNum
   Description: Occurs when Employee is changed
   OperationID: OnChangePCashDocEmployeeNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocEmployeeNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocEmployeeNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCashDocExchRateDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCashDocExchRateDate
   Description: Occurs when Apply Date is changed
   OperationID: OnChangePCashDocExchRateDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocExchRateDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocExchRateDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCashDocOprType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCashDocOprType
   Description: Occurs when Operation type was changed
   OperationID: OnChangePCashDocOprType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocOprType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocOprType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCashDocVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCashDocVendorID
   Description: Occurs when Vendor is changed
   OperationID: OnChangePCashDocVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCashDocVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCashDocVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Recalculate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Recalculate
   Description: Recalculate amounts according to Exchange Rate Date
   OperationID: Recalculate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Recalculate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Recalculate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePCashDoc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePCashDoc
   Description: Call this method after calling other business objects like
Cash Receipts, PaymentEntry, Bank Adjustment etc.
This method updates the PCashDoc record with the
data from other business objects.
   OperationID: UpdatePCashDoc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePCashDoc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePCashDoc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: GetLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the Document.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLegalNumber
   Description: Voids the legal number.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumGenOpts datatable if
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePost
   Description: PrePost method to check accounts before posting.
   OperationID: PrePost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPCashDoc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPCashDoc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPCashDoc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCashDoc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashDoc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPCashDocAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPCashDocAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPCashDocAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCashDocAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashDocAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankTranTaxDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankTranTaxDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankTranTaxDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankTranTaxDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTranTaxDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankTranTGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankTranTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankTranTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankTranTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankTranTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPCashDocTGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPCashDocTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPCashDocTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCashDocTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashDocTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BankTranRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BankTranTGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankTranTaxDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BankTranTaxDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PCashDocAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocLinkedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PCashDocLinkedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PCashDocListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PCashDocRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDocTGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PCashDocTGLCRow] = obj["value"]
      pass

class Erp_Tablesets_BankTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Relates record to a BankAcct.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID of the Transaction.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date that the transaction took place.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Amount of the Transaction  """  
      self.TranRef:str = obj["TranRef"]
      """  Transaction Reference  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates that the Transaction (not cleared variance) has been posted to G/L.  When the Bank Statement is posted all Non-G/L Posted adjustments for the bank are posted to G/L using the Bank Account's Cash and Bank Fee Accounts. G/L Posted Transactions cannot be deleted. (System Set)  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Person who entered the transaction (System Set).  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date that the Transaction was entered into the system (System Set).  """  
      self.EntryTime:str = obj["EntryTime"]
      """  Time that the transaction was entered into the system - in HH:MM:SS format (System Set).  """  
      self.TranCleared:bool = obj["TranCleared"]
      """  Indicates the transaction's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.TranClearPending:bool = obj["TranClearPending"]
      """  Indicates that the transaction is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.TranClearedAmt:int = obj["TranClearedAmt"]
      """  Amount that the Transaction was cleared for.  """  
      self.TranClearedPerson:str = obj["TranClearedPerson"]
      """  Person who cleared the transaction (System Set).  """  
      self.TranClearedDate:str = obj["TranClearedDate"]
      """  Date that the Transaction was cleared in the system (System Set).  """  
      self.TranClearedTime:str = obj["TranClearedTime"]
      """  Time that the transaction was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period the transaction was posted to. Only pertains to when posted to GL.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal Number of related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Document amount of the Transaction  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that is used for this bank transaction.  """  
      self.DocTranClearedAmt:int = obj["DocTranClearedAmt"]
      """  Document amount that the Transaction was cleared for.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.GLRefCodeDesc:str = obj["GLRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranClearedAmt:int = obj["Rpt1TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranClearedAmt:int = obj["Rpt2TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranClearedAmt:int = obj["Rpt3TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix that entry applies to.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      """  Unique ID of the Fee  """  
      self.BankFeeAmt:int = obj["BankFeeAmt"]
      """  The Fee amount; this amount plus the Fee tax amount will compose the total of the charge on the statement  """  
      self.BankFeeTaxAmt:int = obj["BankFeeTaxAmt"]
      """  The Tax Amount that has been charged to the fee  """  
      self.DocBankFeeAmt:int = obj["DocBankFeeAmt"]
      """  The Fee amount in Base Currency  """  
      self.DocBankFeeTaxAmt:int = obj["DocBankFeeTaxAmt"]
      """  The Tax Amount that has been charged to the fee in Base Currency  """  
      self.Rpt1BankFeeAmt:int = obj["Rpt1BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2BankFeeAmt:int = obj["Rpt2BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3BankFeeAmt:int = obj["Rpt3BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1BankFeeTaxAmt:int = obj["Rpt1BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2BankFeeTaxAmt:int = obj["Rpt2BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3BankFeeTaxAmt:int = obj["Rpt3BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Used for Bank Fee Functionality, indicates the module that created this BankFee.  This is assigned by the system.
Values can be; AR, AP and BA.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Consecutive from the AP and AR transactions, this field is used to identify the AP or AR transaction that created this Bank Fee  """  
      self.Voided:bool = obj["Voided"]
      """  Indiates if the BankTran has been voided.  The TranNum field will be the same as the original transaction  """  
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
      """  Bank Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Bank Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number for the record.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.CNToCFICode:str = obj["CNToCFICode"]
      """  CNToCFICode  """  
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      """  BankRecGainLoss  """  
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      """  Rpt1BankRecGainLoss  """  
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      """  Rpt2BankRecGainLoss  """  
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      """  Rpt3BankRecGainLoss  """  
      self.BalanceUpdated:int = obj["BalanceUpdated"]
      """  BalanceUpdated  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      """  DocBankRecGainLoss  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that transaction is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.Plant:str = obj["Plant"]
      """  Multi-Site related Site  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CRCurrCode:str = obj["CRCurrCode"]
      """  Cash Receipt currency code  """  
      self.CRRateGrpCode:str = obj["CRRateGrpCode"]
      """  Cash Receipt Rate group code  """  
      self.CRTranAmt:int = obj["CRTranAmt"]
      """  Cash Receipt Tran amount  """  
      self.CRTranClearedAmt:int = obj["CRTranClearedAmt"]
      """  Cash Receipt Transaction Cleared Amount  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency Switch  """  
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DispAmtReverse:bool = obj["DispAmtReverse"]
      """  The flag to indicate if the Display amount is supposed to be reversed  """  
      self.DispDocTranAmt:int = obj["DispDocTranAmt"]
      self.DispDocTranClearedAmt:int = obj["DispDocTranClearedAmt"]
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DispTranClearedAmt:int = obj["DispTranClearedAmt"]
      self.InternalDate:str = obj["InternalDate"]
      """  Used for tree structure/parent view definition in Petty Cash Entry  """  
      self.IsFiltered:bool = obj["IsFiltered"]
      self.IsLockedBankRec:bool = obj["IsLockedBankRec"]
      """  Indicates if the record is locked by review journal for bank reconciliation  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt1DispTranClearedAmt:int = obj["Rpt1DispTranClearedAmt"]
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt2DispTranClearedAmt:int = obj["Rpt2DispTranClearedAmt"]
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt3DispTranClearedAmt:int = obj["Rpt3DispTranClearedAmt"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.GLAccount:str = obj["GLAccount"]
      """  Display GL Account  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankFeeIDDescription:str = obj["BankFeeIDDescription"]
      self.BankFeeIDTaxCode:str = obj["BankFeeIDTaxCode"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankTranTGLCRow:
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
      self.GroupID:str = obj["GroupID"]
      """  GroupID for relation to BankTran  """  
      self.HeadNum:int = obj["HeadNum"]
      self.InternalDate:str = obj["InternalDate"]
      """  Used for tree structure/parent view definition in Petty Cash Entry  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      self.PCashRefNum:int = obj["PCashRefNum"]
      self.Voided:bool = obj["Voided"]
      """  Voided flag for relation to BankTran  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID for relation to BankTran  """  
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

class Erp_Tablesets_BankTranTaxDtlRow:
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
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CTDescription:str = obj["CTDescription"]
      self.DisableManual:bool = obj["DisableManual"]
      """  Flag to indicate if Manual checkbox should be disabled  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.InternalDate:str = obj["InternalDate"]
      """  Used for tree structure/parent view definition in Petty Cash Entry  """  
      self.IsFiltered:bool = obj["IsFiltered"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
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

class Erp_Tablesets_PCashDocAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.ReferenceNum:int = obj["ReferenceNum"]
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

class Erp_Tablesets_PCashDocLinkedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.ReferenceNum:int = obj["ReferenceNum"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.Description:str = obj["Description"]
      """  Description of the linked document  """  
      self.TranAmt:int = obj["TranAmt"]
      self.OprClassDesc:str = obj["OprClassDesc"]
      """  Description of the operation class  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      self.DocReference:str = obj["DocReference"]
      """  The reference number of the linked document (i.e. ap/ar invoice number)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.LinkedSeq:int = obj["LinkedSeq"]
      """  Internal sequence for uniqueness  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID of the linked document  """  
      self.TranNum:int = obj["TranNum"]
      """  Tran num of the linked document  """  
      self.InternalDate:str = obj["InternalDate"]
      self.Module:str = obj["Module"]
      """  The module of the linked document, i.e. A/R, A/P.  """  
      self.TranType:str = obj["TranType"]
      """  The type of transaction  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date when applicable  """  
      self.DueDate:str = obj["DueDate"]
      """  Invoice due date when applicable  """  
      self.DocDiscAmt:int = obj["DocDiscAmt"]
      self.DiscAmt:int = obj["DiscAmt"]
      self.WithholdAmt:int = obj["WithholdAmt"]
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      self.GainLoss:int = obj["GainLoss"]
      """  Gain/Loss  """  
      self.DocGainLoss:int = obj["DocGainLoss"]
      """  Gain/Loss  """  
      self.Rpt1DiscAmt:int = obj["Rpt1DiscAmt"]
      self.Rpt2DiscAmt:int = obj["Rpt2DiscAmt"]
      self.Rpt3DiscAmt:int = obj["Rpt3DiscAmt"]
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      self.Rpt1GainLoss:int = obj["Rpt1GainLoss"]
      """  Gain/Loss  """  
      self.Rpt2GainLoss:int = obj["Rpt2GainLoss"]
      """  Gain/Loss  """  
      self.Rpt3GainLoss:int = obj["Rpt3GainLoss"]
      """  Gain/Loss  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashDocListRow:
   def __init__(self, obj):
      self.CashDeskID:str = obj["CashDeskID"]
      """  Unique identifier of Cash Desk  """  
      self.ReferenceNum:int = obj["ReferenceNum"]
      """  Reference Number, unique identifier of Petty Cash Document, sequentially assigned for each Petty Cash Desk internal number (never reused)  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date of Operation  """  
      self.DaySeqNum:int = obj["DaySeqNum"]
      """  Sequential number of Cash Receipt or Cash Issue for Petty Cask Desk within Apply Cash Day. Used for Authorized documents only.  """  
      self.Direction:str = obj["Direction"]
      """   CI ? Cash Issue
CR ? Cash Receipt  """  
      self.Draft:bool = obj["Draft"]
      """  Available only when configuration of operation type allows using of draft documents.  """  
      self.ExternalNum:str = obj["ExternalNum"]
      """  Legal Number of the record. Available only for Authorized Documents.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of the record. Available only for Authorized Documents.  """  
      self.OprTypeCode:str = obj["OprTypeCode"]
      """  Unique identifier of Petty Cash Operation Type  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DirectionDesc:str = obj["DirectionDesc"]
      self.OperationTypeIDDescription:str = obj["OperationTypeIDDescription"]
      """  description of operation type  """  
      self.PCashDeskName:str = obj["PCashDeskName"]
      """  PCashDesk Name  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashDocRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CashDeskID:str = obj["CashDeskID"]
      """  Unique identifier of Cash Desk  """  
      self.ReferenceNum:int = obj["ReferenceNum"]
      """  Reference Number, unique identifier of Petty Cash Document, sequentially assigned for each Petty Cash Desk internal number (never reused)  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date of Operation  """  
      self.AuthorizedBy:str = obj["AuthorizedBy"]
      """  User Id of the user who authorize the record.  """  
      self.Cashier:str = obj["Cashier"]
      """  Cashier Name  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  User ID of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date when the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency  """  
      self.DaySeqNum:int = obj["DaySeqNum"]
      """  Sequential number of Cash Receipt or Cash Issue for Petty Cask Desk within Apply Cash Day. Used for Authorized documents only.  """  
      self.Direction:str = obj["Direction"]
      """   CI ? Cash Issue
CR ? Cash Receipt  """  
      self.Draft:bool = obj["Draft"]
      """  Available only when configuration of operation type allows using of draft documents.  """  
      self.ExternalNum:str = obj["ExternalNum"]
      """  Legal Number of the record. Available only for Authorized Documents.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Fiscal Calendar is Company Calendar  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Defined by Apply Date for Company Calendar  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Defined by Apply Date for Company Calendar  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Defined by Apply Date for Company Calendar  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of the record. Available only for Authorized Documents.  """  
      self.OprTypeCode:str = obj["OprTypeCode"]
      """  Unique identifier of Petty Cash Operation Type  """  
      self.PayrollBalOpr:bool = obj["PayrollBalOpr"]
      """  According to Operation Type  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.Printed:bool = obj["Printed"]
      """  Printed  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Reason  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Review Journal.  """  
      self.RecipientType:str = obj["RecipientType"]
      """   According to Operation type definition:
E - Employee; S - Supplier; C - Customer; B - Bank; CD - Cash Desk; O - Other  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer  """  
      self.CustShipTo:str = obj["CustShipTo"]
      """  Ship To Customer (CustCon.ShipToNum)  """  
      self.CustConNum:int = obj["CustConNum"]
      """  Customer Contact Number (CustCon.ConNum)  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier  """  
      self.VendPurPoint:str = obj["VendPurPoint"]
      """  Purchase point from Vendor.(VendCon.PurPoint)  """  
      self.VendConNum:int = obj["VendConNum"]
      """  Supplier Contact number (VendCon.ConNum)  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account  """  
      self.OrganizationID:str = obj["OrganizationID"]
      """  Depending on Recipient Type: Supplier ID; Customer ID; Bank Account ID; Cash Desk ID. Not available for Employee and Other.  """  
      self.OrganizationName:str = obj["OrganizationName"]
      """   Depending on Recipient Type: Supplier Name; Customer Name;
Bank Account Name; Cash Desk Name; Company Name (default for Employee and Other Recipient types).  """  
      self.PersonName:str = obj["PersonName"]
      """   Depending on Recipient type: Employee Display Name (composed from First Name, Middle Initial and Last Name); Supplier Contact Display Name; Customer Contact Display Name; Cash Desk Cashier Name, or Entrusted Cashier Name (recipient of cash transfer); Own Cash Desk Cashier name.
Person Name can be modified. There is no default for Bank and Other recipient.  """  
      self.PersonalData:str = obj["PersonalData"]
      """  Default of Personal Data can be composed using BPM, and can be adjusted by user.  """  
      self.DocCashAmt:int = obj["DocCashAmt"]
      """  Amount to be paid/received in cash  """  
      self.CashAmt:int = obj["CashAmt"]
      """  Amount to be paid/received in cash  """  
      self.Rpt1CashAmt:int = obj["Rpt1CashAmt"]
      """  Amount to be paid/received in cash in reporting Currency  """  
      self.Rpt2CashAmt:int = obj["Rpt2CashAmt"]
      """  Amount to be paid/received in cash in reporting Currency  """  
      self.Rpt3CashAmt:int = obj["Rpt3CashAmt"]
      """  Amount to be paid/received in cash in reporting Currency  """  
      self.DocGrossAmt:int = obj["DocGrossAmt"]
      """  Gross Amount to update AP or AR  """  
      self.GrossAmt:int = obj["GrossAmt"]
      """  Gross Amount to update AP or AR  """  
      self.Rpt1GrossAmt:int = obj["Rpt1GrossAmt"]
      """  Gross Amount in reporting Currency  """  
      self.Rpt2GrossAmt:int = obj["Rpt2GrossAmt"]
      """  Gross Amount in reporting Currency  """  
      self.Rpt3GrossAmt:int = obj["Rpt3GrossAmt"]
      """  Gross Amount in reporting Currency  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  Amount of Applied Cash Discount (AP or AR)  """  
      self.Discount:int = obj["Discount"]
      """  Amount of Applied Cash Discount (AP or AR)  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Amount of Applied Cash Discount  in reporting Currency  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Amount of Applied Cash Discount  in reporting Currency  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Amount of Applied Cash Discount  in reporting Currency  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Amount of calculated withhold taxes (AR or AP)  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Amount of calculated withhold taxes (AR or AP)  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Amount of calculated withhold taxes  in reporting currency  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Amount of calculated withhold taxes  in reporting currency  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Amount of calculated withhold taxes  in reporting currency  """  
      self.DocBankAmt:int = obj["DocBankAmt"]
      """  Bank Amount(Bank To Cash / Cash To Bank)  """  
      self.BankAmt:int = obj["BankAmt"]
      """  Bank Amount(Bank To Cash / Cash To Bank)  """  
      self.Rpt1BankAmt:int = obj["Rpt1BankAmt"]
      """  Bank Amount in reporting currency  """  
      self.Rpt2BankAmt:int = obj["Rpt2BankAmt"]
      """  Bank Amount in reporting currency  """  
      self.Rpt3BankAmt:int = obj["Rpt3BankAmt"]
      """  Bank Amount in reporting currency  """  
      self.DocBankFeeAmt:int = obj["DocBankFeeAmt"]
      """  Bank Fee Amount(Bank To Cash / Cash To Bank)  """  
      self.BankFeeAmt:int = obj["BankFeeAmt"]
      """  Bank Fee Amount(Bank To Cash / Cash To Bank)  """  
      self.Rpt1BankFeeAmt:int = obj["Rpt1BankFeeAmt"]
      """  Bank Fee Amount in reporting currency  """  
      self.Rpt2BankFeeAmt:int = obj["Rpt2BankFeeAmt"]
      """  Bank Fee Amount in reporting currency  """  
      self.Rpt3BankFeeAmt:int = obj["Rpt3BankFeeAmt"]
      """  Bank Fee Amount in reporting currency  """  
      self.RateGrpType:str = obj["RateGrpType"]
      """  Rate Type  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.OnAcctBankAcctID:str = obj["OnAcctBankAcctID"]
      """  OnAcctBankAcctID  """  
      self.ReceiptAmt:int = obj["ReceiptAmt"]
      """  ReceiptAmt  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.Payee:str = obj["Payee"]
      """  Payee  """  
      self.AccountNumber:str = obj["AccountNumber"]
      """  AccountNumber  """  
      self.OtherDetails:str = obj["OtherDetails"]
      """  OtherDetails  """  
      self.PayMethodPMUID:int = obj["PayMethodPMUID"]
      """  PayMethodPMUID  """  
      self.PayMethodName:str = obj["PayMethodName"]
      """  PayMethodName  """  
      self.PayMethodReference:str = obj["PayMethodReference"]
      """  PayMethodReference  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CashDeskIDTransfer:str = obj["CashDeskIDTransfer"]
      """  CashDeskIDTransfer  """  
      self.ExchangeRateDate:str = obj["ExchangeRateDate"]
      """  ExchangeRateDate  """  
      self.ExchRateDateUserDefined:bool = obj["ExchRateDateUserDefined"]
      """  ExchRateDateUserDefined  """  
      self.PrintPage:int = obj["PrintPage"]
      """  PrintPage  """  
      self.PrintPageLegalNum:str = obj["PrintPageLegalNum"]
      """  PrintPageLegalNum  """  
      self.Reason:str = obj["Reason"]
      """  Reason  """  
      self.AllowChangeAfterPrint:bool = obj["AllowChangeAfterPrint"]
      self.BankPersonalData:str = obj["BankPersonalData"]
      self.CashDeskTransferName:str = obj["CashDeskTransferName"]
      """  Cash Desk Transfer from/to Name for CashDesk to CashDesk documents  """  
      self.CDPersonalData:str = obj["CDPersonalData"]
      self.CustomerPersonalData:str = obj["CustomerPersonalData"]
      self.CustomerPersonName:str = obj["CustomerPersonName"]
      self.DirectionDesc:str = obj["DirectionDesc"]
      self.EmpPersonalData:str = obj["EmpPersonalData"]
      self.EnableAssignLegalNum:bool = obj["EnableAssignLegalNum"]
      self.EnableDraft:bool = obj["EnableDraft"]
      self.EnableExchangeRateDate:bool = obj["EnableExchangeRateDate"]
      """  Enable the exchange rate date  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.InternalDate:str = obj["InternalDate"]
      """  Internal date used to set the parent view to PCashDocDates, which is defined in the UI.  """  
      self.IsLcked:bool = obj["IsLcked"]
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be posted: an invoice is already in review journal or in posting process  """  
      self.OprClassDesc:str = obj["OprClassDesc"]
      self.OtherPersonalData:str = obj["OtherPersonalData"]
      self.SupplierPersonalData:str = obj["SupplierPersonalData"]
      self.TreeNodeText:str = obj["TreeNodeText"]
      """  Text for the tree node  """  
      self.UserCanPrint:bool = obj["UserCanPrint"]
      """  Indicates if the user can print the document  """  
      self.EnableApplyDate:bool = obj["EnableApplyDate"]
      """  Indicates if the apply date is enabled  """  
      self.CashReversed:bool = obj["CashReversed"]
      """  Reversed Petty Cash Trans.  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      self.BaseCurrCurrencyCode:str = obj["BaseCurrCurrencyCode"]
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CustCntLastName:str = obj["CustCntLastName"]
      self.CustCntCorpName:str = obj["CustCntCorpName"]
      self.CustCntFirstName:str = obj["CustCntFirstName"]
      self.CustCntFaxNum:str = obj["CustCntFaxNum"]
      self.CustCntPhoneNum:str = obj["CustCntPhoneNum"]
      self.CustCntMiddleName:str = obj["CustCntMiddleName"]
      self.CustCntName:str = obj["CustCntName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.EmployeeName:str = obj["EmployeeName"]
      self.OperationTypeIDDescription:str = obj["OperationTypeIDDescription"]
      self.OperationTypeIDPayrollBal:bool = obj["OperationTypeIDPayrollBal"]
      self.OperationTypeIDOprClass:str = obj["OperationTypeIDOprClass"]
      self.PCashDeskCurrencyCode:str = obj["PCashDeskCurrencyCode"]
      self.PCashDeskName:str = obj["PCashDeskName"]
      self.PCashDeskOprAllowDraftDoc:bool = obj["PCashDeskOprAllowDraftDoc"]
      self.PCashDeskOprAllowUseExtnNum:bool = obj["PCashDeskOprAllowUseExtnNum"]
      self.PCashDeskOprTranDocTypeID:str = obj["PCashDeskOprTranDocTypeID"]
      self.VendCntEmailAddress:str = obj["VendCntEmailAddress"]
      self.VendCntPhoneNum:str = obj["VendCntPhoneNum"]
      self.VendCntFaxNum:str = obj["VendCntFaxNum"]
      self.VendCntName:str = obj["VendCntName"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorName:str = obj["VendorName"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashDocTGLCRow:
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
      self.CashDeskID:str = obj["CashDeskID"]
      self.ReferenceNum:int = obj["ReferenceNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AssignLegalNumber_input:
   """ Required : 
   ipCashDeskID
   ipReferenceNum
   ds
   """  
   def __init__(self, obj):
      self.ipCashDeskID:str = obj["ipCashDeskID"]
      """  Cash Desk ID  """  
      self.ipReferenceNum:int = obj["ipReferenceNum"]
      """  Cash Doc Reference Num  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class AssignLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      self.opLegalNumMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CreateLine_input:
   """ Required : 
   ipCashDeskID
   ipReferenceNum
   ipLineType
   """  
   def __init__(self, obj):
      self.ipCashDeskID:str = obj["ipCashDeskID"]
      """  Identifier of Cash Desk  """  
      self.ipReferenceNum:int = obj["ipReferenceNum"]
      """  Petty Cash document number  """  
      self.ipLineType:str = obj["ipLineType"]
      """  Line type  """  
      pass

class CreateLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opGroupID:str = obj["parameters"]
      self.opLineNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   cashDeskID
   referenceNum
   """  
   def __init__(self, obj):
      self.cashDeskID:str = obj["cashDeskID"]
      self.referenceNum:int = obj["referenceNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_BankTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Relates record to a BankAcct.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID of the Transaction.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date that the transaction took place.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Amount of the Transaction  """  
      self.TranRef:str = obj["TranRef"]
      """  Transaction Reference  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates that the Transaction (not cleared variance) has been posted to G/L.  When the Bank Statement is posted all Non-G/L Posted adjustments for the bank are posted to G/L using the Bank Account's Cash and Bank Fee Accounts. G/L Posted Transactions cannot be deleted. (System Set)  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Person who entered the transaction (System Set).  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date that the Transaction was entered into the system (System Set).  """  
      self.EntryTime:str = obj["EntryTime"]
      """  Time that the transaction was entered into the system - in HH:MM:SS format (System Set).  """  
      self.TranCleared:bool = obj["TranCleared"]
      """  Indicates the transaction's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.TranClearPending:bool = obj["TranClearPending"]
      """  Indicates that the transaction is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.TranClearedAmt:int = obj["TranClearedAmt"]
      """  Amount that the Transaction was cleared for.  """  
      self.TranClearedPerson:str = obj["TranClearedPerson"]
      """  Person who cleared the transaction (System Set).  """  
      self.TranClearedDate:str = obj["TranClearedDate"]
      """  Date that the Transaction was cleared in the system (System Set).  """  
      self.TranClearedTime:str = obj["TranClearedTime"]
      """  Time that the transaction was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period the transaction was posted to. Only pertains to when posted to GL.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal Number of related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Document amount of the Transaction  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that is used for this bank transaction.  """  
      self.DocTranClearedAmt:int = obj["DocTranClearedAmt"]
      """  Document amount that the Transaction was cleared for.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.GLRefCodeDesc:str = obj["GLRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranClearedAmt:int = obj["Rpt1TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranClearedAmt:int = obj["Rpt2TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranClearedAmt:int = obj["Rpt3TranClearedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix that entry applies to.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      """  Unique ID of the Fee  """  
      self.BankFeeAmt:int = obj["BankFeeAmt"]
      """  The Fee amount; this amount plus the Fee tax amount will compose the total of the charge on the statement  """  
      self.BankFeeTaxAmt:int = obj["BankFeeTaxAmt"]
      """  The Tax Amount that has been charged to the fee  """  
      self.DocBankFeeAmt:int = obj["DocBankFeeAmt"]
      """  The Fee amount in Base Currency  """  
      self.DocBankFeeTaxAmt:int = obj["DocBankFeeTaxAmt"]
      """  The Tax Amount that has been charged to the fee in Base Currency  """  
      self.Rpt1BankFeeAmt:int = obj["Rpt1BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2BankFeeAmt:int = obj["Rpt2BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3BankFeeAmt:int = obj["Rpt3BankFeeAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1BankFeeTaxAmt:int = obj["Rpt1BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2BankFeeTaxAmt:int = obj["Rpt2BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3BankFeeTaxAmt:int = obj["Rpt3BankFeeTaxAmt"]
      """  Reporting currency value of this field  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Used for Bank Fee Functionality, indicates the module that created this BankFee.  This is assigned by the system.
Values can be; AR, AP and BA.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Consecutive from the AP and AR transactions, this field is used to identify the AP or AR transaction that created this Bank Fee  """  
      self.Voided:bool = obj["Voided"]
      """  Indiates if the BankTran has been voided.  The TranNum field will be the same as the original transaction  """  
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
      """  Bank Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Bank Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Bank Balance at the time of revaluation  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number for the record.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.CNToCFICode:str = obj["CNToCFICode"]
      """  CNToCFICode  """  
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      """  BankRecGainLoss  """  
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      """  Rpt1BankRecGainLoss  """  
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      """  Rpt2BankRecGainLoss  """  
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      """  Rpt3BankRecGainLoss  """  
      self.BalanceUpdated:int = obj["BalanceUpdated"]
      """  BalanceUpdated  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      """  DocBankRecGainLoss  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that transaction is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.Plant:str = obj["Plant"]
      """  Multi-Site related Site  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CRCurrCode:str = obj["CRCurrCode"]
      """  Cash Receipt currency code  """  
      self.CRRateGrpCode:str = obj["CRRateGrpCode"]
      """  Cash Receipt Rate group code  """  
      self.CRTranAmt:int = obj["CRTranAmt"]
      """  Cash Receipt Tran amount  """  
      self.CRTranClearedAmt:int = obj["CRTranClearedAmt"]
      """  Cash Receipt Transaction Cleared Amount  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency Switch  """  
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DispAmtReverse:bool = obj["DispAmtReverse"]
      """  The flag to indicate if the Display amount is supposed to be reversed  """  
      self.DispDocTranAmt:int = obj["DispDocTranAmt"]
      self.DispDocTranClearedAmt:int = obj["DispDocTranClearedAmt"]
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DispTranClearedAmt:int = obj["DispTranClearedAmt"]
      self.InternalDate:str = obj["InternalDate"]
      """  Used for tree structure/parent view definition in Petty Cash Entry  """  
      self.IsFiltered:bool = obj["IsFiltered"]
      self.IsLockedBankRec:bool = obj["IsLockedBankRec"]
      """  Indicates if the record is locked by review journal for bank reconciliation  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt1DispTranClearedAmt:int = obj["Rpt1DispTranClearedAmt"]
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt2DispTranClearedAmt:int = obj["Rpt2DispTranClearedAmt"]
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt3DispTranClearedAmt:int = obj["Rpt3DispTranClearedAmt"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.GLAccount:str = obj["GLAccount"]
      """  Display GL Account  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankFeeIDDescription:str = obj["BankFeeIDDescription"]
      self.BankFeeIDTaxCode:str = obj["BankFeeIDTaxCode"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankTranTGLCRow:
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
      self.GroupID:str = obj["GroupID"]
      """  GroupID for relation to BankTran  """  
      self.HeadNum:int = obj["HeadNum"]
      self.InternalDate:str = obj["InternalDate"]
      """  Used for tree structure/parent view definition in Petty Cash Entry  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      self.PCashRefNum:int = obj["PCashRefNum"]
      self.Voided:bool = obj["Voided"]
      """  Voided flag for relation to BankTran  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID for relation to BankTran  """  
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

class Erp_Tablesets_BankTranTaxDtlRow:
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
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CTDescription:str = obj["CTDescription"]
      self.DisableManual:bool = obj["DisableManual"]
      """  Flag to indicate if Manual checkbox should be disabled  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.InternalDate:str = obj["InternalDate"]
      """  Used for tree structure/parent view definition in Petty Cash Entry  """  
      self.IsFiltered:bool = obj["IsFiltered"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
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

class Erp_Tablesets_PCashDocAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.ReferenceNum:int = obj["ReferenceNum"]
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

class Erp_Tablesets_PCashDocLinkedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.ReferenceNum:int = obj["ReferenceNum"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.Description:str = obj["Description"]
      """  Description of the linked document  """  
      self.TranAmt:int = obj["TranAmt"]
      self.OprClassDesc:str = obj["OprClassDesc"]
      """  Description of the operation class  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      self.DocReference:str = obj["DocReference"]
      """  The reference number of the linked document (i.e. ap/ar invoice number)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.LinkedSeq:int = obj["LinkedSeq"]
      """  Internal sequence for uniqueness  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID of the linked document  """  
      self.TranNum:int = obj["TranNum"]
      """  Tran num of the linked document  """  
      self.InternalDate:str = obj["InternalDate"]
      self.Module:str = obj["Module"]
      """  The module of the linked document, i.e. A/R, A/P.  """  
      self.TranType:str = obj["TranType"]
      """  The type of transaction  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date when applicable  """  
      self.DueDate:str = obj["DueDate"]
      """  Invoice due date when applicable  """  
      self.DocDiscAmt:int = obj["DocDiscAmt"]
      self.DiscAmt:int = obj["DiscAmt"]
      self.WithholdAmt:int = obj["WithholdAmt"]
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      self.GainLoss:int = obj["GainLoss"]
      """  Gain/Loss  """  
      self.DocGainLoss:int = obj["DocGainLoss"]
      """  Gain/Loss  """  
      self.Rpt1DiscAmt:int = obj["Rpt1DiscAmt"]
      self.Rpt2DiscAmt:int = obj["Rpt2DiscAmt"]
      self.Rpt3DiscAmt:int = obj["Rpt3DiscAmt"]
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      self.Rpt1GainLoss:int = obj["Rpt1GainLoss"]
      """  Gain/Loss  """  
      self.Rpt2GainLoss:int = obj["Rpt2GainLoss"]
      """  Gain/Loss  """  
      self.Rpt3GainLoss:int = obj["Rpt3GainLoss"]
      """  Gain/Loss  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashDocListRow:
   def __init__(self, obj):
      self.CashDeskID:str = obj["CashDeskID"]
      """  Unique identifier of Cash Desk  """  
      self.ReferenceNum:int = obj["ReferenceNum"]
      """  Reference Number, unique identifier of Petty Cash Document, sequentially assigned for each Petty Cash Desk internal number (never reused)  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date of Operation  """  
      self.DaySeqNum:int = obj["DaySeqNum"]
      """  Sequential number of Cash Receipt or Cash Issue for Petty Cask Desk within Apply Cash Day. Used for Authorized documents only.  """  
      self.Direction:str = obj["Direction"]
      """   CI ? Cash Issue
CR ? Cash Receipt  """  
      self.Draft:bool = obj["Draft"]
      """  Available only when configuration of operation type allows using of draft documents.  """  
      self.ExternalNum:str = obj["ExternalNum"]
      """  Legal Number of the record. Available only for Authorized Documents.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of the record. Available only for Authorized Documents.  """  
      self.OprTypeCode:str = obj["OprTypeCode"]
      """  Unique identifier of Petty Cash Operation Type  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DirectionDesc:str = obj["DirectionDesc"]
      self.OperationTypeIDDescription:str = obj["OperationTypeIDDescription"]
      """  description of operation type  """  
      self.PCashDeskName:str = obj["PCashDeskName"]
      """  PCashDesk Name  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashDocRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CashDeskID:str = obj["CashDeskID"]
      """  Unique identifier of Cash Desk  """  
      self.ReferenceNum:int = obj["ReferenceNum"]
      """  Reference Number, unique identifier of Petty Cash Document, sequentially assigned for each Petty Cash Desk internal number (never reused)  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date of Operation  """  
      self.AuthorizedBy:str = obj["AuthorizedBy"]
      """  User Id of the user who authorize the record.  """  
      self.Cashier:str = obj["Cashier"]
      """  Cashier Name  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  User ID of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date when the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency  """  
      self.DaySeqNum:int = obj["DaySeqNum"]
      """  Sequential number of Cash Receipt or Cash Issue for Petty Cask Desk within Apply Cash Day. Used for Authorized documents only.  """  
      self.Direction:str = obj["Direction"]
      """   CI ? Cash Issue
CR ? Cash Receipt  """  
      self.Draft:bool = obj["Draft"]
      """  Available only when configuration of operation type allows using of draft documents.  """  
      self.ExternalNum:str = obj["ExternalNum"]
      """  Legal Number of the record. Available only for Authorized Documents.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Fiscal Calendar is Company Calendar  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Defined by Apply Date for Company Calendar  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Defined by Apply Date for Company Calendar  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Defined by Apply Date for Company Calendar  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of the record. Available only for Authorized Documents.  """  
      self.OprTypeCode:str = obj["OprTypeCode"]
      """  Unique identifier of Petty Cash Operation Type  """  
      self.PayrollBalOpr:bool = obj["PayrollBalOpr"]
      """  According to Operation Type  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.Printed:bool = obj["Printed"]
      """  Printed  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Reason  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Review Journal.  """  
      self.RecipientType:str = obj["RecipientType"]
      """   According to Operation type definition:
E - Employee; S - Supplier; C - Customer; B - Bank; CD - Cash Desk; O - Other  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer  """  
      self.CustShipTo:str = obj["CustShipTo"]
      """  Ship To Customer (CustCon.ShipToNum)  """  
      self.CustConNum:int = obj["CustConNum"]
      """  Customer Contact Number (CustCon.ConNum)  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier  """  
      self.VendPurPoint:str = obj["VendPurPoint"]
      """  Purchase point from Vendor.(VendCon.PurPoint)  """  
      self.VendConNum:int = obj["VendConNum"]
      """  Supplier Contact number (VendCon.ConNum)  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account  """  
      self.OrganizationID:str = obj["OrganizationID"]
      """  Depending on Recipient Type: Supplier ID; Customer ID; Bank Account ID; Cash Desk ID. Not available for Employee and Other.  """  
      self.OrganizationName:str = obj["OrganizationName"]
      """   Depending on Recipient Type: Supplier Name; Customer Name;
Bank Account Name; Cash Desk Name; Company Name (default for Employee and Other Recipient types).  """  
      self.PersonName:str = obj["PersonName"]
      """   Depending on Recipient type: Employee Display Name (composed from First Name, Middle Initial and Last Name); Supplier Contact Display Name; Customer Contact Display Name; Cash Desk Cashier Name, or Entrusted Cashier Name (recipient of cash transfer); Own Cash Desk Cashier name.
Person Name can be modified. There is no default for Bank and Other recipient.  """  
      self.PersonalData:str = obj["PersonalData"]
      """  Default of Personal Data can be composed using BPM, and can be adjusted by user.  """  
      self.DocCashAmt:int = obj["DocCashAmt"]
      """  Amount to be paid/received in cash  """  
      self.CashAmt:int = obj["CashAmt"]
      """  Amount to be paid/received in cash  """  
      self.Rpt1CashAmt:int = obj["Rpt1CashAmt"]
      """  Amount to be paid/received in cash in reporting Currency  """  
      self.Rpt2CashAmt:int = obj["Rpt2CashAmt"]
      """  Amount to be paid/received in cash in reporting Currency  """  
      self.Rpt3CashAmt:int = obj["Rpt3CashAmt"]
      """  Amount to be paid/received in cash in reporting Currency  """  
      self.DocGrossAmt:int = obj["DocGrossAmt"]
      """  Gross Amount to update AP or AR  """  
      self.GrossAmt:int = obj["GrossAmt"]
      """  Gross Amount to update AP or AR  """  
      self.Rpt1GrossAmt:int = obj["Rpt1GrossAmt"]
      """  Gross Amount in reporting Currency  """  
      self.Rpt2GrossAmt:int = obj["Rpt2GrossAmt"]
      """  Gross Amount in reporting Currency  """  
      self.Rpt3GrossAmt:int = obj["Rpt3GrossAmt"]
      """  Gross Amount in reporting Currency  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  Amount of Applied Cash Discount (AP or AR)  """  
      self.Discount:int = obj["Discount"]
      """  Amount of Applied Cash Discount (AP or AR)  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Amount of Applied Cash Discount  in reporting Currency  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Amount of Applied Cash Discount  in reporting Currency  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Amount of Applied Cash Discount  in reporting Currency  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Amount of calculated withhold taxes (AR or AP)  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Amount of calculated withhold taxes (AR or AP)  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Amount of calculated withhold taxes  in reporting currency  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Amount of calculated withhold taxes  in reporting currency  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Amount of calculated withhold taxes  in reporting currency  """  
      self.DocBankAmt:int = obj["DocBankAmt"]
      """  Bank Amount(Bank To Cash / Cash To Bank)  """  
      self.BankAmt:int = obj["BankAmt"]
      """  Bank Amount(Bank To Cash / Cash To Bank)  """  
      self.Rpt1BankAmt:int = obj["Rpt1BankAmt"]
      """  Bank Amount in reporting currency  """  
      self.Rpt2BankAmt:int = obj["Rpt2BankAmt"]
      """  Bank Amount in reporting currency  """  
      self.Rpt3BankAmt:int = obj["Rpt3BankAmt"]
      """  Bank Amount in reporting currency  """  
      self.DocBankFeeAmt:int = obj["DocBankFeeAmt"]
      """  Bank Fee Amount(Bank To Cash / Cash To Bank)  """  
      self.BankFeeAmt:int = obj["BankFeeAmt"]
      """  Bank Fee Amount(Bank To Cash / Cash To Bank)  """  
      self.Rpt1BankFeeAmt:int = obj["Rpt1BankFeeAmt"]
      """  Bank Fee Amount in reporting currency  """  
      self.Rpt2BankFeeAmt:int = obj["Rpt2BankFeeAmt"]
      """  Bank Fee Amount in reporting currency  """  
      self.Rpt3BankFeeAmt:int = obj["Rpt3BankFeeAmt"]
      """  Bank Fee Amount in reporting currency  """  
      self.RateGrpType:str = obj["RateGrpType"]
      """  Rate Type  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.OnAcctBankAcctID:str = obj["OnAcctBankAcctID"]
      """  OnAcctBankAcctID  """  
      self.ReceiptAmt:int = obj["ReceiptAmt"]
      """  ReceiptAmt  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.Payee:str = obj["Payee"]
      """  Payee  """  
      self.AccountNumber:str = obj["AccountNumber"]
      """  AccountNumber  """  
      self.OtherDetails:str = obj["OtherDetails"]
      """  OtherDetails  """  
      self.PayMethodPMUID:int = obj["PayMethodPMUID"]
      """  PayMethodPMUID  """  
      self.PayMethodName:str = obj["PayMethodName"]
      """  PayMethodName  """  
      self.PayMethodReference:str = obj["PayMethodReference"]
      """  PayMethodReference  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CashDeskIDTransfer:str = obj["CashDeskIDTransfer"]
      """  CashDeskIDTransfer  """  
      self.ExchangeRateDate:str = obj["ExchangeRateDate"]
      """  ExchangeRateDate  """  
      self.ExchRateDateUserDefined:bool = obj["ExchRateDateUserDefined"]
      """  ExchRateDateUserDefined  """  
      self.PrintPage:int = obj["PrintPage"]
      """  PrintPage  """  
      self.PrintPageLegalNum:str = obj["PrintPageLegalNum"]
      """  PrintPageLegalNum  """  
      self.Reason:str = obj["Reason"]
      """  Reason  """  
      self.AllowChangeAfterPrint:bool = obj["AllowChangeAfterPrint"]
      self.BankPersonalData:str = obj["BankPersonalData"]
      self.CashDeskTransferName:str = obj["CashDeskTransferName"]
      """  Cash Desk Transfer from/to Name for CashDesk to CashDesk documents  """  
      self.CDPersonalData:str = obj["CDPersonalData"]
      self.CustomerPersonalData:str = obj["CustomerPersonalData"]
      self.CustomerPersonName:str = obj["CustomerPersonName"]
      self.DirectionDesc:str = obj["DirectionDesc"]
      self.EmpPersonalData:str = obj["EmpPersonalData"]
      self.EnableAssignLegalNum:bool = obj["EnableAssignLegalNum"]
      self.EnableDraft:bool = obj["EnableDraft"]
      self.EnableExchangeRateDate:bool = obj["EnableExchangeRateDate"]
      """  Enable the exchange rate date  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.InternalDate:str = obj["InternalDate"]
      """  Internal date used to set the parent view to PCashDocDates, which is defined in the UI.  """  
      self.IsLcked:bool = obj["IsLcked"]
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be posted: an invoice is already in review journal or in posting process  """  
      self.OprClassDesc:str = obj["OprClassDesc"]
      self.OtherPersonalData:str = obj["OtherPersonalData"]
      self.SupplierPersonalData:str = obj["SupplierPersonalData"]
      self.TreeNodeText:str = obj["TreeNodeText"]
      """  Text for the tree node  """  
      self.UserCanPrint:bool = obj["UserCanPrint"]
      """  Indicates if the user can print the document  """  
      self.EnableApplyDate:bool = obj["EnableApplyDate"]
      """  Indicates if the apply date is enabled  """  
      self.CashReversed:bool = obj["CashReversed"]
      """  Reversed Petty Cash Trans.  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      self.BaseCurrCurrencyCode:str = obj["BaseCurrCurrencyCode"]
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CustCntLastName:str = obj["CustCntLastName"]
      self.CustCntCorpName:str = obj["CustCntCorpName"]
      self.CustCntFirstName:str = obj["CustCntFirstName"]
      self.CustCntFaxNum:str = obj["CustCntFaxNum"]
      self.CustCntPhoneNum:str = obj["CustCntPhoneNum"]
      self.CustCntMiddleName:str = obj["CustCntMiddleName"]
      self.CustCntName:str = obj["CustCntName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.EmployeeName:str = obj["EmployeeName"]
      self.OperationTypeIDDescription:str = obj["OperationTypeIDDescription"]
      self.OperationTypeIDPayrollBal:bool = obj["OperationTypeIDPayrollBal"]
      self.OperationTypeIDOprClass:str = obj["OperationTypeIDOprClass"]
      self.PCashDeskCurrencyCode:str = obj["PCashDeskCurrencyCode"]
      self.PCashDeskName:str = obj["PCashDeskName"]
      self.PCashDeskOprAllowDraftDoc:bool = obj["PCashDeskOprAllowDraftDoc"]
      self.PCashDeskOprAllowUseExtnNum:bool = obj["PCashDeskOprAllowUseExtnNum"]
      self.PCashDeskOprTranDocTypeID:str = obj["PCashDeskOprTranDocTypeID"]
      self.VendCntEmailAddress:str = obj["VendCntEmailAddress"]
      self.VendCntPhoneNum:str = obj["VendCntPhoneNum"]
      self.VendCntFaxNum:str = obj["VendCntFaxNum"]
      self.VendCntName:str = obj["VendCntName"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorName:str = obj["VendorName"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashDocTGLCRow:
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
      self.CashDeskID:str = obj["CashDeskID"]
      self.ReferenceNum:int = obj["ReferenceNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashEntryListTableset:
   def __init__(self, obj):
      self.PCashDocList:list[Erp_Tablesets_PCashDocListRow] = obj["PCashDocList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PCashEntryTableset:
   def __init__(self, obj):
      self.PCashDoc:list[Erp_Tablesets_PCashDocRow] = obj["PCashDoc"]
      self.PCashDocAttch:list[Erp_Tablesets_PCashDocAttchRow] = obj["PCashDocAttch"]
      self.BankTran:list[Erp_Tablesets_BankTranRow] = obj["BankTran"]
      self.BankTranTaxDtl:list[Erp_Tablesets_BankTranTaxDtlRow] = obj["BankTranTaxDtl"]
      self.BankTranTGLC:list[Erp_Tablesets_BankTranTGLCRow] = obj["BankTranTGLC"]
      self.PCashDocLinked:list[Erp_Tablesets_PCashDocLinkedRow] = obj["PCashDocLinked"]
      self.PCashDocTGLC:list[Erp_Tablesets_PCashDocTGLCRow] = obj["PCashDocTGLC"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPCashEntryTableset:
   def __init__(self, obj):
      self.PCashDoc:list[Erp_Tablesets_PCashDocRow] = obj["PCashDoc"]
      self.PCashDocAttch:list[Erp_Tablesets_PCashDocAttchRow] = obj["PCashDocAttch"]
      self.BankTran:list[Erp_Tablesets_BankTranRow] = obj["BankTran"]
      self.BankTranTaxDtl:list[Erp_Tablesets_BankTranTaxDtlRow] = obj["BankTranTaxDtl"]
      self.BankTranTGLC:list[Erp_Tablesets_BankTranTGLCRow] = obj["BankTranTGLC"]
      self.PCashDocLinked:list[Erp_Tablesets_PCashDocLinkedRow] = obj["PCashDocLinked"]
      self.PCashDocTGLC:list[Erp_Tablesets_PCashDocTGLCRow] = obj["PCashDocTGLC"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetBankFeeDefaultAccount_input:
   """ Required : 
   bankAcctID
   tranNum
   voided
   ds
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      """  The Bank Account ID  """  
      self.tranNum:int = obj["tranNum"]
      """  The Bank Fee Tran Num  """  
      self.voided:bool = obj["voided"]
      """  voided  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class GetBankFeeDefaultAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   cashDeskID
   referenceNum
   """  
   def __init__(self, obj):
      self.cashDeskID:str = obj["cashDeskID"]
      self.referenceNum:int = obj["referenceNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PCashEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PCashEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PCashEntryTableset] = obj["returnObj"]
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

class GetLegalNumGenOpts_input:
   """ Required : 
   ipCashDeskID
   ipReferenceNum
   ds
   """  
   def __init__(self, obj):
      self.ipCashDeskID:str = obj["ipCashDeskID"]
      """  Cash Desk ID  """  
      self.ipReferenceNum:int = obj["ipReferenceNum"]
      """  Cash Doc Reference Num  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class GetLegalNumGenOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
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
      self.returnObj:list[Erp_Tablesets_PCashEntryListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewBankTranForPCashDoc_input:
   """ Required : 
   inCashDeskID
   inReferenceNum
   ds
   """  
   def __init__(self, obj):
      self.inCashDeskID:str = obj["inCashDeskID"]
      self.inReferenceNum:int = obj["inReferenceNum"]
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class GetNewBankTranForPCashDoc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBankTranTGLC_input:
   """ Required : 
   ds
   bankAcctID
   tranNum
   voided
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.tranNum:int = obj["tranNum"]
      self.voided:bool = obj["voided"]
      pass

class GetNewBankTranTGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBankTranTaxDtl_input:
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
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
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

class GetNewBankTranTaxDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBankTran_input:
   """ Required : 
   ds
   bankAcctID
   tranNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.tranNum:int = obj["tranNum"]
      pass

class GetNewBankTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPCashDocAttch_input:
   """ Required : 
   ds
   cashDeskID
   referenceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      self.cashDeskID:str = obj["cashDeskID"]
      self.referenceNum:int = obj["referenceNum"]
      pass

class GetNewPCashDocAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPCashDocByType_input:
   """ Required : 
   inCashDeskID
   inNewType
   ds
   """  
   def __init__(self, obj):
      self.inCashDeskID:str = obj["inCashDeskID"]
      self.inNewType:str = obj["inNewType"]
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class GetNewPCashDocByType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outDocDate:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPCashDocTGLC_input:
   """ Required : 
   ds
   cashDeskID
   referenceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      self.cashDeskID:str = obj["cashDeskID"]
      self.referenceNum:int = obj["referenceNum"]
      pass

class GetNewPCashDocTGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPCashDoc_input:
   """ Required : 
   ds
   cashDeskID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      self.cashDeskID:str = obj["cashDeskID"]
      pass

class GetNewPCashDoc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPCashDocDefaultAccount_input:
   """ Required : 
   cashDeskID
   referenceNum
   ds
   """  
   def __init__(self, obj):
      self.cashDeskID:str = obj["cashDeskID"]
      """  The Petty Cash ID  """  
      self.referenceNum:int = obj["referenceNum"]
      """  The Petty Cash Reference Num  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class GetPCashDocDefaultAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePCashDoc
   whereClausePCashDocAttch
   whereClauseBankTran
   whereClauseBankTranTaxDtl
   whereClauseBankTranTGLC
   whereClausePCashDocLinked
   whereClausePCashDocTGLC
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePCashDoc:str = obj["whereClausePCashDoc"]
      self.whereClausePCashDocAttch:str = obj["whereClausePCashDocAttch"]
      self.whereClauseBankTran:str = obj["whereClauseBankTran"]
      self.whereClauseBankTranTaxDtl:str = obj["whereClauseBankTranTaxDtl"]
      self.whereClauseBankTranTGLC:str = obj["whereClauseBankTranTGLC"]
      self.whereClausePCashDocLinked:str = obj["whereClausePCashDocLinked"]
      self.whereClausePCashDocTGLC:str = obj["whereClausePCashDocTGLC"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PCashEntryTableset] = obj["returnObj"]
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

class OnChangeBankTranBankFeeID_input:
   """ Required : 
   inBankFeeID
   ds
   """  
   def __init__(self, obj):
      self.inBankFeeID:str = obj["inBankFeeID"]
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangeBankTranBankFeeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBankTranTaxAmt_input:
   """ Required : 
   inAmtType
   inTaxAmt
   ds
   """  
   def __init__(self, obj):
      self.inAmtType:str = obj["inAmtType"]
      """  Indicate which of the amount is changed.
            Valid values are: 'B' for Base Amount and 'D' for Doc Amount  """  
      self.inTaxAmt:int = obj["inTaxAmt"]
      """  Proposed taxable amount value  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangeBankTranTaxAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBankTranTaxCode_input:
   """ Required : 
   inTaxCode
   ds
   """  
   def __init__(self, obj):
      self.inTaxCode:str = obj["inTaxCode"]
      """  Proposed Tax ID  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangeBankTranTaxCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBankTranTaxPercent_input:
   """ Required : 
   inPercent
   ds
   """  
   def __init__(self, obj):
      self.inPercent:int = obj["inPercent"]
      """  Proposed taxable amount value  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangeBankTranTaxPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBankTranTaxRateCode_input:
   """ Required : 
   inRateCode
   ds
   """  
   def __init__(self, obj):
      self.inRateCode:str = obj["inRateCode"]
      """  Proposed RateCode value  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangeBankTranTaxRateCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBankTranTaxTaxableAmt_input:
   """ Required : 
   inAmtType
   inTaxableAmt
   ds
   """  
   def __init__(self, obj):
      self.inAmtType:str = obj["inAmtType"]
      """  Indicate which of the amount is changed.
            Valid values are: 'B' for Base Amount and 'D' for Doc Amount  """  
      self.inTaxableAmt:int = obj["inTaxableAmt"]
      """  Proposed taxable amount value  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangeBankTranTaxTaxableAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBankTranTranAmt_input:
   """ Required : 
   ipTranAmtType
   proposedTranAmt
   ds
   """  
   def __init__(self, obj):
      self.ipTranAmtType:str = obj["ipTranAmtType"]
      """  Indicate which of the transaction amount is changed.
            Valid values are: 'B' for Base Tran Amount and 'D' for Doc Tran Amount  """  
      self.proposedTranAmt:int = obj["proposedTranAmt"]
      """  The proposed Transaction Amount  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangeBankTranTranAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCashDocApplyDate_input:
   """ Required : 
   ipApplyDate
   ds
   """  
   def __init__(self, obj):
      self.ipApplyDate:str = obj["ipApplyDate"]
      """  New Apply Date  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangePCashDocApplyDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCashDocBankAcctID_input:
   """ Required : 
   ipBankAcctID
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcctID:str = obj["ipBankAcctID"]
      """  New Bank Acct ID  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangePCashDocBankAcctID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCashDocCashAmt_input:
   """ Required : 
   inAmtType
   proposedCashAmt
   ds
   """  
   def __init__(self, obj):
      self.inAmtType:str = obj["inAmtType"]
      """  Indicate which of the cash amount is changed.
            Valid values are: 'B' for Base Cash Amount and 'D' for Doc Cash Amount  """  
      self.proposedCashAmt:int = obj["proposedCashAmt"]
      """  The proposed Transaction Amount  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangePCashDocCashAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCashDocCashDeskIDTransfer_input:
   """ Required : 
   ipCashDeskIDTransfer
   ds
   """  
   def __init__(self, obj):
      self.ipCashDeskIDTransfer:str = obj["ipCashDeskIDTransfer"]
      """  New Cash Desk ID Num  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangePCashDocCashDeskIDTransfer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCashDocCustID_input:
   """ Required : 
   ipCustomerID
   ds
   """  
   def __init__(self, obj):
      self.ipCustomerID:str = obj["ipCustomerID"]
      """  New Customer ID  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangePCashDocCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCashDocDraft_input:
   """ Required : 
   ipDraft
   ds
   """  
   def __init__(self, obj):
      self.ipDraft:bool = obj["ipDraft"]
      """  New Draft  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangePCashDocDraft_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opDateChangedMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCashDocEmployeeNum_input:
   """ Required : 
   ipEmployeeNum
   ds
   """  
   def __init__(self, obj):
      self.ipEmployeeNum:str = obj["ipEmployeeNum"]
      """  New Employee Num  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangePCashDocEmployeeNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCashDocExchRateDate_input:
   """ Required : 
   ipExchRateDate
   ds
   """  
   def __init__(self, obj):
      self.ipExchRateDate:str = obj["ipExchRateDate"]
      """  New Exchange Rate Date  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangePCashDocExchRateDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCashDocOprType_input:
   """ Required : 
   ipOprTypeCode
   ds
   """  
   def __init__(self, obj):
      self.ipOprTypeCode:str = obj["ipOprTypeCode"]
      """  New Operation type code  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangePCashDocOprType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCashDocVendorID_input:
   """ Required : 
   ipVendorID
   ds
   """  
   def __init__(self, obj):
      self.ipVendorID:str = obj["ipVendorID"]
      """  New Vendor ID  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class OnChangePCashDocVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PrePost_input:
   """ Required : 
   CashDeskID
   ReferenceNum
   """  
   def __init__(self, obj):
      self.CashDeskID:str = obj["CashDeskID"]
      """  Petty Cash Desk  """  
      self.ReferenceNum:int = obj["ReferenceNum"]
      """  Reference number  """  
      pass

class PrePost_output:
   def __init__(self, obj):
      pass

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class Recalculate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class Recalculate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPCashEntryTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPCashEntryTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdatePCashDoc_input:
   """ Required : 
   pCashDeskID
   pReferenceNum
   """  
   def __init__(self, obj):
      self.pCashDeskID:str = obj["pCashDeskID"]
      """  Cash Desk ID  """  
      self.pReferenceNum:int = obj["pReferenceNum"]
      """  Cash Desk reference number  """  
      pass

class UpdatePCashDoc_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PCashEntryTableset] = obj["returnObj"]
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VoidLegalNumber_input:
   """ Required : 
   pCashDeskId
   referenceNum
   VoidedReason
   ds
   """  
   def __init__(self, obj):
      self.pCashDeskId:str = obj["pCashDeskId"]
      """  The cash desk ID.  """  
      self.referenceNum:int = obj["referenceNum"]
      """  The reference number.  """  
      self.VoidedReason:str = obj["VoidedReason"]
      """  Reason for the void  """  
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

class VoidLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

